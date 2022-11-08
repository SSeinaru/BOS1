from time import sleep

def plot1():
    print("This story begins with a man named Clover Taurus")
    sleep(2)
    print("Hes not the biggest known man, but hes still quite popular")
    sleep(2)
    print("Ofcourse this isn't just some random ass boring story")
    sleep(2)
    print("because you are the one who makes the choices")
    sleep(2)
    print("some background info about Clover")
    sleep(2)
    print("Hes a B-rank Adventurer, He just kinda does this for the funny xd lmao")
    sleep(2)
    print("Now that that is said lets begin")
    sleep(4)
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
    plot2()

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
        plot3()
    
    elif food == "b":
        plot4()

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
    plot5()

def plot4():
    print("So you went to make some sushi")
    sleep(1)
    print("cooked the rice and prepared the nori sheets")
    sleep(1)
    print("after that you grabbed your fish and started to fillet it")
    sleep(1)
    print("you cut it into even strips of fish for the sushi")
    print(1)
    print("after the fish you grab a eggplant and some seeds")
    print(1)
    print("you cut the eggplant into strips once again")
    print(1)
    print("after that you start to put it together")
    sleep(1)
    print("firstly you put down the nori sheets while putting rice on top")
    sleep(1)
    print("after that you put the fish and the eggplant on it and some seeds with it")
    sleep(1)
    print("then you start to roll it up")
    sleep(1)
    print("after rolling it up you cut it into even piece and start to eat")
    plot5()

def plot5():
    print("After that you get ready to head out")
    sleep(1)
    print("you grab your boots and dress correctly to go")
    sleep(1)
    print("after dressing you grab your weapons")
    sleep(1)
    print("you grab your short blade, throwing knifes and your glock-19 silenced")
    sleep(1)
    print("after grabbing it all, you put on your shoes and leave your house")
    sleep(1)
    print("after leaving the house you decide to walk to the center to see what there is to do")
    sleep(1)
    print("while you were walking you saw parts of the city still rebuilding")
    sleep(1)
    print("and you think you might do that")
    sleep(1)
    print("When you reach the board you see that you are capable of doing 2 quests")
    sleep(1)
    print("a kill quest and a search quest")
    plot6()

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
        plot7()
    elif adventure == "B":
        plot15()
    elif adventure == "C":
        plot30()
    elif adventure == "D":
        plot48()
    elif adventure == "E":
        plot50()
    else:
        plot6()

def plot7():
    print("So the slime hunt huh")
    sleep(1)
    print("Wow thats boring as shit but hey")
    sleep(1)
    print("What can I say im just a narrator")
    sleep(1)
    print("So you search for a slime field")
    sleep(1)
    print("You thought when there")
    sleep(1)
    print("'This is gonna be so damn easy'")
    sleep(1)    
    print("Oh brother what wrong you are")
    sleep(1)
    print("You start stabbing slimes")
    sleep(1)
    print("Only to realise that nothing is happening")
    sleep(1)
    print("You think 'Well fuck'")    
    sleep(1)
    print("You start thinking on how to defeat these shits")
    sleep(1)
    print("After multiple attemps you finally find out you have to pop them like a balloon")
    sleep(1)
    print("but is has to be at a very specific place, between the eyes")
    sleep(1)
    plot8()

def plot8():
    print("After a while you notice that there aren't that slimes left in the region")
    print("So you decide to move to another place to find more")
    sleep(1)
    print("eventually you do find some more in the volcano region")
    sleep(1)
    print("you continue popping slimes while going further into the volcano")
    sleep(1)
    print("after you stabbed the last slime you needed that there was a dragon in the middle of the volcano")
    sleep(1)
    print("you realised that the dragon was obviously stronger than you in every way possible")
    sleep(1)
    print("so you decide to start running behind a wall to plan on what to do")
    sleep(1)
    question2()


def question2():
    print("you realised you have 2 options")
    sleep(1)
    print("Either you start running")
    print("Or you start fighting")
    print("so what is your choice")
    print("A. Fight")
    print("B. Run")
    choice2 = input().lower()
    if choice2 == "a":
        plot9()
    elif choice2 == "b":
        plot11()
    else:
        question2()

