# Day 04 - List Practice
# Author: Amir Mohammad Taji
# Concepts Used:
# - List
# - append()
# - remove()
# - sort()
# - len()
# ==========================================

skills = ["Python",
          "Networking",
          "Linux",
          "English"
          ]

print("Original Skills:", skills)

skills.remove("Linux")
skills.append("Cyber Security")
skills.sort()
skills.append("hard working")

print("Updated Skills:", skills)
print("Number of Skills:", len(skills))
