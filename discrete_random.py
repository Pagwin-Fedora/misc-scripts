#!/usr/bin/python3
import math
def solve_problem():
    num = int(input("How many points in the distribution?     "))
    dictionary = {}
    for i in range(0,num):
        key = float(input("Value #"+str(i+1)+": "))
        value = float(input("Probability #"+str(i+1)+": "))
        dictionary[key] = value;
    average = 0
    for value in dictionary:
        average+=value*dictionary[value]
    print("\nAverage: "+str(average))
    variability = 0
    for value in dictionary:
        variability += math.pow(value-average,2)*dictionary[value]
    print("Variability: "+str(variability))
    print("Standard Deviation: "+str(math.sqrt(variability))+"\n" )
y_n = input('Do you want to solve this problem repeatedly(y/n)?  ')
if y_n == 'y':
    while True:
        solve_problem()
else:
    solve_problem()