def plot9():
    print("So you choose to fight")
    sleep(1)
    print("That is the worst decision you have done so far")
    sleep(1)
    print("but anyways your unsure on how to tackle this enemy")
    sleep(1)
    print("you think for a moment on what to do")
    sleep(1)
    print("You realise you have your glock with you")
    sleep(1)
    print("you attempt to shoot the dragon")
    sleep(1)
    print("you hit the shot but it didn't even pierce the skin")
    sleep(1)
    print("you decide that you have to fight it with your sword")
    sleep(1)
    plot10()

def plot10():
    print("You start to sneak up to the dragon with your daggers out")
    sleep(1)
    print("You stab the dragon in its neck")
    sleep(1)
    print("The dragon screams in agony and starts attempting to get you off")
    sleep(1)
    print("You continue to stab it in the neck")
    sleep(1)
    print("but eventually the dragon does get you off and stands up completely overshadowing you")
    sleep(1)
    print("you now realise what the difference in strength between eachother is big")
    sleep(1)
    print("Too big for you to handle on your own")
    sleep(1)
    print("You fall to your knees and accept the sweet brace of death as the dragon charges something")
    sleep(1)
    print("you no longer care and as the dragon fires your entire body just decitigrates into ash")
    sleep(1)
    eind1()

def plot11():
    print("You chose to run good choice")
    sleep(1)
    print("then you start questioning on how to get away from this alive")
    sleep(1)
    print("you know you can't just straight up speedrun your way from here")
    sleep(1)
    print("You sit in the ground on but still ready to run if you have to")
    sleep(1)
    print("You start to think of a logical option")
    sleep(1)
    print("its go hard or go slow")
    sleep(1)
    plot12()
    
def plot12():
    print("So once again you have a choice.")
    sleep(1)
    print("This time you can sneak away or you start sprinting full speed")
    sleep(1)
    print("Obviously you can go quietly but slow")
    sleep(1)
    print("Or you can go loud and fast")
    sleep(1)
    print("Its time to decide")
    sleep(1)
    print("A. Sprinting, Loud and Dumb")
    sleep(1)
    print("B. Sneak, Silent but Slow")
    choice = input().lower()

    if choice == "a":
        plot13()
    elif choice == "b":
        plot14()

def plot13():
    print("So you are gonna do it loud and dumb")
    sleep(1)
    print("I had faith in you that you were somewhat smart")
    sleep(1)
    print("but I guess I was wrong")
    sleep(1)
    print("Well you start sprinting away at full speed")
    sleep(1)
    print("but your a clumsy idiot who ran straight into a wall that knocks more walls down")
    sleep(1)
    print("Alerting the dragon you start running even harder")
    sleep(1)
    print("the dragon starts chasing you, hes catching up quickly")
    sleep(1)
    print("You knowing damn well that he's faster than you make a sharp turn")
    sleep(1)
    print("you catch the dragon confused for a second the dragon passes but quickly turning around")
    sleep(1)
    print("you reaching a dead end decides to finally take the dragon head on")
    sleep(1)
    print("You grab your trowing knives and glock and go for his eyes")
    sleep(1)
    print("you hit him and make him go blind but you realise slightly too late that that was making your own death")
    sleep(1)
    print("the dragon falls and crushes your puny body. killing you instantly")
    sleep(1)
    eind1()

def plot14():
    print("Silent but slow, Good you're not a idiot")
    sleep(1)
    print("You start to sneak away while doing so you find a random egg on the floor")
    sleep(1)
    print("you not knowing what it is just grabs it and leaves")
    sleep(1)
    print("you accidentally step on a branch and it shatters")
    sleep(1)
    print("You look back at the dragon and tense up")
    sleep(1)
    print("the dragon slightly woke up, but thankfully enough falls asleep again")
    sleep(1)
    print("you savely sneak away")
    sleep(1)
    print("You cash in the quest with the slime cores you receive a rtx 4090 with a approximate worth of a average elon musk")
    sleep(1)
    print("You return home realising you did 0 cleaning this entire time")
    sleep(1)
    print("You say fuck it thats for another day")
    sleep(1)
    print("You finally decide to head to bed, its been enough for the day")
    sleep(1)
    eind2()

