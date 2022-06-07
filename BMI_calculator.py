# get user input  
height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  

# function to calculate BMI 
BMI = weight / (height/100)**2  


# Output
#print("Your Body Mass Index: ", round(BMI, 2)) 
print(f"Your BMI is {BMI:.2f} and ", end='')

if BMI <= 18.5:  
    print("you are underweight.")  
elif BMI <= 24.9:  
    print("you are healthy.")  
elif BMI <= 29.9:  
    print("you are over weight.")  
elif BMI <=34.9:  
    print("you are obese.")  
else:
    print("you are extremely obese")