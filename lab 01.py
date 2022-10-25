def singleInt():
    num = int(input("Please enter a single integer: "))
    if num in range(0,101):
        print(True)

    else:
        print(False)

singleInt()
