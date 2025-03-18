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
print("b. Mjolnir              d. Hofund")
answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the answer is C.")

print("\nQuestion 3:")
print("(Hoshea Shania Lopez) How many were King Henry VIII's wives?")
print("a. 7             c. 6")
print("b. 3             d. 5")
answer = input("Enter your answer: ").upper()

if answer == "C":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the answer is C.")
    
print("\nQuestion 4:")
print("(Hoshea Shania Lopez) Who was the first woman to win a Nobel Prize?")
print("a. Marie Curie           c. Rosa Parks")
print("b. Amy Farrah Fowler     d. Anne Frank")
answer = input("Enter your answer: ").upper()

if answer == "A":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the answer is A.")


# Display score    
print(f"\nCongratulations! You got {score_counter} out of {NUMBER_OF_ITEMS} items.")