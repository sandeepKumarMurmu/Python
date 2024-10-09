# while => wile loop will execute some code while the certain condition remains true.

# name = input("Please enter your name : ");
# name = name.strip()

# while name == '':
#     print("you haven't entered your name ......");
#     name = input("Please enter your name : ");
#     name = name.strip()

# print(f"Your name is {name}")


#for loop => for loop will execute a block of code a fixed number of times 
# you can iterate over a range, string, sequence etc

# for x in range(1,11,2):
#     print(f"x : {x}")


for x in range(1,11):
    if(x==3):
        print("------------")
        # continue
        break
    else:
        print(f"x : {x}")