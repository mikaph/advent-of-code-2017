import random
from  itertools import count
input_file = open('input13', 'r').read().splitlines()

parsed_input = [list(x.split(':')) for x in input_file]

packet_position = 0
severity = 0
firewall = []

class Scanner:
    def __init__(self, range):
        self.range = range
        self.position = 0
        self.reverse = False
    def move(self):
        if self.reverse:
            self.position -= 1
            if self.position == 0:
                self.reverse = False
        else:
            self.position += 1
            if self.position == self.range -1:
                self.reverse = True

    def is_detecting(self):
        if self.position == 0:
            return True
        else:
            return False

    def get_range(self):
        return self.range

    def __str__(self):
        return_str = "pos:" + str(self.position) + " range:" + str(self.range)
        return return_str

firewall_size = max([int(x[0]) for x in parsed_input]) +1

for i in range(0,firewall_size):
    firewall.append(None)

for item in parsed_input:
    firewall[int(item[0])] = Scanner(int(item[1]))

while packet_position < firewall_size:

    if firewall[packet_position] == None:
        pass
    elif firewall[packet_position].is_detecting():
        severity += packet_position*firewall[packet_position].get_range()

    for item in firewall:
        if item != None:
            item.move()

    packet_position += 1

print("answer1:" +  str(severity))

#part 2

for delay in range(0,30):
    packet_position = 0
    severity = 0
    firewall = []
    time_delayed = 0
    packet_moving = False
    detected = False

    for i in range(0, firewall_size):
        firewall.append(None)

    for item in parsed_input:
        firewall[int(item[0])] = Scanner(int(item[1]))

    while packet_position < firewall_size:
        if time_delayed == delay:
            packet_moving = True

        if firewall[packet_position] == None:
            pass
        elif firewall[packet_position].is_detecting() and packet_moving:
            detected = True
            print("detected at: " + str(packet_position) + " delay:" + str(delay))
            severity += packet_position * firewall[packet_position].get_range()

        for item in firewall:
            if item != None:
                item.move()

        if packet_moving:
            packet_position += 1
        else:
            time_delayed += 1

    if detected == False:
        print("answer2:" + str(delay))
        continue




BIGGEST_NUMBER = 10000000
numbers_to_try = set(range(0,BIGGEST_NUMBER))

for item in parsed_input:
    firewall_pos = int(item[0])
    firewall_rng = int(item[1])
    firewall_freq = firewall_rng*2 - 2
    firewall_fail_delay_start = 0
    for i in count():
        if i == firewall_pos:
            break
        elif firewall_fail_delay_start == 0:
            firewall_fail_delay_start = firewall_freq - 1
        else:
            firewall_fail_delay_start -= 1
    print("fw: " + str(item))
    bad_nums = set(map((lambda x: x*firewall_freq + firewall_fail_delay_start), set(range(0, BIGGEST_NUMBER))))
    numbers_to_try.difference_update(bad_nums)

print(min(numbers_to_try))