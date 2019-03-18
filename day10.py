from functools import reduce

input10 = "227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144"

rope = list(range(0, 256))

input10_2 = list((input10.split(',')))
parsed_input = []

for i in input10_2:
    parsed_input.append(int(i))

class Cyclic_iterator:
    def __init__(self, list_size):
        self.list_size = list_size
        self.i = 0
    def increment(self, amount):
        for i in range(0,amount):
            if self.i == self.list_size - 1:
                self.i = 0
            else:
                self.i += 1
    def get_i(self):
        return self.i

    def set_i(self, i):
        self.i = i


i_rope = Cyclic_iterator(len(rope))

sublist = []
skip_size = 0


for i in parsed_input:
    sublist_start = i_rope.get_i()
    for j in range(0, i):
        sublist.append(rope[i_rope.get_i()])
        i_rope.increment(1)

    sublist.reverse()
    i_rope.set_i(sublist_start)

    for item in sublist:
        rope[i_rope.get_i()] = item
        i_rope.increment(1)

    sublist = []

    i_rope.increment(skip_size)
    skip_size += 1


print("answer1:" + str(rope[0]*rope[1]))

# part2

input10_3 = []
parsed_input2 = []

for i in input10:
    input10_3.append(str(ord(i)))

for i in input10_3:
    parsed_input2.append(int(i))

magic_numbers = [17, 31, 73, 47, 23]

parsed_input2.extend(magic_numbers)

sublist = []
skip_size = 0
rope = list(range(0, 256))
i_rope = Cyclic_iterator(len(rope))

for j in range(0, 64):
    for i in parsed_input2:
        sublist_start = i_rope.get_i()
        for k in range(0, i):
            sublist.append(rope[i_rope.get_i()])
            i_rope.increment(1)

        sublist.reverse()
        i_rope.set_i(sublist_start)

        for item in sublist:
            rope[i_rope.get_i()] = item
            i_rope.increment(1)

        sublist = []

        i_rope.increment(skip_size)
        skip_size += 1


hashi = []

for i in range(0, 16):
    hashi.append(reduce((lambda x, y: x ^ y), rope[i*16:(i+1)*16]))


hex_hashi = []
for i in hashi:
    hex_hashi.append(hex(i))

print("answer2:" + str(reduce((lambda x, y: x + y[2:]), hex_hashi, "")))