def plot15():
    print("You chose to help rebuild, wise choice")
    sleep(1)
    print("You start to walk around")
    sleep(1)
    print("While walking around you talk to a few people of what still has to happen")
    sleep(1)
    print("You ask them what are the most important things that have to be done")
    sleep(1)
    print("They all respond with the same 2 answers")
    sleep(1)
    print("You also thought of renovating your own home")
    sleep(1)
    print("You sit down somewhere to think")
    sleep(1)
    print("You have 3 choices in total")
    sleep(1)
    print("2 are good for the community and 1 is good for yourself")
    sleep(1)

def plot16():
    print("So will it be?")
    print("A. The Town Hall")
    print("B. Roads leading in and out the city")
    print("C. Renovate your own house to look somewhat livable")
    answer3 = input().lower()
    if answer3 == "a":
        plot17()
    elif answer3 == "b":
        plot21()
    elif answer3 == "c":
        plot25()
    else:
        plot16()

def plot17():
    print("So you decide on rebuilding the town hall since that obviously is the most important")
    sleep(1)
    print("You start walking to the town hall to see how broken it is")
    sleep(1)
    print("You see that the town hall is on supports but need the entire roof rebuilt")
    sleep(1)
    print("You know what to do now")
    sleep(1)
    print("You walk to the person in control there on what you can do to help")
    sleep(1)
    print("They answer with 2 things")
    sleep(1)
    print("The roof or the supports for the roof")
    sleep(1)
    print("What do you think?")
    sleep(1)
    plot18()

def plot18():
    print("Will you help with the roof supports or with the actual roof")
    sleep(1)
    print("You should think about it carefully")
    sleep(1)
    print("Your life might depend on it")
    sleep(1)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("     :)      ")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("A. Roof")
    print("B. Roof support")
    a = input().lower()
    if a == "a":
        plot19()
    elif a == "b":
        plot20()

def plot19():
    print("So the roof huh")
    sleep(1)
    print("You climb up to the roof to help continue building it")
    sleep(1)
    print("A lot of heavy lifting if im honest")
    sleep(1)
    print("After that long and tough day its finally done")
    sleep(1)
    print("You are allowed to inside")
    sleep(1)
    print("The president is giving a speach to the ones who helped building")
    sleep(1)
    print("During the speech you are looking around when suddenly")
    sleep(1)
    print("You start to see cracks in the Support pillars creep down the pillars")
    sleep(1)
    print("You scream for everyone to get out of there")
    sleep(1)
    print("Everyone starts to look around sees the cracks")
    sleep(1)
    print("Panic breaks out while everyone tries to leave")
    sleep(1)
    print("you who got sent to the back gives up and goes to on a chair")
    sleep(1)
    print("waiting for your inevitable death")
    eind1()

def plot20():
    print("So the pillars good choice")
    sleep(1)
    print("Stability and strength of the pillars is upmost importance ;)")
    sleep(1)
    print("Thats why you took the lead in the pillars")
    sleep(1)
    print("Time to work on it mate")
    sleep(1)
    print("     9 hours later")
    sleep(1)
    print("The pillars and roof are finally finished")
    sleep(1)
    print("and your now in the hall itself")
    sleep(1)
    print("You look around and admire the work all of you put into this")
    sleep(1)
    print("You are proud of yourself")
    sleep(1)
    print("The president is giving a speech of how proud of he is of us all")
    sleep(1)
    print("And that he'd like to reward us with anything that we desire to")
    sleep(1)
    print("you think about what you want for a second before knowing exactly what you want")
    sleep(1)
    print("You ask for someone to help clean in the house while your away")
    sleep(1)
    print("He responds with that he can fix that for you, you smile and you go home")
    sleep(1)
    print("Tired after such a long day")
    sleep(1)
    print("You get home and decide to sleep")
    sleep(1)
    print("you are proud of yourself and fall asleep with a smile")
    eind2()


def plot21(): 
    print("You decide to help with the roads")
    sleep(1)
    print("You walk to the built on roads and ask around who's in charge")
    sleep(1)
    print("Eventually you find the man in charge and ask if there is anything you can do")
    sleep(1)
    print("He answers with 'Of course you can help here in the city or outside the gates'")
    sleep(1)
    print("'But if you go out the gates be aware of anything around you'")
    sleep(1)
    print("'Anything outside the walls doesn't know the word mercy'")
    sleep(1)
    print("You start to think about it")
    sleep(1)
    plot22()

