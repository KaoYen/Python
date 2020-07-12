class CustomException(Exception):
    """An exception of the domain model."""


def seq(name, start, end):
    value = start
    print(f'{name} start at {start}')
    while value < end:
        try:
            received = yield value
            print(f'{name} received {received}')
            value += 1
        except CustomException as e:
            print(f'{name} is handling {e}')
            received = yield 'ok'
    return end

def main():
    step1 = yield from seq('first', 0, 5)
    step2 = yield from seq('second', step1, 10)
    return step1 + step2



if __name__ == '__main__':

    g = main()
    # for _ in range(101):
    #     print(next(g))
    print(next(g))
    print(g.send(123))
    print(g.send(123))
    print(g.throw(CustomException('test error')))
