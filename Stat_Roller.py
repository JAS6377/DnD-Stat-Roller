# Created by Jason Smith
# September 2, 2019

# Define Variables
import random
import math
stats = 5
diesize = 6
rolls = int(input("How many dice per stat? (3 for hardcore, 4 will drop the lowest from each set) "))
fail = 0
statoutput = []

print()

# Tracking your fails
if rolls < 3 or rolls > 4:
    print("Invalid input.")
    print()
    rolls = int(input("How many dice per stat? (3 for hardcore, 4 will drop the lowest from each set) "))
    print()
    fail = fail + 1
elif rolls == 3:
    print("Hardcore selected. Only 3 dice will be rolled per stat. Good luck!")
    print()
elif rolls == 4:
    print("4 dice will be rolled per stat. The lowest will be dropped.")
    print()

if fail == 1 and (rolls < 3 or rolls > 4):
    rolls = int(input("Try again. 3 or 4? "))
    print()
    fail = fail + 1
elif rolls == 3 and fail == 1:
    print("Hardcore and fat-fingered. Away we go!")
    print()
elif rolls == 4 and fail == 1:
    print("Rolling 4 dice per stat. Good choice!")
    print()

if fail == 2 and (rolls < 3 or rolls > 4):
    rolls = int(input("Really? "))
    print()
    fail = fail + 1
elif rolls == 3 and fail == 2:
    print("Are you sure about that..? Alright then.")
    print()
elif rolls == 4 and fail == 2:
    print("Perhaps for the best.")
    print()

if fail == 3 and (rolls < 3 or rolls > 4):
    rolls = int(input("You're hopeless. You get 1 more shot. 3 or 4? "))
    print()
    fail = fail + 1
elif rolls == 3 and fail == 3:
    print("If past performance is any indication, I'm not sure this is the best choice for you.")
    print()
elif rolls == 4 and fail == 3:
    print("Yeah, you made the right choice.")
    print()

if fail == 4 and (rolls < 3 or rolls > 4):
    print("Since you obviously can't handle the simplest of tasks, "
          "you need every bit of help you can get. Rolls set to 4")
    print()
    rolls = 4

input("Press ENTER to roll your stats.")
print("--------------------------------------------------")

# Set the loops
for i in range(0, stats):
    for x in range(0, rolls):
        statoutput.append(random.randint(1, diesize))

# DO THE MATH! It's the matrix math
stat1 = statoutput[0:rolls]
stat2 = statoutput[rolls:rolls*2]
stat3 = statoutput[rolls*2:rolls*3]
stat4 = statoutput[rolls*3:rolls*4]
stat5 = statoutput[rolls*4:rolls*5]

if rolls == 4:
    stat1.remove(min(stat1))
    stat2.remove(min(stat2))
    stat3.remove(min(stat3))
    stat4.remove(min(stat4))
    stat5.remove(min(stat5))

s1 = sum(stat1)
s2 = sum(stat2)
s3 = sum(stat3)
s4 = sum(stat4)
s5 = sum(stat5)

s1x = math.floor((s1-10)/2)
s2x = math.floor((s2-10)/2)
s3x = math.floor((s3-10)/2)
s4x = math.floor((s4-10)/2)
s5x = math.floor((s5-10)/2)

# Print the roll outputs
print("Stat 1 rolls: ", stat1)
print("Stat 2 rolls: ", stat2)
print("Stat 3 rolls: ", stat3)
print("Stat 4 rolls: ", stat4)
print("Stat 5 rolls: ", stat5)
print()

# Print the base stats and bonuses
print("Stat 1 total is ", s1, ", and the bonus is +", s1x)
print("Stat 2 total is ", s2, ", and the bonus is +", s2x)
print("Stat 3 total is ", s3, ", and the bonus is +", s3x)
print("Stat 4 total is ", s4, ", and the bonus is +", s4x)
print("Stat 5 total is ", s5, ", and the bonus is +", s5x)
