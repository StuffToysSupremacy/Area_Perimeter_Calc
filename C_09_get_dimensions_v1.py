import pandas
from tabulate import tabulate
import math


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


def num_check(question, num_type, exit_code=None):
    """Checks users enter an integer / float that is more than
    zero (or the optional exit code)"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter a number more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def calc_dimensions(calc_type):
    """Gets the dimension of the shapes that is needed
    to be calculated"""

    # List for panda
    all_shapes = []
    all_area = []
    all_perimeter = []

    # Dimension dictionary
    dimension_dict = {
        "Shapes": all_shapes,
        "Area": all_area,
        "Perimeter": all_perimeter
    }

    # Loop for testing purposes
    while True:

        if calc_type == "area" and entered_shape == "xxx" and len(all_shapes) == 0:
            print("Oops - you have not entered anything. "
                  "You need at least one shape")
            continue

        # If user choice is the exit code, break the loop
        elif entered_shape == "xxx":
            break

        # Get dimension for calculating area
        if calc_type == "area":

            response = entered_shape

            # get the dimensions of the shape
            if response == "square" or response == "s":
                length_dimension = num_check("Length? ",
                                             "float", "")

                area_result = length_dimension * length_dimension

            if response == "circle" or response == "c":
                # get the radius somehow
                radius_dimension = num_check("Radius? ",
                                             "float", "")

                area_result = math.pi * (radius_dimension ** 2)

            if response == "rectangle" or response == "r":
                # get the dimensions somehow
                length_dimension = num_check("Length? ",
                                             "float", "")
                width_dimension = num_check("Width? ",
                                            "float", "")

                area_result = length_dimension * width_dimension

            if response == "parallelogram" or response == "p":
                # get the dimensions somehow
                height_dimension = num_check("Height? ",
                                             "float", "")
                base_dimension = num_check("Base? ",
                                           "float", "")

                area_result = base_dimension * height_dimension

    all_shapes.append(entered_shape)
    all_area.append(area_result)
    # all_perimeter.append()

    # make panda
    result_frame = pandas.DataFrame(dimension_dict)


# Main routine go here
yes_no_list = ['yes', 'no']
shapes_list = ['circle', 'square', 'rectangle', 'parallelogram', 'triangle', 'trapezium']

# Initialise question details
mode = "regular"

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

    # # end loop when users enter exit code
    if entered_shape == "xxx":
        break

    question_details = calc_dimensions("variable")
    print()


    question_asked += 1
