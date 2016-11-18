def get_int(start_message, error_message, end_message):
    inpu = input(start_message + '\n')
    while 1:
        try:
            x = int(inpu)
            break
        except:
            inpu = input(error_message + '\n')
    print(end_message)
    return x
