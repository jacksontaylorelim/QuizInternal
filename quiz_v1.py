correct = "You got it... CORRECT!"
incorrect = "You got it... incorrect"
print("""Welcome to Jackson's RETRO GAME QUIZ
You will be asked a series of multi-choice questions
You will anwser either A, B, C or D
At the end you will be given your score out of 5""")

question1 = input("""
What was Mario's brothers name? Was it...
A) Wario
B) Luigi
C) Yoshi
D) Toad
Answer: """).strip().lower()
if question1 == "b":
    print(correct)
else:
    print(incorrect)

question2 = input("""
Complete the character name. Sonic the...
A) Hedgehog
B) Walrus
C) Human
D) Unicorn
Answer: """).strip().lower()
if question2 == "a":
    print(correct)
else:
    print(incorrect)

question3 = input("""
What colour was MegaMan's suit? Was it...
A) Blue
B) Red
C) White
D) All of the above
Answer: """).strip().lower()
if question3 == "a":
    print(correct)
else:
    print(incorrect)

question4 = input("""
What were all of the Pacman ghost names?
A) Ghost 1, Ghost 2, Ghost 3 and Ghost 4
B) Inkie, Winkie, Pinkie and Clint
C) Stink, Winky, Tinky and Lyde
D) Inky, Blinky, Pinky and Clyde
Answer: """).strip().lower()
if question4 == "d":
    print(correct)
else:
    print(incorrect)

question5 = input("""
What is the name of the main character from 'The Legend of Zelda'?
A) Elijah
B) Zelda
C) Link
D) Strife
Answer: """).strip().lower()
if question5 == "c":
    print(correct)
else:
    print(incorrect)
