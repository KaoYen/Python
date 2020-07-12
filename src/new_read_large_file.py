from itertools import tee
from statistics import median


def produce_values(how_many):
    for i in range(1, how_many + 1):
        print("producing purchase %i", i)
        yield i


def process_purchases(purchases):
    min_, max_, avg = tee(purchases, 3)
    return min(min_), max(max_), median(avg)


def _process_purchases(purchases):
    return min(purchases), max(purchases), median(purchases)


def main():
    data = produce_values(7)
    print(type(data), data)
    obtained = _process_purchases(data)
    print("Obtained: %s", obtained)
    assert obtained == (1, 7, 4)

if __name__ == "__main__":
    main()
