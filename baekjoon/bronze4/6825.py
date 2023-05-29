weight = float(input())
tall = float(input())
bmi = weight/(tall * tall)

if bmi > 25:
    print("Overweight")
elif 18.5<=bmi<=25:
    print("Normal weight")
else:
    print("Underweight")
