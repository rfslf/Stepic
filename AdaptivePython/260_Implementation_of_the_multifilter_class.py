class multifilter():
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            return True
        else:
            return False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1:
            return True
        else:
            return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.f = funcs
        self.a = iterable
        self.j = judge
        self.list = []

    def __iter__(self):
        for i in self.a:
            positive = 0
            negative = 0
            for j in self.f:
                if j(i):
                    positive += 1
                else:
                    negative += 1
            if self.j(positive, negative):
                self.list.append(i)
                yield i
