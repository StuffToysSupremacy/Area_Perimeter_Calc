# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


# checks the user enters an integer
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            print(error)
            # return "invalid"


# Initialise question details
mode = "regular"

question_asked = 0

calc_heading = make_statement("Area and Perimeter calculator", "🔢")
print(calc_heading)


# Ask user for the number of questions / infinite mode
num_question = int_check("How many questions would you like to do? push <enter> for infinite mode: ")

if num_question == "infinite":
    mode = "infinite"
    num_question = 5

# Question loop starts here
while question_asked < num_question:

    # Question Heading
    if mode == "infinite":
        question_heading = f"\nQuestion {question_asked + 1} (Infinite Mode)🔢 "

    else:
        question_heading = f"\nQuestion {question_asked + 1} of {num_question}🔢"

    print(question_heading)

    # get user response
    user_answer = input("What is the shape? ")

    # If user choice is the exit code, break the loop
    if user_answer == "xxx":
        break

    question_asked += 1

    # if users are in infinite mode, increase number of question!
    if mode == "infinite":
        num_question += 1.
