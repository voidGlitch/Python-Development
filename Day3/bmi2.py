height = float(input("please enter your height in meters \n"))
weight = float(input("please enter your weight in kg's \n"))
bmi = weight / (height ** 2)
bmi =round(bmi,2)
print("your bmi is " + str(bmi))
if(bmi<=18.5):
    print("You  are underweight")
elif(bmi<=25):
    print("you have a norml weight")
elif(bmi<30):
    print("you are over weight")
elif(bmi<35):
    print("you are obese")
else:
    print("you are clinically obese")