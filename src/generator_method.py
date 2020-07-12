import time

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


def stream_db_records(db_handler):
    """Example of .close()
    >>> streamer = stream_db_records(DBHandler("testdb"))
    >>> len(next(streamer))
    10
    >>> len(next(streamer))
    10
    """
    try:
        while True:
            yield db_handler.read_n_records(10)
            time.sleep(.1)
    except GeneratorExit:
        db_handler.close()
    # while True:
    #     yield db_handler.read_n_records(10)
    #     time.sleep(.1)


class CustomException(Exception):
    """An exception of the domain model."""


def stream_data(db_handler):
    """Test the ``.throw()`` method.
    >>> streamer = stream_data(DBHandler("testdb"))
    >>> len(next(streamer))
    10
    """
    while True:
        try:
            yield db_handler.read_n_records(10)
        except CustomException as e:
            logger.info("controlled error %r, continuing", e)
        # except Exception as e:
        #     logger.info("unhandled error %r, stopping", e)
        #     db_handler.close()
        #     break


if __name__ == '__main__':
    streamer = stream_db_records(DBHandler("testdb"))
    print(next(streamer))
    print(next(streamer))
    streamer.close()

    # throw()
    # streamer = stream_data(DBHandler("testdb"))
    # print(len(next(streamer)))
    # streamer.throw(CustomException)
    # streamer.throw(RuntimeError)