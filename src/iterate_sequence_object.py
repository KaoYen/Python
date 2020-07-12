import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class MappedRange:
    """對一個數字範圍執行轉換"""

    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transformation(value)
        logger.info(f"Index {index}: {result}")
        return result

    def __len__(self):
        return len(self._wrapped)


if __name__ == '__main__':
    mr = MappedRange(abs, -10, 5)
    print(list(mr))
