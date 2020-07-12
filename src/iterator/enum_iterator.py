def python_enum():
    """
    首先介紹Python的內建函式 enumerate()
    當它收到第一個迭代物之後會回傳另一個可迭代物，裡面的元素是tuple，tuple的第一個元素是第二個元素的編號 (原始可迭代物內的元素編號) :

    """
    print(list(enumerate('abcdefg')))


if __name__ == '__main__':
    python_enum()
