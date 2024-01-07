#!/usr/bin/python3
#else block

x = 10
if (x > 10):
    print("X greater than 10")
else:
    print("X is less than 11")


for x in range(10):
    print("The current value of x : ", x)
else:
    print("Congratualtions, all items processed successfully")

for x in range(10):
    if (x > 5):
        break
    print("the current value of x : ", x)
else:
    print("Congratualtions, all the items processed successfully")
