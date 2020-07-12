import sys
import cProfile

l = [x ** 2 for x in range(1000000)]

g = (x ** 2 for x in range(1000000))


def _sum():
    cProfile.run('sum([x ** 2 for x in range(1000000)])')
    print('Memory:', sys.getsizeof(l))


def gen_sum():
    cProfile.run('sum((x ** 2 for x in range(1000000)))')
    print('Memory:', sys.getsizeof(g))


if __name__ == '__main__':
    _sum()
    print('-'*50)
    gen_sum()
    print('-' * 50)
