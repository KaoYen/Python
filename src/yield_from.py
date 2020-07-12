"""yield from 最簡單的用法"""

# def chain(*iterables):
#     """
#     這是不成熟的做法
#     :param iterables:
#     :return:
#     """
#     for it in iterables:
#         for value in it:
#             yield value
#
#
# def new_chain(*iterables):
#     """
#     yield from 語法可以提供更好的功能並且避免嵌套迴圈，因為它可以直接從子產生器產生值。
#     請注意，這兩種產生器的行為是完全相同的!
#     # 這段程式簡化了一些語法，但節省一行 for 陳述式並不是什麼大的改善，不足以成為讓這種與演做這種改變的理由。
#     :param iterables:
#     :return:
#     """
#     for it in iterables:
#         yield from it
#
#
# if __name__ == '__main__':
#     print(list(chain('hello', ['world'], ('tuple', 'of', 'values.'))))
#     print(list(new_chain('hello', ['world'], ('tuple', 'of', 'values.'))))


"""捕捉子產生器回傳的值"""


# def seq(name, start, end):
#     print(f'{name} started at {start}')
#     yield from range(start, end)
#     print(f'{name} finished at {end}')
#     return end
#
#
# def main():
#     step1 = yield from seq('first', 0, 5)
#     step2 = yield from seq('second', step1, 10)
#     return step1 + step2
#
#
# if __name__ == '__main__':
#     m = main()
#     for _ in range(15):
#         print(next(m))


'''bonus'''
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total / count

    # 每一次return，都意味着当前协程结束。
    return total, count, average


# 委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))


# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)  # 预激协程
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0
    calc_average.send(None)  # 结束协程
    # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程


if __name__ == '__main__':
    main()
