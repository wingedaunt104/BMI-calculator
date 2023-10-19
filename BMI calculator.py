import math
#first 3 lines are to get the user input
print("Hello this is a BMI calculator, please enter required information below so we can compute your BMI ")
fullName = input("You will enter your full name after this next step, please press any key and then enter to proceed:")
#Printing the first name

name_parts = fullName.split()
#These lines get the weight
while True:
    fullName = input("Please enter your full name please: ")
    name_parts = fullName.split()
    if len(name_parts) >= 2:
        firstName = name_parts[0]
        print("OK " + firstName + ", now let's proceed.")
        break
    else:
        print("Invalid input. ")
print("")

while True:
    weight = input("Please enter your weight: ")

    try:
        weight = int(weight)  # Attempt to convert input to an integer

        if weight < 91:
            print("Invalid! Weight must be 91 or more.")
        elif weight > 320:
            print("Invalid!! your weight must be below 320, however if your weight is above 320 you should seek medical attention unless you are in a sport")

        else:
            break  # Exit the loop if input is valid

    except ValueError:
        print("Invalid! Please enter a valid integer for weight.")

# At this point, you have a valid integer for weight that is greater than or equal to 100.
print("Weight entered:", weight)


#These lines get the height

while True:
    height = input("Now please enter you height (in inches) 70 , your height and weight will then be immediately calculated: ")
        #these next few lines factor height and weight togehter to get the user's 
    try:
        height = int(height)
        if height < 58:
            print("Invalid!! must be 58-78 inches")
        elif height > 79:
            print("Invalid!! must be 58-78 inches")
        else:
            weightInKilos = float(weight) * 0.45359237 
            heightInMeters = float(height) * 0.0254
            bmi = round(weightInKilos/(heightInMeters ** 2), 1)
            print("your bmi is:", bmi)
            
            break

    except ValueError:
        print ("please enter an integer for weight!!")

    
    
if bmi <= 18.5:
    print("This bmi might mean you're underweight, watch your weight or see a medical advisor")
elif bmi <= 24 and bmi >= 18.6:
    print("This bmi usually means you're at good health for you're height and weight")
elif bmi >= 24.1 and bmi <= 29:
    print ("This bmi for your height and weight usually means you're overweight, you can change this however")
elif bmi >= 29.1 and bmi <= 35:
    print ("This bmi for your height and weight usually means you're obese, but you can easily change it")
elif bmi > 35.1:
    print("This bmi might mean you're morbidly obese")
      

    

    
        

