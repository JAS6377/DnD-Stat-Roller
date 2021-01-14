# Created by Jason Smith
# January 13, 2021
# Base code taken from https://github.com/JAS6377/DnD-Stat-Roller/blob/master/Stat_Roller.py

# Define Variables
import random
import math
stats = int(input("How many stats would you like to roll? -- "))
print()
diesize = 6
rolls = int(input("How many dice per stat (3 for hardcore, 4 will drop the lowest from each set)? -- "))
statoutput = []

print()

# This time it's not snarky. Mainly because I'm lazy.
if rolls < 3 or rolls > 4:
    print("Invalid input.")
    print()
    rolls = int(input("How many dice per stat? (3 for hardcore, 4 will drop the lowest from each set) "))
    print()
elif rolls == 3:
    print("Hardcore selected. Only 3 dice will be rolled per stat. Good luck!")
    print()
elif rolls == 4:
    print("4 dice will be rolled per stat. The lowest will be dropped.")
    print()

input("Press ENTER to roll your stats.")
print("--------------------------------------------------")

# Set the loops
for i in range(0, stats):
    for x in range(0, rolls):
        statoutput.append(random.randint(1, diesize))

# LOOK!!! No more hardcoded matrix math! It's like I'm learning or something!
for i in range(0, stats):
    stat = statoutput[rolls*i:rolls*(i+1)]

    if rolls == 4:
        stat.remove(min(stat))

    s = sum(stat)
    sx = math.floor((s-10)/2)

    # Print the roll outputs. But, like, looped. Because hell yeah.
    print("Stat ", i+1, "rolls: ", stat)
    # Print the base stats and bonuses
    print("Stat ", i+1, "total is ", s, ", and the bonus is +", sx)
    print()
