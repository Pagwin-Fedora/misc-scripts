import random
import matplotlib.pyplot as plt
#a script I used to get some random statistics data about how long it would take a netherite hoe with unbreaking 3 to break on average and how that varied on average it's pretty pointless
def average(l):
    return sum(l)/len(l)
def averages(l):
    return [average(l[0:i+1]) for i in range(len(l))]
def gen(val=2030,percent=1/4):
    n = 0
    while val>0:
        val -= 1//(random.randrange(4)+1)
        n+=1
    return n

def genAmount(amount):
    return [gen() for i in range(amount)]

l = averages(genAmount(int(input("How many samplings do you want?"))))
print(f"average:{average(l)}\nmin:{min(l)}\nmax:{max(l)}")
plt.plot(list(range(len(l))),l)
plt.show()