def plot22(): 
    print("So you once again for the so manieth time have a choice to make")
    sleep(1)
    print("What is it this time")
    sleep(1)
    print("A. Inside")
    print("B. Outside")
    B = input().lower()
    if B == "a":
        plot23()
    elif B == "b":
        plot24()

def plot23(): 
    print("So the save option huh")
    print("good choice? idk anymore tbh its all just some text displayed on a screen")
    print("So you choose to work on the inside")
    print("You look around to see where you can start")
    print("You realise that you are no where near somewhere you can start")
    print("Something doesn't feel right, how did you end up here")
    print("You start following a road not knowing where you are")
    print("After a while you look up again and suddenly find out you are in the middle of the forrest")
    print("You don't even remember walking here")
    print("Suddenly you hear hissing and bushes shake")
    print("You start to run")
    print("IT catches up and cuts your tendans in your leg")
    print("You fall face first")
    print("You accept the brace of death for what is about to happen to you")
    print("...")
    eind1()

def plot24(): 
    print("So you are working outside huh")
    print("Thats a choice i guess")
    print("Anyways you start to walk out the gates and to the nearest road thats under construction")
    print("You see others already working hard")
    print("You start to help around to anyone who needs it")
    print("A few hours later")
    print("It was time to stop for most of the road has been completed")
    print("Everyone starts to walk back to the gate and gets let in")
    print("You get the free food they offered for the workers")
    print("After the food you and some others decide to head to a tavern")
    print("After that you head back home and straight to bed when you reached home")
    eind2()

def plot25(): 
    print("You head back home to work on your own home for once")
    print("You realise when you head home how bad your own house is")
    print("You look at your own decrepped and broken down shack of your house")
    print("You enter and look around")
    print("The more you look around the more you realise how broken it is")
    print("You say fuck it and start to sort out all your stuff into garbage and not so garbage")
    print("At the end you have 2 massive piles of stuff you want to keep and stuff to throw away")
    print("You decide to put the stuff you want into boxes in a store place")
    print("And you sell the rest somewhere to help with paying for the house")
    print("Later after everything was sold you had enough to do 1 of 3 things")
    plot26()

def plot26(): 
    print("You were thinking of 3 styles for your house")
    print("A. You destroy it and rebuild it with a completely new style")
    print("B. You repair the house and strengthen it with slight redesigns")
    print("C. You buy a new house")
    c = input().lower()
    if c == "a":
        plot27()
    elif c == "b":
        plot28()
    elif c == "c":
        plot29()
    else:
        plot26()


def plot27(): 
    print("Once again you decide to destroy and rebuild the house")
    print("Not like you have done this before so here we go")
    print("You start thinking for the style of the house and decide to go with traditional japanese")
    print("You find the builders guild and ask some for help")
    print("You successfully hire the builders and go to work")
    print("To destroy it you chopped it down, it was made from wood anyways")
    print("Free wood for the winter")
    print("You and the builders discuss on what the best plan of action is for building the house")
    print("All of you decide to just do it the traditional way")
    print("1 week later")
    print("The house is finally finished and your so goddamn proud of it with the builders")
    print("You pay all of them the last bit they earned and you invite them to the tavern")
    print("After that you decide to go back home and sleep")
    eind6()

def plot28(): 
    print("So you planned to stay with what you have and build uppon it")
    print("You call some builders to help")
    print("After you wait for the builders to arrive")
    print("When evetually the builders arrived all of you went to work and started to plan it out")
    print("All of you decided to do it the best way possible")
    print("You all decide to strengthen the house at all possible points you can")
    print("It will take a while to actually make the house look good once again")
    print("A paintjob and a a lot of grinding and stengthening everything")
    print("2 weeks later")
    print("You are all finally done with the task of hell")
    print("All of you look at the result and are proud as absolute hell")
    print("You all sit there with the thought of we did that shit")
    print("You treat all of them to a bear and become good pals")
    print("after that you head inside and went to bed")
    eind6()

