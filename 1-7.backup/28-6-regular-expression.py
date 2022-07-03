# điều kiện nhận biết số: 
# 1. Phải có 10 ký tự
# 2. Số đầu tiên phải là số 0
# 3. Số thứ 2 phải <> 0
# 4. Số điện thoại phải là number (0-9)

# def isphonenumber (test):
#     if len(test) !=10:
#         return False
#     elif test[0] !="0":
#         return False
#     elif test[1] == 0:
#         return False
#     for i in range(len(test)):
#         if not test[i].isdecimal():
#             return False
#     return True

# testA = "Call me 0394671054 or 0918357703, press 9999 to meet me"

# fvalue = False

# for i in range(len(testA)):
#     chunk = testA[i:i+10]
#     if isphonenumber(chunk):
#         fvalue = True
#         print("Phone number found: "+ chunk)
# if not fvalue:
#     print ("Could not find any phone number")

import re
testB = "Call me 0394671054 or 0918357703, press 9999 to meet me"
findall= re.findall("0[1-9]\d{8}",testB)
print(findall)