# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no_check(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


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


def string_check(question, valid_ans_list, num_letters):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from list of world responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letter
            elif response == item[:num_letters]:
                return item

            elif response == "t":
                return which_t()

        print(f"Please choose an option from {valid_ans_list}")


def which_t():
    """If user inputs 't' ask if its triangle or trapezium"""

    while True:
        # ask for the question...
        response = input("Did you mean triangle? ").lower()

        # verification if its triangle
        # if no it's trapezium
        if response == "yes" or response == "y":
            return "triangle"

        elif response == "no" or response == "n":
            return "trapezium"

        else:
            print("Please enter yes (y) or no (n). \n")


# Main Routine goes here...
yes_no_list = ['yes', 'no']
shapes_list = ['circle', 'square', 'rectangle', 'parallelogram', 'triangle', 'trapezium']

# Initialise question details
mode = "regular"

question_asked = 0

calc_heading = make_statement("Area and Perimeter calculator", "🔢")
print(calc_heading)

# loop fot testing purposes
while True:
    want_instructions = string_check("Do you want to see the instructions? ", yes_no_list, 1)
    print(f"You chose {want_instructions}")

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

        entered_shape = string_check("What is the shape? ", shapes_list, 1)
        print(f"You choose {entered_shape}")

        question_asked += 1

        # if users are in infinite mode, increase number of question!
        if mode == "infinite":
            num_question += 1.