def plot29(): 
    print("You finally scrap that old hole of yours")
    print("To straight up decide to live somewhere else")
    print("I mean you have the money for it so why not yk its always better than that scrap of yours")
    print("You ask for help from family on how to get a house")
    print("They help and eventually you find a house")
    print("After you buy it you get help with moving in")
    print("Everyone there helps")
    print("At the end of it all you are left with a gorgeous house")
    print("you thank everyone with a piece of cake and something drink")
    print("After that everyone starts to leave and you are finally alone")
    print("The first thing you think of is ways to use the space to its full use")
    print("But thats for another day")
    print("It has been a long day and so you head to bed")
    print("Smiling of your new home")
    print("As time goes by you starts to close your eyes and once more fall asleep")
    eind6()

items = ["A dragons tooth", "A demonic slime core", "A full restore mana potion", "A high mana crystal"]
def plot30():    
    print("So you took the item quest")
    print("You read what you needed to get")
    print("You need to get the items")
    print(items[0])
    print(items[1])
    print(items[2])
    print(items[3])
    print("You basically know how to get most of them")
    print("but your missing on where to get them")
    print("but right now the most important part is the act of choosing what goes first")

def plot31(): 
    print("So for which one are you going first")
    print("You have to get them all anyways so why does it matter")
    print("So lets go")

def question3():
    print("A.", items[0])
    print("B.", items[1])
    print("C.", items[2])
    print("D.", items[3])
    D = input().lower()
    if D == "a":
        plot32()
        list.remove[0]
    elif D == "b":
        plot38()
        list.remove[1]
    elif D == "c":
        plot41()
        list.remove[2]
    elif D == "d":
        plot42()
        list.remove[3]
    else:
        question3()        

def plot32(): 
    print("So your starting with the dragons tooth")
    print("Not the hardest to find, just the most annoying")
    print("You start to look at places where you could get one")
    print("You realise that they aren't the most expensive things to buy")
    print("but you also find out that they aren't hard to get either")
    print("So you start to think oin how to do it")
    print("So now you are once again stuck with 2 options")
    print("you can either")
    print("A. Find a Dragon or tooth itself")
    print("B. Buy one for a decent price")
    print("So what will it be partner")
    E = input().lower()
    if E == "a":
        plot33()
    elif E == "b":
        plot37()

def plot33(): 
    print("So finding it yourself won't be hard")
    print("But getting the actual tooth will be the problem")
    print("You remember you heard someone around the board say that heard people said that there was a dragon in the volcano")
    print("So your go back home to prepare on facing the dragon")
    print("When you got home you searched around for some better equipment")
    print("Eventually you find a sniper rifle and a katana")
    print("That already helps a lot you thought")
    print("You start to head to the volcano")
    print("When you get there you already see the dragon")
    print("He's laying in the middle of an open area surrounded by old infrastructure")
    print("You start to think how you are gonna do this")
    print("You come up with 3 strageties")
    print("You go for his eyes first, the tooth or the legs")
    print("So what are you going with?")
    print("A. Get the eyes")
    print("B. Go straight for the tooth")
    print("C. Go for the legs to immobilize him")
    F = input().lower()
    if F == "a":
        plot34()
    elif F == "b":
        plot35()
    elif F == "c":
        plot36()

newlist = [] 
def plot34():
    
    print("You grab the sniper and aim for his right eye")
    print("You shoot and hit it destroying it")
    print("The dragon shoots up in anger and looks at you with rage")
    print("You know this is gonna be difficult but this just got much worse")
    print("You aim again for his left eye now")
    print("You shoot but miss, He's too fast")
    print("You put the sniper back over your shoulder as you dodge the dragons attack")
    print("You grab the katana and the glock you still had with you")
    print("You shoot for the dragons eye again")
    print("You hit but it doesn't do a lot of damage")
    print("You sprint to the dragon with your katana")
    print("As the dragon comes for you you dodge making him hit himself on a wall")
    print("When he gets disoriented you climb onto his head")
    print("If your quick you can stab his eye")
    print("You go for the eye barely hitting it but hitting it good enough for the dragon to lose vision")
    print("You use this opportunity to stab the dragon in his throat multiple times")
    print("The dragon eventually dies")
    print("After the dragon died you took a few teeth")
    newlist.append("Dragons tooth")

