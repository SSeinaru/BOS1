from time import sleep

def plot1():
    print("This story begins with a man named Clover Taurus")
    sleep(1)
    print("Hes not the biggest known man, but hes still quite popular")
    sleep(1)
    print("Ofcourse this isn't just some random ass boring story")
    sleep(1)
    print("because you are the one who makes the choices")
    sleep(1)
    print("some background info about Clover")
    sleep(1)
    print("Hes a B-rank Adventurer, He just kinda does this for the funny xd lmao")
    sleep(1)
    print("Now that that is said lets begin")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    print("                                     ")
    plot2

def plot2():
    print("You wake up on your tatami mat")
    sleep(1)
    print("you get out of bed and get dressed")
    sleep(1)
    print("You look at your room and then you look at the others rooms")
    sleep(1)
    print("You finally realise how dirty your house")
    sleep(1)
    print("You decide to maybe do it later, because after all")
    sleep(1)
    print("because breakfast is more important")
    sleep(1)
    print("you look into your look around if there is anything to eat")
    sleep(1)
    print("you find some gold coins and some sushi rice and some fish")
    sleep(1)
    print("So you have 2 options, you use the coins to get some fresh bread")
    sleep(1)
    print("Or you make some sushi")
    sleep(1)
    print("So what do you decide eat? A. Buy bread B. Make sushi")
    food = input().lower()

    if food == "a":
        plot3
    
    elif food == "b":
        plot4

def plot3():
    print("So you decide to go buy some bread")
    sleep(1)
    print("You go to the bakery")
    sleep(1)
    print("Inside the bakery you meet the baker and see that he has 2 loafs of bread left")
    sleep(1)
    print("you ask him if he has any bread left for sale")
    sleep(1)
    print("He answers that he has a singular loaf left for sale")
    sleep(1)
    print("All the others have been sold and the other one is on reservation")
    sleep(1)
    print("thank fully you walk back with the bread piece")
    sleep(1)
    print("when you arrive home you cut the bread and make some sandviches")
    sleep(1)
    print("you thought that you might need some later so you make some extra's")
    sleep(1)
    plot5

def plot4():
    print("")

def plot5():
    print("After that you get ready to head out")

def plot6():
    print("So right now you have 5 choices")
    sleep(0.3)
    print("A. You kill those slimes")
    sleep(0.5)
    print("B. You help rebuild the city")
    sleep(0.5)
    print("C. You search for the quest items")
    sleep(0.5)
    print("D. You walk around doing literally nothing (the most boring option)")
    sleep(0.5)
    print("E. You clean your home")
    sleep(1)
    print("So what will it be partner")
    adventure = input().upper()
    if adventure == "A":
        plot7
    elif adventure == "B":
        plot15
    elif adventure == "C":
        plot30
    elif adventure == "D":
        plot48
    elif adventure == "E":
        plot50
    else:
        plot6

def plot7():
    print("So the slime hunt huh")
    print("Wow thats boring as shit but hey")
    print("What can I say im just a narrator")
    print("So you search for a slime field")
    print("You thought when there")
    print("'This is gonna be so damn easy'")
    print("Oh brother what wrong you are")
    print("")
def plot8():
    print("")

def plot9():
    print("")

def plot10():
    print("")

def plot11():
    print("")

def plot12():
    print("So once again you have a choice.")
    print("This time you can sneak away or you start sprinting full speed")
    print("Obviously you can go quietly but slow")
    print("Or you can go loud and fast")
    print("Its time to decide")
    print("A. Sprinting, Loud and Dumb")
    print("B. Sneak, Silent but Slow")
    choice = input().lower()

    if choice == "a":
        plot13
    elif choice == "b":
        plot14

def plot13():
    print("")

def plot14():
    print("")



def plot15():
    print("So you took the item quest")
    print("You read what you needed to get")
    print("You need to get the items")
    print("A dragons tooth")
    print("A Demonic slime core")
    print("A Full mana potion")
    print("")

def plot16():
    print("")

def plot17():
    print("")

def plot18():
    print("")
    
def plot19():
    print("")

def plot21(): 
    print("")

def plot22(): 
    print("")

def plot23(): 
    print("")

def plot24(): 
    print("")

def plot25(): 
    print("")

def plot26(): 
    print("")

def plot27(): 
    print("")

def plot28(): 
    print("")

def plot29(): 
    print("")



def plot30(): 
    print("")

def plot31(): 
    print("")

def plot32(): 
    print("")

def plot33(): 
    print("")

def plot34(): 
    print("")

def plot35(): 
    print("")

def plot36(): 
    print("")

def plot37(): 
    print("")

def plot38(): 
    print("")

def plot39(): 
    print("")

def plot40(): 
    print("")

def plot41(): 
    print("")

def plot42(): 
    print("")

def plot43(): 
    print("")

def plot44(): 
    print("")

def plot45(): 
    print("")

def plot46(): 
    print("")

def plot47(): 
    print("")



def plot48(): 
    print("")

def plot49(): 
    print("")



def plot50(): 
    print("")

def plot51(): 
    print("")

def plot52(): 
    print("")

def plot53(): 
    print("")

def plot54(): 
    print("")

def plot55(): 
    print("")

def plot56(): 
    print("")

def plot57(): 
    print("")

def plot58(): 
    print("")

def plot59(): 
    print("")

def plot60(): 
    print("")

def plot61(): 
    print("")

def plot62(): 
    print("")

def plot63(): 
    print("")

def plot64(): 
    print("")

def plot65(): 
    print("")

def plot66(): 
    print("")



def eind1(): 
    print("")

def eind2(): 
    print("")

def eind3(): 
    print("")

def eind4(): 
    print("")

def eind5(): 
    print("")

def intro():
    print("Do you wish to start?")
    answer = input().lower()
    if answer == "yes":
        plot1
    elif answer == "no":
        quit
    else:
        print("Mate thats not an acceptable answer")

intro()