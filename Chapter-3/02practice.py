# Write a program to fill in a letter template given below with name and date.
# letter = '''
# # Dear <|Name|>,
# # You are selected!
# # <|Date|>
# # Thanks and Regards
# # XYZ

name = input ("Enter your Name")
date = input ("Enter Date")
letter = f'''
Dear {name},        
You are selected!
{date}
Thanks and Regards
XYZ
'''
# print(letter) Let's use the replace function instead

# print(letter.replace("<|Name|>", "Hridyansh").replace("<|Date|>", "5 March 2041"))
