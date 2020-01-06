#!/usr/bin/env python3
N = 10
su = 0
count = 0
print("please input 10 numbers:")
while count < N:
    number = float(input())
    su = su + number
    count = count + 1
average = su / N
print("N = {}, Sum = {}".format(N, su))
print("Average = {:.2f}".format(average))