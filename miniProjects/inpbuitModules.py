import time

time_in = int(input("Enter time : "))

for x in range(0,time_in):
    print(f"x : {x}")
    time.sleep(1)


print("end-----")