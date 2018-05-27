import random
print(""" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌               ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌
▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌     ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌     ▐░▌  ▐░▌               ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          
▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄       ▀▀▀▀▀▀█░█▀▀ ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌             ▐░▌  ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀               ▀    ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                                                                                                                                                                   """)
print("""Welcome to Jackson's RETRO GAME QUIZ
You will be asked a series of multi-choice questions
You will anwser either A, B, C or D
Once you start you wont be able to quit until you've completed the quiz
""")

loop = ""
while loop == "":
    # checks if users input is valid
    def intcheck(question, low, high):
        valid = False
        while not valid:
            error = "Please pick a number from {} to {}".format(low, high)

            try:
                response = int(input(question))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()
            except ValueError:
                print(error)
                print()
    number = intcheck("How many questions would you like to be asked out of 5? ", 1, 5)

    # generates random numbers and shuffles it's order
    orderlist = [i for i in range(10)]
    random.shuffle(orderlist)

    win = 0
    rounds = 0
    # lists for questions, answers and options
    question = ["""
What was Mario's brothers name?
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
What main colour was MegaMan's suit?
A) Blue
B) Black
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
Answer: """, """
What is the blue fireball move called from 'Street Fighter'?
A) Spirit Bomb
B) Blue Fireball
C) Kamehameha
D) Hadouken
Answer: """, """
What letters are on Donkey Kong's tie?
A) TIE
B) MONKEY
C) DK
D) BANANA
Answer: """, """
Who is the villian in 'Fix it Felix'?
A) Donkey Kong
B) Wreck it Ralph
C) Break it Bob
D) Smash it Sam
Answer: """, """
What is the main characters name in 'Tomb Raider'?
A) Lara Croft
B) Princess Peach
C) Indiana Jones
D) Jack Danger
Answer: """, """
How many different shapes are there in 'Tetris'?
A) 5
B) 7
C) 10
D) Infinite"""]
    answer = ['b', 'a', 'a', 'd', 'c', 'd', 'c', 'b', 'a', 'b']
    options = ['a', 'b', 'c', 'd']

    # takes random question from list and checks if it's in options and if the answer is the same as the answer in the list
    for element in orderlist:
        question[element] = input(question[element]).strip().lower()
        if question[element] not in options:
            print("Sorry that was not one of the options so you got it... incorrect")
            rounds += 1
        elif question[element] == answer[element]:
            print('You got it... CORRECT!')
            win += 1
            rounds += 1
        else:
            print('You got it... incorrect')
            rounds += 1

        if rounds == number:
            break

    print("")
    print("You scored... {} out of {}!".format(win, number))
    loop = input("Press <enter> to play again or any key to quit \n")
