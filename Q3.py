# # Jaise hum list ki length nikalne ki len ka use karte aa rahe hain, waise hi hum strings ki length nikalne ke liye len ka use kar sakte hain.

# string_name = "Shakrudin"
# print (len(string_name))
# # Visualize
# # Yahan print command 9 print karegi kyunki "Shakrudin" mein 9 letters ya charecters hai.

# string_name = "Rishabh Verma"
# print (len(string_name))
# # Visualize
# # Yahan 13 print hoga kyunki "Rishabh" ke 7 letter aur "Verma" ke 5 letter ki ilava beech ka space bhi ek character hai.

# # Aur jaise hum in ka use kar ke yeh dekh sakte hain ki koi item list mein hai ya nahi. Waise hi hum in string ke saath bhi use kar sakte hain. Jaise:

# string_name = "navgurukul"
# if "n" in string_name:
#     print ("n hai")
# else:
#     print ("n nahi hai")
# # Visualize
# # Wahan hum yeh dekh rahe hain ki string_name variable mein n hai ya nahi. Basically in ka use kar ke hume ek boolean milta hai.

# print ("n" in string_name)
# print (type("n" in string_name))




# Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki humara password strong hai.
# 
# Pehle user se ek password ka string input lijiye.
# 
# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:
# 1
# 
# Kam se kam uski length 6 honi chaiye
# 
# 2
# 
# Jada se jada length 16 se jyada na ho
# 
# 3
# 
# Kam se kam ek dollar ka sign ($) hona chaiye
# 
# 4
# 
# Kam se kam password mein 2 ya 8 hona chaiye
# 
# 5
# 
# Password mein capital A ya capital Z hona chaiye
# 
# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, nahi toh "Weak Password" type karo







# import re

# print("Please enter password should be \n1) One Capital Letter\n2) Special Character\n3) One Number \n4) Length Should be 8-18: ")
# pswd = input()
# reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
# match_re = re.compile(reg)
# res = re.search(match_re, pswd)
# if res:
#    print("Strong Password")
# else:
#    print("Weak Password")










# import re

# pattern = ("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")
# password = input("Enter string to test: ")
# result = re.findall(pattern, password)
# if (result):
#     print ("Strong password")
# else:
#     print ("Weak Password")


