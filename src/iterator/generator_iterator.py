def sequence(start=0):
    while True:
        yield start
        start += 1


if __name__ == '__main__':
    #  generator本身就是迭代器
    seq = sequence(10)
    for _ in range(10):
        print(next(seq))

    #  同上例用法，產生的結果完全相同
    print(list(zip(sequence(), 'abcdefg')))
