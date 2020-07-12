def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


if __name__ == '__main__':
    # use for loop to iter generator
    # for i in infinite_sequence():
    #     print(i)

    # use next to get value from generator
    gen = infinite_sequence()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))



