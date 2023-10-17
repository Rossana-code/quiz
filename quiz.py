#comment

lives = 3

print("**Welcome to our quizz!**")
print("You have 3 lives.")
print()

# Question 1 if lives > 0
print("Question 1:")
question1= input("How many times France soccer team won the World Cup?")
print('Your answer : {}'.format(question1))

while question1 != "2":
    lives -= 1 # same as lives = lives - 1
    print("Sorry, you have {} chances left".format(lives))
    if lives == 0:
        print("Oh no, you lost the quiz...")
        break
    question1= input("How many times France soccer team won the World Cup?")
    print('Your answer : {}'.format(question1))


# Question 2 if lives > 0
if lives > 0:
    print("Question 2:")
    question2 = input("When Apple was founded?")
    print('Your answer : {}'.format(question2))
    while question2 != "1976":
        lives -=1
        print("Sorry, you have {} chances left".format(lives))
        if lives == 0:
            print("Oh no, you lost the quiz...")
            break
        question2 = input("When Apple was founded?")
        print('Your answer : {}'.format(question2))


# Question 3 if lives > 0
if lives > 0:
    print("Question 3:")
    question3 = input("Who founded SpaceX?")
    question3 = question3.lower()
    print("Your answer : {}".format(question3))
    while question3 != "elon musk":
        lives -=1
        print("Sorry, you have {} chances left".format(lives))
        if lives == 0:
            print("Oh no, you lost the quiz...")
            break
        question3 = input("Who founded SpaceX?")
        question3 = question3.lower()
        print("Your answer : {}".format(question3))

if lives > 0:
    print("Well done, you have win!")