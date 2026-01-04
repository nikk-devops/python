test = "We are learing to write in files using python." 


f = open("write.txt", "a") # Open a file in append mode
f.write(test)
f.close()