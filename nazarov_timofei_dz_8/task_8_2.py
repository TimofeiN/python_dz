
def logger(func):
    def wrapper(*args):
        result = func(*args)
        print(type(args))
        output = ''
        #output = ''f',' .join(map(str, args))
        for arg in args:
            if len(args) > 1:
                output += f'({arg}: {type(arg)}), '
            else:
                output += f'({arg}: {type(arg)}), '
        print(f'{func.__name__}{output[:-2]}')
        return result
    return wrapper


@logger
def calc_cubes(*args):
    res = []
    for num in args:
        res.append(num**3)
    return res


a = calc_cubes(5, 3, 2)
