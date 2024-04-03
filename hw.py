print("You are exploring a rainforest in search of treasure.")
print("Legend has it that there are some buried on a nearby island.")
print("You come across a lake. Do you want to swim across, or wait for a boat? (swim/wait):")
ans = input(">>")
if ans == ("swim"):
    print("You get eaten by a hungry shark. Game over.")
elif ans == ("wait"):
    print("A boat arrives and you arrive at the island safely.")
    print("You come to a cave. Do you want to venture inside or walk on? (venture/walk):")
    ans2 = input(">>")
    if ans2 == ("venture"):
        print("You are squished by boulders never to be seen again. Game over.")
    elif ans2 == ("walk"):
        print("You safely walked along the coastline.")
        print("You are at a crossroads. Do you go left, right, or straight? (left/right/straight):")
        ans3 = input(">>")
        if ans3 == ("left"):
            print("You are trampled by a herd of wildebeest. Game over.")
        if ans3 == ("right"):
            print("You get stung by a poisonous wasp. Game over.")
        elif ans3 == ("straight"):
            print("You march on and find the buried treasure! Yippee!!")
