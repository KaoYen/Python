# version 1: use flag to break for loop
def search_nested_bad(array, desired_value):
    coords = None
    for i, row in enumerate(array):
        for k, v in row.items():
            if v == desired_value:
                coords = (i, k, v)
                break
        if coords is not None:
            break
    if coords is None:
        raise ValueError(f'{desired_value} not found')

    print(f'value {desired_value} found at {coords}')
    return coords


# version 2
def _iterate_array(array):
    for i, row in enumerate(array):
        for k, v in row.items():
            yield i, k, v


def search_nested(array, desired_value):
    try:
        coords = next((i, k, v) for i, k, v in _iterate_array(array) if v == desired_value)
    except StopIteration:
        raise ValueError(f'{desired_value} not found')
    print(f'value {desired_value} found at {coords}')
    return coords


if __name__ == '__main__':
    array = [{f'key-{i}': i} for i in range(100)]
    print(array)

    # version 1
    # search_nested_bad(array=array, desired_value=10)

    # version 2
    search_nested(array=array, desired_value=10)
