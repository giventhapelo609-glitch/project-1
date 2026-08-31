weight_of_patient = input("Enter your weight: ")
unit_of_measurement_for_weight = input("Enter the unit of measurement for weight (kg/lb): ")
weight_opertion = 2.20462

if unit_of_measurement_for_weight == "kg":    
       result = int(weight_of_patient) / int(weight_opertion) 
       print(f"Thank you for providing your weight as {result} kg")
elif unit_of_measurement_for_weight == "lb":
        result = int(weight_of_patient) * int(weight_opertion)
        print(f"Thank you for providing your weight as {result} lb")
