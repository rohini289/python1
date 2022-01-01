#Introduce BMI Calculator
print ('Welcome to BMI Calculator!')

#Ask if user would like to use Metric or Imperial units
input1 = input ('Would you like to input Metric units or Imperial units? ')

#If Imperial... If Metric... Calculate BMI...
if input1 == 'imperial':
    heightIN = float(input('Input your height in Inches (in): '))
    weightLB = float(input('Input your weight in Pounds (lbs):' ))
    BMI = round(((weightLB/(heightIN*heightIN))*703), 2) 


    if BMI >= 19 and BMI <= 24:
        print ('Your BMI is', BMI, 'so, you are healthy weight!')

    elif BMI >= 25 and BMI <= 29:
        print ('Your BMI is', BMI, 'so, you are overweight!')

    elif BMI >= 30 and BMI <= 39:
        print ('Your BMI is', BMI, 'so, you are obese!')

    elif BMI > 39:
        print ('Your BMI is', BMI, 'so, you are extremely obese!')

    elif BMI < 19:
        print ('Your BMI is', BMI, 'so, you are underweight!')

elif input1 == 'metric':
    heightCM = float(input('Input your height in Centimeters (cm): '))
    weightKG = float(input('Input your weight in kilograms (kg): '))
    heightM = heightCM*0.01
    BMI = round((weightKG/(heightM*heightM)), 2)

    if BMI >= 19 and BMI <= 24:
        print ('Your BMI is', BMI, 'so, you are healthy weight!')

    elif BMI >= 25 and BMI <= 29:
        print ('Your BMI is', BMI, 'so, you are overweight!')

    elif BMI >= 30 and BMI <= 39:
        print ('Your BMI is', BMI, 'so, you are obese!')

    elif BMI > 39:
        print ('Your BMI is', BMI, 'so, you are extremely obese!')

    elif BMI < 19:
        print ('Your BMI is', BMI, 'so, you are underweight!')

else:
    print ('There was an error with your input. Please restart the program!')
    
