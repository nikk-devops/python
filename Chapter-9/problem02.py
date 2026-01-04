'''
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
'''
def game():
    import random
    score = random.randint(0, 100)  # Simulating a game score
    return score

# Read the previous Hi-score from the file

with open("Hi-score.txt", "r") as f:
    hi_score = f.read()
    if(hi_score!=""):
        hi_score = int(hi_score)
    else:
        hi_score = 0

    print(f"Previous Hi-score: {hi_score}")
    if (hi_score < game()):
        print("Congratulations! You've beaten the Hi-score.")
        with open("Hi-score.txt", "w") as f:
            f.write(str(game()))
 
game()