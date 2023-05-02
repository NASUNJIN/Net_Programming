def str_dict(s):
    result = {}
    parser = s.split('&')
    for i in parser:
        key, value = i.split('=')
        result[key] = value
    return result

str = 'led=on&motor=off&switch=off'
print(str_dict(str))