def gen():
    while True:
        yield 1
        yield 2
        return 3


def main():
    value = yield gen()
    print('return value:', value)


if __name__ == '__main__':
    # g = gen()
    # print(next(g))
    # print(next(g))
    # try:
    #     print(next(g))
    # except StopIteration as e:
    #     print(e.value)

    # 使用yield from 取得產生器的回傳值
    m = main()
    print(next(m))
    print(next(m))
    print(next(m))


