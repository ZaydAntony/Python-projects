score = 0
valid_choices = ("A", "B", "C", "D")

questions_set =[
    {
        "id":1,
        "Question": "1. How many surahs are in the Holy Quran ?",
        "options": ('A. 114', 'B. 286', 'C. 185', 'D. 200' ),
        "answer": 'A'
    },

    {
        "id":2,
        "Question": "2. Which prophet build the Kaabah ?",
        "options": ('A. Musa (AS)', 'B. Isa (AS)', 'C. Nuh (AS)', 'D. Ibrahim (AS)' ),
        "answer": 'D'
    },
    {
        "id":3,
        "Question": "3. In many days did Allah (SWT) create the heavens and the earth ?",
        "options": ('A. 5', 'B. 2', 'C. 6', 'D. 7' ),
        "answer": 'C'
    },
    {
        "id":4,
        "Question": "4. Which surah in the Quran are muslims encouraged to recite before bed for protection against the punishment of the grave ?",
        "options": ('A. Al-Baqarah', 'B. Al-Mulk', 'C. Al-Fatiha', 'D. An-Nas' ),
        "answer": 'B'
    }
]

def startGame():
    print("------------------TEST YOUR ISLAMIC KNOWLEDGE ☪🎊🎊🕋-------------")
    print("------------------WELCOME--------------")




def userguess():
    while True:
        user_guess = str(input("Please select the answer (A, B, C or D): ")).upper()
        if user_guess == "":
            print("Cannot be empty")
        elif user_guess not in valid_choices:
            print("Answer can only be A, B, C or D")
        else:
            return user_guess

def displayqn():
    for question in questions_set:
        global score
        print(question["Question"])
        for option in question["options"]:
            print(option)
        user_guess = userguess()
        if user_guess == question["answer"]:
            print("correct ✅")
            score += 1
        else:
            print("incorrect 💔")
            print(f"The correct answer is {question["answer"]}")
    print("---------------🎊🎊🎊🎊😉🎊🎊---------")
    print(f"Your final score is {score}/{len(questions_set)}")
    print()
        


startGame()
displayqn()
