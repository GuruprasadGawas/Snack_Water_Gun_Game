import random
def swg(comp,mine):
    if (comp == mine):
        return None
    elif (comp == 's' and mine == 'g'):
        return True
    elif (comp == 'w' and mine == 's'):
        return True
    elif (comp == 'g' and mine == 'w'):
        return True
    else:
        return False


mine = input("Choose either s, w or g : ")
choice = ('s','w','g')
comp = random.randint(0,2)
comp = choice[comp]
win = swg(comp,mine)
print(F"You chose {mine} and Computer chose {comp}")
if win:
    print("YOU WON")
elif win is None:
    print("MATCH DRAWN")
else :
    print("YOU LOSS")

