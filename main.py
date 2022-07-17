# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
bmi_in_1dp = round(bmi, 1)
if bmi_in_1dp < 18.5:
  print(f"Your bmi is {bmi_in_1dp}, you are underweight!")
elif bmi_in_1dp < 25:
  print(f"Your bmi is {bmi_in_1dp}, you have a normal weight!")
elif bmi_in_1dp < 30:
  print(f"Your bmi is {bmi_in_1dp}, you are overweight!")
elif bmi_in_1dp < 35:
  print(f"Your bmi is {bmi_in_1dp}, you are Obese!")
else:
  print(f"Your bmi is {bmi_in_1dp}, you are clinically obese!")