def plot35(): 
    print("So straight to it huh")
    print("Not my plan of action but hey its you who is doing it so i don't really care")
    print("You sneak up to the dragon shoot it in his jaw")
    print("Shattering it but nothing comes out")
    print("You think to yourself 'Fuck'")
    print("The dragon stands up enraged")
    print("He just charges something but it doesn't come")
    print("The dragon can't do anything his jaw is shattered")
    print("You take this opporunity to shoot it right between its eyes")
    print("Suprisingly enough it works and the dragon falls over")
    print("You take some teeth and leave")
    newlist.append("Dragons tooth")

def plot36(): 
    print("So you go for his legs huh")
    print("You cut his legs and causes the dragon to not being able to stand")
    print("Then you realise the dragon can fly")
    print("Dragon starts to fly and charge an attack")
    print("The dragon fires its beam and fucking kills you in a heartbeat")
    print("That was fucking dumb")
    eind1()

def plot37(): 
    print("You go to buy one")
    print("Really boring but it gets the work done")
    print("You go to an auction and there is one for auction at that moment")
    print("You join in on the bidding and eventually win")
    print("It costing a fuck ton but besides that")
    print("You finally have the tooth")
    newlist.append("Dragons tooth")

def question6():
    print("Do you wish to continue with this quest")
    print("Or do you wish to stop for now?")
    print("A. Continue")
    print("B. Stop")
    Z = input().lower()
    if Z == "a":
        question3()
    elif Z == "b":
        quit

def plot38(): 
    print("So your going with the DSC first")
    print("Alright then good luck")
    print("Unlike normal slimes Demonic slimes fight back")
    print("So where will you start to look for DMC's")
    print("Are you gonna buy one or hunt for one?")
    print("Its on you")
    print("A. Buy")
    print("B. Search")
    P = input().lower()
    if P == "a":
        plot39()
    elif P == "b":
        plot41()

def plot39(): 
    print("You decide to staight up buy one")
    print("You know a store that sells slime cores")
    print("You go there to see if they have a DMC")
    print("You enter the shop and see a old lady at the counter")
    print("She looks very happy to see someone enter the shop")
    print("You walk to her and was about to ask if they had a DMC")
    print("She starts talking and says 'You appear to be in the need of a DMC, am i correct?")
    print("You sort of shocked answer yes")
    print("You ask her how she knew")
    print("She answers with that she didn't")
    print("She tells you to wait here while she goes to get one")
    print("After she gets back she shows 3 different DMC's")
    print("You decide to go with the 3rd one")
    print("She tells that that core used to belond to a mighty man named 'Tempest'")
    print("She also tells that the other 2 were part of a orginization who wanted to kill every human on earth")
    print("But were stopped by orginization called the 'Octagram'")
    print("You decide to just all of them")
    print("After you pay for all the items you leave")
    print("You return home")
    list.append("Demonic slime core")
    question6()

def plot40(): 
    print("So hunting for it")
    print("I will pray for your safety")
    print("You begin with looking near the volcano")
    print("Not going near the ruined city")
    print("Eventually you do find a demon slime")
    print("You attempt to shoot it between the eyes")
    print("You miss the slime gets allerted")
    print("You realise that this was a bad idea but now that you angered it you have to fight it")
    print("You go in but realise as soon as you it it that its a slime")
    print("So you say fuck it")
    print("Point blank sniper shot")
    print("You obviously hit the shot and the slime just fucking explodes")
    print("After that you realise that that was way easier than you thought")
    print("You grab the DMC and leave back home")
    list.append("Demonic slime core")
    question3()

def plot41(): 
    print("So the potion first huh")
    print("atleast max mana potions are suprisingly cheap")
    print("and since you don't wanna bother making one yourself")
    print("You just decide to buy one instead")
    print("You just go to the nearest brewery")
    print("And just buy one there")
    print("After that you go home")
    list.append("High mana potion")
    question6()

def plot42(): 
    print("So the Crystal now huh")
    print("You could find them in caves or you could buy them")
    print("I mean you can get them basically anywhere")
    print("Grow them, mine them or buy them")
    print("Growing takes a really long time")
    print("so it would be mining of buying")
    print("Mining can only be done in well the mines")
    print("But specifically a high rich mana mine")
    print("So what do you decide")
    print("I will have to say they will probably be done pretty quickly")
    print("A. Mine")
    print("B. Buy")
    Crys = input().lower()
    if Crys == "a":
        plot43()
    elif Crys == "b":
        plot44()

