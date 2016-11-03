class fibonacci_sequence():
    class StopIteration(Exception):
        pass

    def __init__(self, numb):
        self.n = numb

    def __iter__(self):
        """Fibonacci numbers generator"""
        a, b = 1, 1
        for i in range(self.n):
            yield a
            a, b = b, a + b
        else:
            raise StopIteration(self.n+1)
