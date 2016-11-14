def modify_list(l):
    i = 0
    while i < len(l):
        z = l.pop(i)
        if not z % 2:
            l.insert(i, z//2)
            i += 1
