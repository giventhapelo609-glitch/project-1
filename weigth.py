#this program will convert the weight of a patient from kg to lb and vice versa

# frist we the input from the user to enter the weight of the patient
weight_of_patient = input("Enter your weight: ")

# had to consider facters such as weight measurement into the code 
unit_of_measurement_for_weight = input("Enter the unit of measurement for weight (kg/lb): ")

# this next line of code will be use as the conversion factor to convert the weight from kg to lb and vice versa
weight_opertion = 2.20462

# now we are going to use if and alif statements to check the unit of measurement and perform the conversion accordingly
# this is the out put operation deals with when the user puts kg as there unit of measurement for weight
if unit_of_measurement_for_weight == "kg":    
       result = int(weight_of_patient) / int(weight_opertion) 
       print(f"Thank you for providing your weight as {result} kg")

# this is the out put operation deals with when the user puts lb as there unit of measurement for weight
elif unit_of_measurement_for_weight == "lb":
        result = int(weight_of_patient) * int(weight_opertion)
        print(f"Thank you for providing your weight as {result} lb")
