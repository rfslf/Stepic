def fib(n):
    # put your code here
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
