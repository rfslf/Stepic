class Buffer:
    def __init__(self):
        self.listik = []

    def add(self, *a):
        self.a = a
        for i in self.a:
            self.listik.append(i)
            if len(self.listik) == 5:
                print(sum(self.listik[:5]))
                self.listik = self.listik[5:]

    def get_current_part(self):
        return self.listik
