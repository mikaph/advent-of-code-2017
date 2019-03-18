class Spinlock:
    def __init__(self, spin_len):
        self.spin_len = spin_len
        self.buf = [0]
        self.pos = 0
        self.last = 0

    def __str__(self):
        return "buffer:" + str(self.buf) + " position:" + str(self.buf[self.pos])

    def spin(self):
        self.pos = (self.spin_len + self.pos) % len(self.buf)

    def insert(self):
        self.spin()
        self.last = self.last + 1
        self.pos = self.pos + 1
        self.buf.insert(self.pos,self.last)

    def get_next_value(self):
        return self.buf[self.pos+1]

    def get_value_at(self, index):
        return self.buf[index]


spinner = Spinlock(329)

for i in range(0,2017):
    spinner.insert()

print("answer1:" + str(spinner.get_next_value()))

#2

class FakeSpinlock:
    def __init__(self, spin_len):
        self.spin_len = spin_len
        self.buf_len = 1
        self.pos = 0
        self.last = 0
        self.after_zero = 0

    def spin(self):
        self.pos = (self.spin_len + self.pos) % self.buf_len

    def insert(self):
        self.spin()
        self.last = self.last + 1
        self.pos = self.pos + 1
        if self.pos == 1:
            self.after_zero = self.last
        self.buf_len = self.buf_len + 1

    def get_after_zero(self):
        return self.after_zero


fake_spinner = FakeSpinlock(329)

for i in range(0,50000000):
    fake_spinner.insert()
    if i % 1000000 == 0:
        print(str(i/50000000))

print("answer2: " + str(fake_spinner.get_after_zero()))