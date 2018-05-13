import random
orderlist = [i for i in range(5)]
random.shuffle(orderlist)
win = 0

print("""Welcome to Jackson's RETRO GAME QUIZ
You will be asked a series of multi-choice questions
You will anwser either A, B, C or D
At the end you will be given your score out of 5""")

question = ["""
What was Mario's brothers name? Was it...
A) Wario
B) Luigi
C) Yoshi
D) Toad
Answer: """, """
Complete the character name. Sonic the...
A) Hedgehog
B) Walrus
C) Human
D) Unicorn
Answer: """, """
What colour was MegaMan's suit? Was it...
A) Blue
B) Red
C) White
D) All of the above
Answer: """, """
What were all of the Pacman ghost names?
A) Ghost 1, Ghost 2, Ghost 3 and Ghost 4
B) Inkie, Winkie, Pinkie and Clint
C) Stinky, Winky, Tinky and Lyde
D) Inky, Blinky, Pinky and Clyde
Answer: """, """
What is the name of the main character from 'The Legend of Zelda'?
A) Elijah
B) Zelda
C) Link
D) Strife
Answer: """]
answer = ['b', 'a', 'a', 'd', 'c']

for element in orderlist:
    question[element] = input(question[element]).strip().lower()
    if question[element] == answer[element]:
        print('You got it... CORRECT!')
        win += 1
    else:
        print('You got it... incorrect')

print("")
print("You scored... {} out of 5!".format(win))
