class Push_swap:
    def __init__(self, a: list):
        self.a = a
        self.b = []

    def sa(self):
        if len(self.a) >= 2:
            self.a[0], self.a[1] = self.a[1], self.a[0]

    def sb(self):
        if len(self.b) >= 2:
            self.b[0], self.b[1] = self.b[1], self.b[0]

    def ss(self):
        self.sa()
        self.sb()

    def pa(self):
        if len(self.b):
            self.a.insert(0, self.b[0])
            self.b.pop(0)

    def pb(self):
        if len(self.a):
            self.b.insert(0, self.a[0])
            self.a.pop(0)

    def ra(self):
        if len(self.a) >= 2:
            self.a = self.a[1:] + [self.a[0]]

    def rb(self):
        if len(self.b) >= 2:
            self.b = self.b[1:] + [self.b[0]]

    def rr(self):
        self.ra()
        self.rb()

    def rra(self):
        if len(self.a) >= 2:
            self.a = [self.a[-1]] + self.a[:-1]

    def rrb(self):
        if len(self.b) >= 2:
            self.b = [self.b[-1]] + self.b[:-1]

    def rrr(self):
        self.rra()
        self.rrb()