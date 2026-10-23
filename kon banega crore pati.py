
# Create a program capable of displaying questions to the user like KBC.
# use List data to store the questions and their correct answer.
# Display the final amount the person is taking home after home playing the game.



questions = [
    ["What is the capital of India?",
     ["Mumbai", "New Delhi", "Kolkata", "Chennai"], "B", 1000],

    ["Who is the Father of the Nation in India?",
     ["Nehru", "Bhagat Singh", "Mahatma Gandhi", "Subhash Bose"], "C", 5000],

    ["Which planet is known as the Red Planet?",
     ["Earth", "Mars", "Jupiter", "Venus"], "B", 10000],

    ["Who wrote the Indian National Anthem?",
     ["Rabindranath Tagore", "Premchand", "Sarojini Naidu", "Nehru"], "A", 50000],

    ["How many days are there in a leap year?",
     ["365", "364", "366", "360"], "C", 100000]
]

money = 0

for q in questions:
    print("\n", q[0])

    print("A.", q[1][0])
    print("B.", q[1][1])
    print("C.", q[1][2])
    print("D.", q[1][3])

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q[2]:
        money = q[3]
        print("Correct Answer!")
        print("You won Rs.", money)
    else:
        print("Wrong Answer!")
        print("Correct answer is:", q[2])
        break

print("\nGame Over!")
print("Your final take-home amount is Rs.", money)