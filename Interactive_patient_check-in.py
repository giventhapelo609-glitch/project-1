# Making a basic calculator program
   # Frist we need to put in the frist input to the program

# Interactive patient check-in
   # variables 
patient_name = input("enter your name: ")
patient_surname = input("enter your surname: ")
patient_age = input("enter your age: ")

   # Command to print 
print("Welcome to the patient check-in system")
print(f"hello i'm the new patient, {patient_name} {patient_surname}. Who is{patient_age} years old.")

# Check whether the user is a new patient or not 
print("Answer in small letters")
patient_status = input("Are you a new patient? (yes/no): ")
if patient_status.upper() == "yes":
    print("Welcome to the clinic! Please fill out the registration form.")


    weight_of_patient = input("Enter your weight: ")
    unit_of_measurement_for_weight = input("Enter the unit of measurement for weight (kg/lb): ")
    weight_opertion = 2.20462

    if unit_of_measurement_for_weight == "kg":
        result = int(weight_of_patient) / int(weight_opertion)
    elif unit_of_measurement_for_weight == "lb":
        result = int(weight_of_patient) * int(weight_opertion)   
    print(f"Thank you for providing your weight as {result}")

else:
    print("Welcome back! Please proceed to the check-in desk.")