a = 100
b = 100
c = 100

if a > b: # if this line is true then only the control flow goes inside this block
    print("a is greater than b")
    print("Yes, I want to tell again A is bigger than b")
else: # if the above if condition fails, then it goes to else block
    print("b is greater than a")

# *************************************
if a > b and a > c: # if this line is true then only the control flow goes inside this block
    print("A is Biggest amongst A,B,c")
    print("Yes, I want to tell again A is bigger than b")
elif b > a and b > c:
    print("B is Biggest than A")

elif c > a and c > b:
    print("C is greater than A")
else: # if the above if condition fails, then it goes to else block
    print("All are equal")

# *************************************
