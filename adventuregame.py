name = input("Type your name: ")
print("Welcome", name, "to this mysterious adventure!")

answer = input(
    "You are standing at the edge of a dark forest and a rocky mountain trail. Do you enter the forest or climb the mountain? (forest/mountain): ").lower()

if answer == "forest":
    answer = input(
        "The forest is dense and quiet. Soon, you find a hidden cave and a glowing tree. Do you enter the cave or approach the tree? (cave/tree): ").lower()

    if answer == "cave":
        print("Inside the cave, you find ancient ruins and treasure. You WIN!")
    elif answer == "tree":
        print("The glowing tree was magical and teleported you to a maze. You get lost forever. You lose.")
    else:
        print("Not a valid option. You lose.")

elif answer == "mountain":
    answer = input(
        "As you climb, a storm begins. You see a shelter and a rope bridge. Do you take shelter or cross the bridge? (shelter/bridge): ").lower()

    if answer == "shelter":
        print("You wait out the storm safely and discover a map to a secret land. You WIN!")
    elif answer == "bridge":
        print("The bridge collapses and you fall into the canyon. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing,", name)
