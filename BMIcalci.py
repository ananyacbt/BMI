                  #Body Mass Index
height = input("Enter your height in metre ")
weight = input("Enter your weight in kg ")
BMI = float(weight) / float(height) ** 2 
print(BMI)
if BMI < 18.5: 
    print("You are underweight")
elif BMI < 25:
    print("Your weight is normal")
elif BMI < 30:
    print("You are over weight")
elif BMI < 35:
    print("You are obese")
elif BMI > 35:
    print("You are clinically obese")


