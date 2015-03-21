# -*- coding: utf-8 -*-
 
"""
Hopscotch Game:
-This is a python program that works as a quiz and tests your knowledge on well known books and authors.
-You would need to answer the questions correctly and hopscotch your way to the finish line to earn some food for thought.
-To play, download and run as a python file: python hs.py 
"""
 
import random
from random import choice
 
#questions and answers
single_block_questions = [("the Harry Potter series","2"),
                        ("The Fountainhead","1"),
                        ("Love Story","1",),
                        ("Jonathon Livingston Seagull","2"),
                        ("Wings of Fire","1")]
double_block_questions = [("George Orwell", "1","2"),
                        ("Malcolm Gladwell", "1", "4")]
single_block_options = [("Stephnie Meyer", "JK Rowling"),
                        ("Ayn Rand", "Cecelia Ahern"),
                        ("Erich Segal", "Nicholas Spark"),
                        ("David Kirkpatrick", "Richard Bach"),
                        ("A P J Abdul Kalam", "Jawaharlal Nehru")]
double_block_options = [("Animal Farm", "Nineteen Eighty Four", "The Room on the Roof", "The Gift of the Magi"),
                        ("Outliers", "Freakonomics", "Superfreakonomics", "Blink")]
 
food_for_thought = [
"You just have to decide whether you are tigger or eyeore.",
"We cannot change the cards we are dealt, just how we play the hand.",
"When it comes to men who are romantically interested in you, it’s really simple. Just ignore everything they say and only pay attention to what they do.",
"Experience is what you get when you didn't get what you wanted.",
"The key question to keep asking is, Are you spending your time on the right things? Because time is all you have.",
"If I only had three words of advice, they would be, Tell the Truth. If got three more words, I'd add, all the time.",
"When you're screwing up and nobody says anything to you anymore, that means they've given up on you.",
"Follow your passions, believe in karma, and you won't have to chase your dreams, they will come to you.",
"Its important to have specific dreams. Dream Big. Dream without fear.",
"All my adult life I've felt drawn to ask long-married couples how they were able to stay together. All of them said the same thing: We worked hard at it."]
 
positive_single_block_message = "Yay! You now hop to the next box!"
positive_double_block_message = "Double yay! You now hop to the twin boxes!"
negative_message = "Oops! We're sorry you picked the wrong answer. Better luck next time!"
final_completion_message = "Congratulations! You just hopscotched your way to the finish line =)"
exit_game_message = "Thanks for trying this out! :)\n"
 
 
def introduction():
    print "Hopscotch - a quiz game"
    print "Are you ready to hop your way through this to earn some Food for Thought? :D\n"
 
    #draw hopscotch
    print '   -----   '
    print '   |   |   '
    print '   -----   '
    print '   -----   '
    print '   |   |   '
    print '   -----   '
    print '   -----   '
    print '   |   |   '
    print '   -----   '
    print '----- -----'
    print '|    |    |'
    print '----- -----'
    print '   -----   '
    print '   |   |   '
    print '   -----   '
    print '----- -----'
    print '|    |    |'
    print '----- -----'
    print "Finish Line\n"
 
 
def get_player_response():
    while True:
        try:
            user_wish = int(raw_input('Hi there, type 1 to start the game and 0 to exit\n'))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if user_wish != 0 and user_wish != 1:
                print "Invalid value, please enter 0 or 1\n"
            else:
                return user_wish
 
 
def game_winner():
    print final_completion_message
    message_number = random.randint(0,9)
    print "Food for thought (from The Last Lecture by Randy Pausch):\n{}\n".format(food_for_thought[message_number])
 
 
def end_game_due_to_incorrect_answer():
    print negative_message
    while True:
        try:
            choice = int(raw_input('Type 1 to restart and 0 to discontinue hopping!\n'))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if choice is not 0 and choice is not 1:
                print "Invalid value, please try again\n"
            elif choice == 1:
                #restart
                get_started()
                return False
            elif choice == 0:
                #choice is 0
                exit_game()
                return False
 
 
def quiz_the_player_single_block(level, question, answer, answer_choices):
    while True:
        try:
            print "Q: Name the author of {}".format(str(question))
            user_answer = int(raw_input("1 for {}\n2 for {}\nYour answer: ".format(answer_choices[0], answer_choices[1])))
            print "\n"
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if user_answer is not 1 and user_answer is not 2:
                print "Invalid value, please try again\n"
            elif int(user_answer) == int(answer):
                if level == 3 or level == 5:
                    print positive_double_block_message
                else:
                    print positive_single_block_message
                #increment level as player responded with the right answer
                level += 1
                display_hops(level)
                return level
            elif int(user_answer) != int(answer):
                #exit game with message
                level = -1
                return level
 
 
