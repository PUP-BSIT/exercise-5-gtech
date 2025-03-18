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

print("\nQuestion 5:")
print("(Dianna Rain M. Romero) Who painted the Mona Lisa?")
print("a. Vincent van Gogh      c. Pablo Picasso")
print("b. Leonardo da Vinci     d. Michelangelo")
answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the correct answer is B.")

print("\nQuestion 6:")
print("(Dianna Rain M. Romero) What is the longest river in the world?")
print("a. Amazon River           c. Nile River")
print("b. Yangtze River          d. Mississippi River")
answer = input("Enter your answer: ").upper()

if answer == "C":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the correct answer is C.")

print("\nQuestion 7:")
print("(Althea Aragon) What is the last name of the business tycoon behind the 'No.5' perfume?")
print("a. Chanel              c. Dior")
print("b. Louis Vuitton       d. Coco")
answer = input("Enter your answer: ").upper()

if answer == "A":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the correct answer is A.")

print("\nQuestion 8:")
print("(Althea Aragon) What is the smallest country in the world?")
print("a. Barbados       c. Vatican City")
print("b. Malta          d. Maldives")
answer = input("Enter your answer: ").upper()

if answer == "C":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the correct answer is C.")

print("\nQuestion 9:")
print("(Grace Anne Lim) Which is the shortest month of the year?")
print("a. March     c. April")
print("b. July      d. February")
answer = input("Enter your answer: ").upper()

if answer == "D":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the correct answer is D.")

print("\nQuestion 10:")
print("(Grace Anne Lim) What is the largest planet in our Solar System?")
print("a. Earth         c. Mars")
print("b. Jupiter       d. Neptune")
answer = input("Enter your answer: ").upper()

if answer == "B":
    print("Your answer is correct!")
    score_counter += 1
else:
    print(f"{answer} is incorrect, the correct answer is B.")

# Display score    
print(f"\nCongratulations! You got {score_counter} out of {NUMBER_OF_ITEMS} items.")