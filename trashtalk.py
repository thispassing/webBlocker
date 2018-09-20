# testing a loop to change chat log from an online game based on age.  if age is < 18, then certain words
# being written will trigger the line to be deleted automatically

import time

filter_list = ["bad", "suck", "cy@"]
age = int(input("Are you old enough? Enter your age: "))
good_c = "cya"
bad_c = "cy@"
when_30 = "AHAHAHAHA\nPWNED\n"
# quick = file.write(f"hey everyone\ni'm andy hehe\nyou are bad!!!!!!!!!!!!\ni win\ngg\n{good_c}\nyou suck haha!!!!!!!!!!\n{bad_c}")

while True:
    if age < 18:
        with open("gamelog.txt", 'r+') as file:
            content=file.readlines()
            file.seek(0)
            file.write(f"hey everyone\ni'm andy hehe\nyou are bad!!!!!!!!!!!!\ni win\ngg\n{good_c}\nyou suck haha!!!!!!!!!!\n{bad_c}")
            file.seek(0)
            for line in content:
                if not any(bad in line for bad in filter_list):
                    file.write(line)
            file.truncate()
            print("done")
        break
    elif age == 30:
        with open("gamelog.txt", 'r+') as file:
            content=file.read()
            file.seek(0)
            file.write(f"AHAHAHAHA\nPWNED\n{bad_c}")
            file.truncate()
            print("that was different")
        break
    else:
        with open("gamelog.txt", 'r+') as file:
            file.seek(0)
            file.write(f"hey everyone\ni'm andy hehe\nyou are bad!!!!!!!!!!!!\ni win\ngg\n{good_c}\nyou suck haha!!!!!!!!!!\n{bad_c}")
            file.truncate()
            print("done right")
        break
