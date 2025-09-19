#Checking Eligibility with if and else
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are Elegible to vote.")
# else:
#     print("You are not Elegible to vote.")



#Discount Calculator with elif
# purchase_amount = float(input("Enter Your purchase amount: "))

# if purchase_amount >= 1000:
#     discount = 0.1
# elif purchase_amount >= 500:
#     discount = 0.05
# else: 
#     discount = 0
    
# final_price = purchase_amount * (1 - discount)
# print("Final Price After Disaount: $" + str(final_price)) 



#Letter Grade Assigner with Nested if Statements
# score = int(input("Enter your score: "))

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# else:
#     if score >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
        
# print("Your Grade is: " + grade)


#Task
# Mad Libs Story Generator

# Prompt user for words
weather_adjective = input("Enter an adjective to describe the day: ")
monkey_adjective = input("Enter an adjective to describe the monkey: ")
lion_adjective = input("Enter an adjective to describe the lion: ")
experience_adjective = input("Enter an adjective to describe the experience: ")
animal = input("Name another animal you might see at the zoo: ")

# Conditional variation based on the animal
if animal.lower() == "elephant":
    animal_sentence = "I even saw an elephant spraying water with its trunk!"
else:
    animal_sentence = f"I even saw a {animal} doing something funny!"

# Build and display the story
story = (
    f"On a beautiful {weather_adjective} day, I went to the zoo. "
    f"I saw a funny {monkey_adjective} monkey swinging from the trees. "
    f"Then, I spotted a majestic {lion_adjective} lion lounging in the sun. "
    f"{animal_sentence} What a wild and {experience_adjective} experience!"
)

print("\nYour Mad Libs Story:")
print(story)