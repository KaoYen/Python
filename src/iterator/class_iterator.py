class NumberSequence:
    def __init__(self, start=0):
        self.current = start

    def next(self):
        current = self.current
        self.current += 1
        return current


class NewNumberSequence:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    """
    使用自定義類別
    """
    # seq = NumberSequence()
    # print(seq.next())
    # print(seq.next())

    # 用for 迴圈進行迭代的錯誤情況
    # list(zip(NumberSequence(), 'abcdefg'))


    """
    實作__iter__ and __next__ 魔術方法
    """
    print(list(zip(NewNumberSequence(), 'abcdefg')))


    """
    1. next() 內建函式可以將可迭代物移到它的下一個元素並回傳
    2. 如果迭代器沒有元素可以產生，就會引發 StopIteration 例外，這個例外指出迭代已經結束，沒有其他元素可以使用了
    """
    word = iter('hello')
    print(next(word))
    print(next(word))
    print(next(word))
    print(next(word))
    print(next(word))
    print(next(word))
