import os

def DoSomething(a, B):
    x = 5  # unused variable
    if a == True:  # E712: comparison to True
        print("True branch")
    else:
        print("False branch")

    for i in range(0, 10): print(i)  # E701: multiple statements on one line

    password = input("Enter password:")  # B322: input used (security concern)

    os.system("ls -l")  # B605: shell command injection risk

def complex_function(x, y, z):
    if x > 0:
        if y > 0:
            if z > 0:
                return x + y + z
            else:
                return x + y - z
        else:
            if z < 0:
                return x - y + z
            else:
                return x - y - z
    else:
        return 0
