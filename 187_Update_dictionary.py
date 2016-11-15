def update_dictionary(d, key, value):
    ls = []
    if key in d:
        ls.extend(d[key])
        ls.append(value)
        d[key] = ls
    else:
        key = int(2*key)
        if key not in d:
            ls.append(value)
            d[key] = ls
        else:
            ls.extend(d[key])
            ls.append(value)
            d[key] = ls

# не добавляйте кода вне функции