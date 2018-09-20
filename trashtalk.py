# testing a loop to change chat log from an online game based on age.  if age is < 18, then certain words
# being written will trigger the line to be deleted automatically

import time

filter_list = ["bad", "suck"]
age = int(input("Are you old enough? Enter your age: "))

while True:
    if age < 18:
        with open("gamelog.txt", 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(bad in line for bad in filter_list):
                    file.write(line)
            file.truncate()
            print("done")
        break
    else:
        with open("gamelog.txt", 'r+') as file:
            file.seek(0)
            file.write("hey everyone\ni'm andy hehe\nyou are bad!!!!!!!!!!!!\ni win\ngg\nyou suck haha!!!!!!!!!!\ncya")
            file.truncate()
            print("done right")
        break