def plot43(): 
    print("So mining it")
    print("I mean its a valid choice but might take a to find one")
    print("You just straight up walk to the miners guild and ask if there are any high mana mines nearby")
    print("They answer yea and just follow us")
    print("we were gonna go there now anyways")
    print("You all go there")
    print("You grab a pickaxe and get to work")
    print("Eventually you have enough crystals for a while")
    print("And you finally decide to go home")
    print("You thank the miners and leave")
    print("You get back home with the crystals and put them somewhere for a bit")
    list.append("High mana crystals")
    question6()

def plot44(): 
    print("You just buy it")
    print("You find a crystal shop")
    print("An old lady is sitting behind the counter")
    print("You walk up to her and was about the ask before she interupted you")
    print("'Im going to guess that you are in the need for a high mana crystal")
    print("You were shocked for a second and then answered yes")
    print("She closes what she was doing and stands up and walks to the back")
    print("Coming back with a bag full")
    print("'There you go' you ask how much it will cost and she lists a price")
    print("You're shocked thats pretty cheap compared to other places")
    print("She answers that it doesn't really matter how expensive they are")
    print("What matters is the quality")
    print("You say thats fair and pay")
    print("You grab the bag and thank the old lady")
    list.append("High mana crystals")




def plot45(): 
    print("So you just walk around?")
    print("Nothing else?")
    print("boring af not gonna lie")
    print("but hey its your life not mine")
    print("You just walk around seeing the town hall and roads getting rebuilt")
    print("Apparantly someone bombed the townhall and the roads have always been shitty")
    print("You see people you know and say hello to them")
    print("You have conversations with some and others just a simple hello")
    print("After walking the entire day you just kinda go home")
    print("You saw that it was getting dark")
    print("When you get home you prepare some dinner for yourself")
    print("You head to the pub later and go back home late")
    print("When you get home all your met is your bed")
    print("you doze to sleep as everything fades away")
    eind3()



def plot46(): 
    print("You decide no its time to stop pushing everything away")
    print("You return home to clean")
    print("You look around and see which rooms are the worst")
    print("Then you realise that every room is equally bad")
    print("You think and start to realise that you have been living in this hell hole")
    print("How did you never figure this out")
    print("not even you know")
    print("You don't have the biggest house")
    plot47 ()

def plot47(): 
    print("So you have 4 rooms to clean")
    print("Which one goes first?")
    print("You have to clean all of them")
    print("you have enough time")
    print("Think about it for a bit and then choose")
    print("The rooms are")
    print("A. Living room")
    print("B. Bedroom")
    print("C. Kitchen")
    print("D. Bathroom")
    
    Clean = input().lower()
    if Clean == "a":
        if plot48.counter == 1:
            print("you have done that already")
            print("Choose something else")
            plot47()
        elif plot48.counter == 0:
            plot48()
        
    elif Clean == "b":
        if plot51.counter == 1:
            print("you have done that already")
            print("Choose something else")
            plot47()
        elif plot51.counter == 0:
            plot51()

    elif Clean == "c":
        if plot54.counter == 1:
            print("you have done that already")
            print("Choose something else")
            plot47()
        elif plot54.counter == 0:
            plot54()

    elif Clean == "d":
        if plot57.counter == 1:
            print("you have done that already")
            print("Choose something else")
            plot47()
        elif plot51.counter == 0:
            plot57()
    
def plot48():
    plot48.counter = 0
    plot48.counter += 1
    
    print("You begin with the Living room")
    print("Obviously since its the main room of the house")
    print("The more you look around the more you realise how boring your house is")
    print("You think should i clean correctly or just lightly enough to live and have some of your day left over")
    print("so?")
    print("A. Correctly")
    print("B. Lightly")
    how = input().lower()
    if how == "a": 
        plot49()
    elif how == "b":
        plot50()   

def plot49(): 
    print("You think well obviously i have to do it correctly")
    print("You realise that there is a lot to do but you just do it")
    print("You sort all of it into 2 piles")
    print("Junk and collectibles")
    print("All the junk you sell and the collectibles you keep")
    print("After all the sorting you can finally begin cleaning")
    print("When you're done you admire you work but realise you have so much more to do")
    print("You sell all your junk and put the collectibles you put away around the room")
    plot47()

