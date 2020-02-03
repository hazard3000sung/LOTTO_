try:
    import random as rand
except:
    pass

def lotto():
    lottery = []
    for i in range(0,6):
        lottery.append(rand.randint(1,46))
    return lottery

if __name__ == "__main__":
    integer = int(input("How much do you need?"))
    for i in range(1,integer+1):
        print(lotto())
