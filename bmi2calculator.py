'''
Sierra Andreason
IS 303 

Inputs
- name
- height
- weight
- age
- sex

Processes
- Input validation
- Calculate BMI - weight / height^2 * 703
- Categorize BMI (WHO BMI Classification)
    -underweight >18.5
    -healthy 18.5-24.9
    -overweight 25.0-29.0
    -Obese 30.0-39.0
    -Severe obesity 40+

Outputs:
- Report for an individual
'''
#collect inputs
name = input("Name: ")
age = input("Age: ")
sex = input("Sex: ")
height = input("Height (in inches): ")
weight = input("Weight (in pounds): ")

#Input Validation -- makes it so age doesn't crash if use
age = age.replace("."," ",1)
age_is_int = age.isdigit()
if age_is_int == True:
    age = int(age)
age_is_reasonable = False
if age_is_int == True and age < 140 or age > 1:
        age_is_reasonable = True 
# to avoid breaks in the system, even if a user inputs "John" or another random string

sex = sex.lower()
sex_is_valid = False
if sex == "Male" or sex == "Female":
        sex_is_valid = True

height = height.replace("."," ",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = False
if height_is_int ==True and height >= 12 or height <= 140:
        height_is_reasonable = True 

weight = weight.replace("."," ",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = False
if weight_is_int ==True and weight >= 12 or weight <= 1200:
        weight_is_reasonable = True

ready_to_process = True

if age_is_int == False or  age_is_reasonable == False:
    print("You entered a non-expected age, please use whole numbers! ")
    ready_to_process = False

if sex_is_valid == False: 
       print("You entered a non-expected sex. Please use male or female. ")

if height_is_int == False or height_is_reasonable == False:
       print("You entered a non-expected height. Please use whole numbers between 1 and 140 inches! ")

if weight_is_int == False or weight_is_reasonable == False:
       print("You entered a non-expected weight. Please use whole numbers between 12 and 1200 pounds! ")

'''
- Categorize BMI (WHO BMI Classification)
    -underweight >18.5
    -healthy 18.5-24.9
    -overweight 25.0-29.0
    -Obese 30.0-39.0
    -Severe obesity 40+
'''
if ready_to_process == True:
      bmi = (weight / height ** 2) * 703
      bmi_category = " "
      if bmi < 18.5:
            bmi_category = "Underweight"
      elif bmi <=24.9:
            bmi_category = "Healthy"
      elif bmi <=29.9:
            bmi_category = "Overweight"
      elif bmi <=39.9:
            bmi_category = "Obese"
      else:
            bmi_category = "Severely Obese"

# Report
print(f"Report for {name}\n"
      f"{age} year old {sex}\n"
      f"Your BMI is {bmi:.2f}.\n"
      f"Your BMI category is: {bmi_category}")
        