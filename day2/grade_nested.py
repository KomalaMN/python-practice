#using nested if
marks = int(input("Enter your marks: "))

if marks >= 50:
    if marks >= 75:
        print("First Class")
    else:
        print("Second Class")
else:
    print("Fail")
