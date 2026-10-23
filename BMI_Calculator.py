import sys

def calculate():
    weight = float(input("Enter Your Weight in Kilograms  "))
    height = float(input("Enter Your Height in Meters mother father  "))

    bmi = weight / (height * height)

    print("Your BMI is ", round(bmi, 2))

    if bmi < 18.5:
        print("Category : Underweight")
    elif bmi >= 18.5 and bmi < 26:
        print("Category : Normal Weight")
    elif bmi >= 27 and bmi < 30:
        print("Category : Overweight")
    else:
        print("Category : Obese")

    ch = int(input("1 = Calculate Again \n 2 = Break \n = "))
    if ch == 1:
        calculate()
    elif ch == 2:
        sys.exit(0)
    else:
        print("Wrong Choice , Exiting ")
        sys.exit(0)


print("BMI Calculator Program ")

ch = int(input('''
1 = Calculate BMI
2 = Break

'''))

if ch == 1:
    calculate()

elif ch == 2:
    sys.exit(0)

else:
    print("Wrong Input !! Terminating")
