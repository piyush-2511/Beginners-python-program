#multiplication table using f string

a = int(input("Enter the number : "))
print(f"Multiplication Table of {a} is:")

for i in range(1,11):
    print(f"{a} X {i} = {a*i}")