def quiz_the_player_double_block(level, question, answer1, answer2, answer_choices):
    while True:
        try:
            print "Q: Pick the 2 books written by {}".format(str(question))
            print "Tip: Please enter your answer choices together, in ascending order"
            user_answer = int(raw_input("1 for {}\n2 for {}\n3 for {}\n4 for {}\nYour answer: ".format(answer_choices[0], answer_choices[1], answer_choices[2], answer_choices[3])))
            print "\n"
            answer = str(answer1) + str(answer2)
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if user_answer is not 12 and user_answer is not 13 and user_answer is not 14 and user_answer is not 23 and user_answer is not 24 and user_answer is not 34:
                print "Invalid value, please try again\n"
            elif int(user_answer) == int(answer):
                #increment level as player responded with the right answer
                level += 1
                if (level == 7):
                    #player has won the game
                    game_winner()
                    level = 0
                else: 
                    print positive_single_block_message
                    display_hops(level)
                return level
            elif int(user_answer) != int(answer):
                #exit game with message
                level = -1
                return level
 
 
def play(level, single_block_question_number, double_block_question_number):
    if (level >= 1 and level <= 3) or level == 5:
        #single_block_questions
        question = single_block_questions[single_block_question_number][0]
        answer = single_block_questions[single_block_question_number][1]
        answer_choices = single_block_options[single_block_question_number]
        level = quiz_the_player_single_block(level, question, answer, answer_choices)
        single_block_question_number += 1
        play(level, single_block_question_number, double_block_question_number)
    elif (level == 4 or level == 6):
        #double_block_questions
        question = double_block_questions[double_block_question_number][0]
        answer1 = double_block_questions[double_block_question_number][1]
        answer2 = double_block_questions[double_block_question_number][2]
        answer_choices = double_block_options[double_block_question_number]
        level = quiz_the_player_double_block(level, question, answer1, answer2, answer_choices)
        double_block_question_number += 1
        play(level, single_block_question_number, double_block_question_number)
    elif (level == -1):
        #wrong answer supplied by player
        end_game_due_to_incorrect_answer()
    elif (level == 0):
        #game completed
        exit_game()              
 
 
def display_hops(level):
    if level == 1:
        print '                     |-----|       |-----|'
        print '                     |     |       |     |'
        print '|-----||-----||-----||     ||-----||     |'
        print '|  +  ||     ||     ||-----||     ||-----|'
        print '|-----||-----||-----||     ||-----||     |'
        print '                     |     |       |     |'
        print '                     |-----|       |-----|'
        print '\n'
    elif level == 2:
        print '                     |-----|       |-----|'
        print '                     |     |       |     |'
        print '|-----||-----||-----||     ||-----||     |'
        print '|  +  ||  +  ||     ||-----||     ||-----|'
        print '|-----||-----||-----||     ||-----||     |'
        print '                     |     |       |     |'
        print '                     |-----|       |-----|'
        print '\n'
    elif level == 3:
        print '                     |-----|       |-----|'
        print '                     |     |       |     |'
        print '|-----||-----||-----||     ||-----||     |'
        print '|  +  ||  +  ||  +  ||-----||     ||-----|'
        print '|-----||-----||-----||     ||-----||     |'
        print '                     |     |       |     |'
        print '                     |-----|       |-----|'
        print '\n'
    elif level == 4:
        print '                     |-----|       |-----|'
        print '                     |  +  |       |     |'
        print '|-----||-----||-----||     ||-----||     |'
        print '|  +  ||  +  ||  +  ||-----||     ||-----|'
        print '|-----||-----||-----||     ||-----||     |'
        print '                     |  +  |       |     |'
        print '                     |-----|       |-----|'
        print '\n'
    elif level == 5:
        print '                     |-----|       |-----|'
        print '                     |  +  |       |     |'
        print '|-----||-----||-----||     ||-----||     |'
        print '|  +  ||  +  ||  +  ||-----||  +  ||-----|'
        print '|-----||-----||-----||     ||-----||     |'
        print '                     |  +  |       |     |'
        print '                     |-----|       |-----|'
        print '\n'
    elif level == 6:
        print '                     |-----|       |-----|'
        print '                     |  +  |       |  +  |'
        print '|-----||-----||-----||     ||-----||     |'
        print '|  +  ||  +  ||  +  ||-----||  +  ||-----|'
        print '|-----||-----||-----||     ||-----||     |'
        print '                     |  +  |       |  +  |'
        print '                     |-----|       |-----|'
        print '\n'
    
 
def exit_game():
    print exit_game_message
    return False
 
 
def get_started():
    introduction()
    action = get_player_response()
    if action == 1:
        #start game
        print ("Get set go! And your game starts now!\n\n")
        level = 1
        display_hops(level)
        single_block_question_number = 0
        double_block_question_number = 0
        play(level, single_block_question_number, double_block_question_number)
    elif action == 0:
        #exit game
        exit_game()   
 
 
#start hopping!
get_started()
 
