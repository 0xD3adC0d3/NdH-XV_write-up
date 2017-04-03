#!/usr/bin/python

import random
import os

random.seed(os.getpid())
ngames = 0

def generate_combination():
    numbers = ""
    for _ in range(10):
        rand_num = random.randint(0, 99)
        if rand_num < 10:
            numbers += "0"
        numbers += str(rand_num)
        if _ != 9:
            numbers += "-"
    return numbers

print "First winning combination  : " + generate_combination()
print "Second winning combination : " + generate_combination() 
