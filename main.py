# Welcome the player to the quiz
print("Welcome to the Rangiora High School Quiz!\n")

# Create a list of questions and answers
questions = [
    "How many houses are in Rangiora High School? ",
    "What day is shorter through the week? ",
    "What house color is Hillary? ",
    "What house color is Rutherford? ",
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

# Print the player's score
print("Quiz complete! Your score is {}/{}.".format(score, len(questions)))
