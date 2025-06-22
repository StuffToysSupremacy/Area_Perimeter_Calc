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


def string_check(question, valid_ans_list, num_letters, exit_code=None):
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

question_asked = 0

calc_heading = make_statement("Area and Perimeter calculator", "🔢")
print(calc_heading)

# loop for testing purposes

want_instructions = string_check("Do you want to see the instructions? ", yes_no_list, 1)
print(f"You chose {want_instructions}")

while True:

    question_heading = f"\n❓❓🔢 Question {question_asked + 1} 🔢❓❓"
    print(question_heading)
    entered_shape = string_check("What is the shape? ", shapes_list, 1)
    print(f"You choose {entered_shape}")

    # # # end loop when users enter exit code
    # if entered_shape == "xxx":
    #     break

    question_asked += 1
