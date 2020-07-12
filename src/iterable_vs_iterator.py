class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        """
        iterable
        :return:
        """
        return self

    def __next__(self):
        """
        iterator
        :return:
        """
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rv = Reverse('abc')

for char in rv:
    print(char)
