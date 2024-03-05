import random
import time
import sys
while(1):
    print("GAME:guess the number..")
    print()
    print("select any from the below options:")
    print()
    print("1.you guess the number \n2.let system guess the number\n3.exit")
    print("enter your choice:")
    op = int(input())
    if op == 0 or op > 3:
        print("incorrect option/option not present.. please select between 1 and 2")
    if op == 3:
        print(":-} see you soon ")
        sys.exit()
    if op == 1:
        print("choose the level:")
        print("1.simple\n2.medium\n3.hard")
        lev = int(input())
        if lev==1:
            print("guess the number between 1-10")
            num=random.randint(1,10)
            print("if feel like giving up enter '0' ")
            c=0
            while(1):
                gu=int(input())
                if gu==num:
                    print("hey! you won.you took ",c,"attempts")
                    sys.exit()
                elif gu<num and gu>0:
                    print("greater number then this")
                    c+=1
                elif gu>num and gu>0:
                    print("smaller number then this")
                    c+=1
                if gu==0:
                    print(":-} see you soon ")
                    sys.exit()
        if lev==2:
            print("guess the number between 1-50")
            num = random.randint(1, 50)
            print("if feel like giving up enter '0' ")
            c = 0
            while (1):
                gu = int(input())
                if gu == num:
                    print("hey! you won.you took ", c, "attempts")
                    sys.exit()
                elif gu < num and gu > 0:
                    print("greater number then this")
                    c += 1
                elif gu > num and gu > 0:
                    print("smaller number then this")
                    c += 1
                if gu == 0:
                    print(":-} see you soon ")
                    sys.exit()

        if lev==3:
            print("guess the number between 1-100")
            num = random.randint(1,100)
            print("if feel like giving up enter '0' ")
            c = 0
            print(num)
            while (1):
                gu = int(input())
                if gu == num:
                    print("hey! you won.you took ", c, "attempts")
                    sys.exit()
                elif gu < num and gu > 0:
                    print("greater number then this")
                    c += 1
                elif gu > num and gu > 0:
                    print("smaller number then this")
                    c += 1
                if gu == 0:
                    print(":-} see you soon ")
                    sys.exit()

    if op==2:
        print("enter the range")
        print("that is 1-?")
        rm=1
        ra=int(input())
        print("enter 'w' if system is right \n enter 'l' to indicate lower the number \n enter 'h' to higher the number")
        print("enter 'e' to exit:")
        time.sleep(2)
        while(1):
            num = random.randint(rm, ra)
            print("system choose:",end="")
            print(num)
            pl=input()
            if pl=='w' or pl=='W':
                print("that was great game .see you soon.")
                sys.exit()
            if pl=='h'or pl=='H':
                rm=num
            elif pl=='l'or pl=='L':
                ra=num
            if pl=='e'or pl=='E':
                print("ok see you soon")
                sys.exit()

