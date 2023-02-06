import requests
import json

payload = {'Monthh': 'Jul',
 'WeekOfMonth': 1, 
 'DayOfWeek': 'Saturday', 
 'Make': 'Honda', 
 'AccidentArea': 'Urban', 
 'DayOfWeekClaimed': 'Tuesday', 
 'MonthClaimed': 'Sep', 
 'WeekOfMonthClaimed': 4, 
 'Sex': 'Male', 
 'MaritalStatus': 'Single', 
 'Age': 30, 
 'Fault': 'Policy Holder', 
 'PolicyType': 'Sedan - All Perils', 
 'VehicleCategory': 'Sedan', 
 'VehiclePrice': 'more than 69000', 
 'PolicyNumber': 29, 
 'RepNumber': 9, 
 'Deductible': 400, 
 'DriverRating': 1, 
 'Days_Policy_Accident': 'more than 30', 
 'Days_Policy_Claim': 'more than 30', 
 'PastNumberOfClaims': 'none', 
 'AgeOfVehicle': 'new', 
 'AgeOfPolicyHolder': '16 to 17', 
 'PoliceReportFiled': 'No', 
 'WitnessPresent': 'No', 
 'AgentType': 'External', 
 'NumberOfSuppliments': 'none', 
 'AddressChange_Claim': 'no change', 
 'NumberOfCars': '1 vehicle', 
 'Yearr': 1994, 
 'BasePolicy': 'All Perils'}

r = requests.post("http://127.0.0.1:8000/predict", data=json.dumps(payload), headers={'Content-Type': 'application/json'})

print(r.json())