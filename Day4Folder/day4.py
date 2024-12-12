# Write all your codes for Day 4 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
print("hello from day4")

plate_is_clean = False
print("i want to eat chicken rice today")
import random

while plate_is_clean == False:
    print("take a mouth of chicken rice")
    random_number = random.randint(1,6)
    if random_number == 6:
        plate_is_clean = True

print("i have finished my chicken rice")