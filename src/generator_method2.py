import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class DBHandler:
    """Simulate reading from the database by pages."""

    def __init__(self, db):
        self.db = db
        self.is_closed = False

    def read_n_records(self, limit):
        return [(i, f"row {i}") for i in range(limit)]

    def close(self):
        logger.debug("closing connection to database %r", self.db)
        self.is_closed = True


def _stream_db_records(db_handler):
    retrieved_data = None
    previous_page_size = 10
    try:
        while True:
            page_size = yield retrieved_data
            if page_size is None:
                page_size = previous_page_size

            previous_page_size = page_size

            retrieved_data = db_handler.read_n_records(page_size)
    except GeneratorExit:
        db_handler.close()


def stream_db_records(db_handler):
    retrieved_data = None
    page_size = 10
    try:
        while True:
            page_size = (yield retrieved_data) or page_size
            retrieved_data = db_handler.read_n_records(page_size)
    except GeneratorExit:
        db_handler.close()

def prepare_coroutine(coroutine):
    def wrapped(*args, **kwargs):
        advanced_coroutine = coroutine(*args, **kwargs)
        next(advanced_coroutine)
        return advanced_coroutine

    return wrapped


@prepare_coroutine
def auto_stream_db_records(db_handler):
    """This coroutine is automatically advanced so it doesn't need the first
    next() call.
    """
    retrieved_data = None
    page_size = 10
    try:
        while True:
            page_size = (yield retrieved_data) or page_size
            retrieved_data = db_handler.read_n_records(page_size)
    except GeneratorExit:
        db_handler.close()


if __name__ == '__main__':
    db_handler = stream_db_records(DBHandler('db'))
    # db_handler = auto_stream_db_records(DBHandler('db'))
    # db_handler = _stream_db_records(DBHandler('db'))
    print(next(db_handler))
    print(next(db_handler))
    print(db_handler.send(213))
