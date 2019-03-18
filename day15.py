gen_a = 618
gen_b = 814

#gen_a = 65
#gen_b = 8921

factor_a = 16807
factor_b = 48271

den = 2147483647

counter = 0

for i in range(0,40000000):
    gen_a = gen_a * factor_a % den
    gen_b = gen_b * factor_b % den
    if not (gen_a ^ gen_b) & 0b1111111111111111:
        counter += 1

print("answer1:" + str(counter))

#2
counter2 = 0
gen_a = 618
gen_b = 814

for i in range(0,5000000):
    while True:
        gen_a = gen_a * factor_a % den
        if gen_a % 4 == 0:
            break

    while True:
        gen_b = gen_b * factor_b % den
        if gen_b % 8 == 0:
            break

    if not (gen_a ^ gen_b) & 0b1111111111111111:
        counter2 += 1

print("answer2: " + str(counter2))
