# ----------------------------------------
# Day 02 - String Practice
# Author: Amir Mohammad Taji
#
# Topics:
# - Variables
# - String Concatenation
# - print()
# - lower()
# - len()
# - split()
# ----------------------------------------

name = "Amir Mohammad"
family = "Taji"

fullname = name + " " + family

goal = "I want to build Cyber Jarvis"

print("=" * 40)
print("Full Name :", fullname)
print("Goal      :", goal)
print("=" * 40)

print("Lowercase :", goal.lower())
print("Length    :", len(goal))
print("Words     :", goal.split(" "))
