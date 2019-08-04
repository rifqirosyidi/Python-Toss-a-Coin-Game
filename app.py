# TOSS A COIN PYTHON
# Toss a coin about 1000 times and see the probabilities between head and tails

# Made By Rief
import random

toss_count = 0
toss_total = 1000

toss_res_head = 0
toss_res_tail = 0

while toss_count <= toss_total:
    tossed = random.randint(0, 1)
    if tossed == 0:
        toss_res_head += 1
    else:
        toss_res_tail += 1
    toss_count += 1


print("Toss Head Total : ", toss_res_head)
print("Toss Tail Total : ", toss_res_tail)
