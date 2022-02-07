# Iss program ko attempt karne ke liye pehle ek users.json naam ki file mein neeche diye hue text ko save karein.

# {
#     "users": [{
#             "firstName": "vidur",
#             "lastName": "singla",
#             "details": {
#                 "age": 21,
#                 "mobileNo": 1234567890,
#                 "City": "Delhi"
#             }
#         },
#         {
#             "firstName": "rishabh",
#             "lastName": "verma",
#             "details": {
#             "details": {
#                 "age": 22,
#                 "mobileNo": 12345678320,
#                 "City": "Chandigarh"
#             }
#         },
#         {
#             "firstName": "abhishek",
#             "lastName": "gupta",
#             "details": {
#                 "age": 25,
#                 "mobileNo": 12332567890,
#                 "City": "Gurgaon"
#             }
#         }
#     ]
# }





import json

with open('users.json') as data_file:    
    data = json.load(data_file)

users = data['users']
print(users,"\n")


for user in users:
    counter = 0
    print ("users full name is " + user['firstName'] + ' ' + user['lastName'])
    while counter < len(user['details']):
        print ("users mobile number is " + str(user['details']['mobileNo']))
        print ("users age  is " + str(user['details']['age']))
        print ("users city is " + str(user['details']['City']))
        counter=counter+1
        break



# users.json file mein users ka data padha hai. Yeh program users.json file ko read kar kar usmein se users ka data print karega. Iss file ko debug kar kar run karo.

# Topics covered:

# Key error

# loop iterates over the wrong list.

# for i in users:
#     print(i)


