'''
1 for rock,
-1 for paper and 
0 for scissor
'''
import random

computer = random.choice([1, -1, 0 ]) # computer's choice

yourChoice = int(input("Enter your choice: 1 for rock, -1 for paper, 0 for scissor: ")) # 1 for rock, -1 for paper, 0 for scissor
youDit = {1: "rock", -1: "paper", 0: "scissor"} # dictionary to store the choices
yChoice = youDit[yourChoice] # get the choice of the user

# check the result

if( computer == 1 and yourChoice == 0):
    print(f"Computer chose rock and you chose scissor. Computer win!")

elif( computer == 1 and yourChoice == -1):
    print(f"Computer chose rock and you chose paper. You win!")

elif( computer == -1 and yourChoice == 1):
    print(f"Computer chose paper and you chose rock. Computer win!")

elif( computer == -1 and yourChoice == 0):  
    print(f"Computer chose paper and you chose scissor. You win!")

elif( computer == 0 and yourChoice == 1):
    print(f"Computer chose scissor and you chose rock. You win!")

elif( computer == 0 and yourChoice == -1):
    print(f"Computer chose scissor and you chose paper. Computer win!") 

else:
    print(f"Computer chose {youDit[computer]} and you chose {yChoice}. It's a draw!")

    