def plot50(): 
    print("You clean it lightly")
    print("Barely enough to make it a livable living condition")
    print("You start to think that you should probably clean this way better")
    print("All you do is sort stuff out")
    print("You don't really do anything after sorting")
    print("But hey atleast it looks a lot better now")
    print("But you still havea long way to go")
    plot47()

def plot51(): 
    plot51.counter = 0
    plot51.counter += 1
    print("Of course  your bedroom is one of the most important rooms")
    print("Because well you sleep in it")
    print("Pretty obvious not going to lie")
    print("Same question as the others")
    print("Clean it lightly or correctly")
    print("A. Correctly")
    print("B. lightly")
    clean = input().lower()
    if clean == "a":
            plot52()
    elif clean == "b":
            plot53()

def plot52(): 
    print("So you clean it correctly because you have to sleep here")
    print("You can't just sleep on garbage for the rest of your life")
    print("Like the other rooms you sort all of it out")
    print("You sort it into 2 piles")
    print("Junk and collectibles")
    print("After sorting all of it out you sell all the junk to someone")
    print("And you clean the room before anything")
    print("Then after the cleaning you put all the collectibles around the room")
    print("You look at it with pride but that pride quickly fades when you realise you still have to do a lot")
    print("So you better get to work")
    plot47()

def plot53(): 
    print("So you clean it lightly")
    print("lightly enough to live in it")
    print("You begin with sorting all of it")
    print("You throw the trash away and the junk and collectibles you keep in a corner")
    print("It might not be cleaned correctly")
    print("but atleast you can sleep in in")
    plot47()

def plot54():
    plot54.counter = 0
    plot54.counter += 1 
    print("So the kitchen now")
    print("Welp better get to work")
    print("right before we continue with all the cleaning")
    print("How do you want to clean it")
    print("Light or correctly?")
    print("A. Correctly")
    print("B. Lightly")
    clen = input().lower()
    if clen == "a":
        plot55()
    elif clen == "b":
        plot56()

def plot55(): 
    print("So you clean it thoroughly. good choice")
    print("Don't want anything nasty to get on your food now")
    print("You thoroughly clean the kitchen tops for that exact reason")
    print("You once again sort out the everything that doesn't belong in the kitchen")
    print("or is just trash or junk")
    print("Even after your done sorting it all")
    print("You throw away the trash and sell the junk")
    print("And any collectible you find you put around the kitchen as decoration")
    print("When your done you see that your kitchen now looks like an actual kitchen")
    print("And its something to be proud of")
    print("now lets see what else we can clean correctly")

def plot56(): 
    print("You decide to clean the kitchen to a healthy extent")
    print("You sort out the trash and junk")
    print("You of course sell the junk and throw away the trash")
    print("The only thing that you will clean thoroughly is the kitchen counter ")
    print("Because health reasons")
    print("After that you just continue cleaning you other rooms")
    plot47()


def plot57(): 
    plot57.counter = 0
    plot57.counter += 1
    print("Ah yes the bathroom")
    print("Now after you clean this you can finally take a shower")
    print("Yes im saying you smell digusting")
    print("Cunt.")
    print("No but anyways how do you wanna do this one")
    print("A. Correctly")
    print("B. lightly")
    Claen = input().lower()
    if Claen == "a":
        plot58()
    elif Claen == "b":
        plot59()

def plot58(): 
    print("You clean your bathroom thoroughly. Once again good choice")
    print("Its not time to get sick yet")
    print("You shower to stay healthy and smell good")
    print("You do the usual you sort out everything like the other rooms")
    print("You throw away the trash and sell the junk")
    print("You put the collectibles in the other rooms")
    print("Now you can finally shower again")
    print("Now anything else left to clean?")
    plot47()

def plot59(): 
    print("You really decide to do it lightly?")
    print("No i don't accept that")
    print("Ok well I can't really force you but yk")
    print("You do the usual once again")
    print("You throw the trash away and sell the junk")
    print("The one thing you do clean thoroughly is the shower and sink")
    print("No nasty things around here please")
    print("After that hell you look if there is anything left to do")
    plot47()

def plot60():
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

def eind6():
    print("")

def intro():
    print("Do you wish to start?")
    answer = input().lower()
    if answer == "yes":
        plot1()
    elif answer == "no":
        quit
    else:
        print("Mate thats not an acceptable answer")
intro()