import random

def elsofeladat():
    rnd = random.randint(1, 50)
    print("\tI/A:")
    print("\tA generált szám: ",rnd)
    print("\tI/B:")
    if rnd % 5 == 0 and rnd % 3 == 0:
        print("\tA szám öttel és hárommal is osztható!")
    elif rnd % 5 ==0 :
        print("\tA szám öttel osztható!")
    elif rnd % 3== 0:
        print("\tA szám hárommal  osztható!")
