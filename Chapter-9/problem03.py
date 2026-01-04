'''
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.

'''

def multiplication_table(n):
    with open(f"table/table_of_{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n*i}\n")

for num in range(2, 21):
    multiplication_table(num)

# --- IGNORE ---            
