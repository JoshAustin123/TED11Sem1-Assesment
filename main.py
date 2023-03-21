# Define a function to ask the player if they want to restart the quiz
def ask_restart():
    restart = input("Do you want to play again? (yes/no) ")
    if restart.lower() == "yes":
        return True
    elif restart.lower() == "no":
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return ask_restart()

# Welcome the player to the quiz and ask for their name
print("Welcome to the Rangiora High School Quiz!\n")
player_name = input("What is your name? ")

# Create a list of questions and answers
questions = [
    "How many houses are there in Rangiora High School? ",
    "What day is shorter through the week? ",
    "What house colour is Hillary? ",
    "What house colour is Rutherford? ",
    "How many terms are there? ",
    "What game do they play normally during summerfest? ",
    "What classes are in H block? ",
    "What classes are based in G block? ",
    "What class is in c3? ",
    "Where is the French class based at? "
]
answers = ["6", "Wednesday", "red", "blue", "4", "benchball", "cooking", "English", "maths", "K block"]

# Set initial score to 0
score = 0

# Loop through each question and ask the player
for i in range(len(questions)):
    # Ask the question
    print(questions[i])
    # Get the player's answer
    player_answer = input()
    
    # Check if the player's answer matches the correct answer
    if player_answer.lower() == answers[i].lower():
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect.\n")

# Print the player's score and thanks for playing message
print("Well done, {}! You scored {}/{}.".format(player_name, score, len(questions)))
print("Thanks for playing the Rangiora High School Quiz!\n")

# Ask the player if they want to restart the quiz
restart = ask_restart()

# If the player wants to restart, run the quiz again
while restart:
    # Set score to 0
    score = 0

    # Loop through each question and ask the player
    for i in range(len(questions)):
        # Ask the question
        print(questions[i])
        # Get the player's answer
        player_answer = input()

        # Check if the player's answer matches the correct answer
        if player_answer.lower() == answers[i].lower():
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")

    # Print the player's score and thanks for playing message
    print("Well done, {}! You scored {}/{}.".format(player_name, score, len(questions)))
    print("Thanks for playing the Rangiora High School Quiz!\n")

    # Ask the player if they want to restart the quiz again
    restart = ask_restart()
