score_counter = 0 
NUMBER_OF_ITEMS = 10

print ("\n\t\t\tGTech Quiz!")
print ("Directions: Choose the letter of the correct answer.")

# Display the question number
print("\nQuestion 1:")
# Display the question and choices
print("(Adriel Joseph Dimayuga) Who was the first Avenger?")
print("a. Iron Man        c. Captain America")
print("b. Thor            d. Hulk")
# Input answer to the question, automcatically sets the answer to upper case
answer = input("Enter your answer: ").upper()

# Check if answer is correct
if answer == "C":
    # Display confirmation
    print("Your answer is correct!")
    # Add 1 to the score
    score_counter += 1
else:
    # Display user's answer and the correct answer
    print(f"{answer} is incorrect, the answer is C.")
    
print("\nQuestion 2:")
print("(Adriel Joseph Dimayuga) What is the name of Thor’s hammer?")
print("a. Stormbreaker        c. Gungnir")
print("b. Mjolir              d. Hofund")
answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the answer is C.")
    

# Display score    
print(f"\nCongratulations! You got {score_counter} out of {NUMBER_OF_ITEMS} items.")