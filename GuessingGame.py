import random

points = 2  # always start with two points
while True:
        print('Welcome, if you want to see the rules, press "r", if you want to begin, press "c": ')    # "c" means continue and "r" means rules
        HowTo = (input())
        if HowTo == "r":    # rules
            print("""
            To win you need to reach 10 points 
            If you guess the number from 1-10 you get two points
            If you want a third guess you need to pay 1 point
            """)
        elif HowTo == "c":  # starts game if user types "c"
            while not points >= 10:     # you win if you reach 10 points
                print("-" * 80)
                print(f"Current score: {points}")
                print("Guess a number between 1 and 10: ")
                guess = int(input()) # first guess

                answer = random.randint(1,10)   # picks a random number bettween 1 and 10

                if guess == answer:
                    print("Good job, you guessed it!")
                    points = points +2
                else: 
                    if guess != answer:    # not same as answer
                        if guess < answer:  # if guess less than answer
                                print("Guess higher")
                                guess = int(input())    # second guess 
                                if guess == answer:
                                    print("Good job, you guessed it!")
                                    points = points +2
                                else:
                                    print("You've not guessed correctly")   # you need a third try or just continue
                                    print("Press 'c' to continue or give 1 point 'p' to guess agian: ")     # "c" means continue and "p" means play again
                                    User_Input = (input())  # needs to pick between "c" and "p"
                                    if User_Input == "p":
                                        points = points -1  # pays 1 point 
                                        print("You get another chance")
                                        guess = int(input())    # guess again
                                        if guess == answer:
                                            print("Good job, you guessed it!")
                                            points = points +2
                                        else:
                                            print("You've not guessed correctly")
                        else:   # if guess higher than answer
                            print("Guess lower")
                            guess = int(input())    # second guess 
                            if guess == answer: 
                                print("Good job, you guessed it!")
                                points = points +2
                            else:
                                print("You've not guessed correctly")   # you need a third try or just continue
                                print("Press 'c' to continue or give 1 point 'p' to guess agian: ") 
                                User_Input = (input())  # needs to pick between "c" and "p"
                                if User_Input == "p":
                                    points = points -1  # pays 1 point 
                                    print("You get another chance")
                                    guess = int(input())
                                    if guess == answer:
                                        print("Good job, you guessed it!")
                                        points = points +2
                                    else:
                                        print("You've not guessed correctly") 
            if points == 10:
                print("Good Job!! You Won!!")
   
        