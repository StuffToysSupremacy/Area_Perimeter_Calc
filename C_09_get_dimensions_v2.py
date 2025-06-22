import numpy as np
import pandas
from tabulate import tabulate
import math


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


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


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1, exit_code="xxx"):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from list of world responses"""

    while True:

        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

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


# Main routine go here
yes_no_list = ['yes', 'no']
shapes_list = ['circle', 'square', 'rectangle', 'parallelogram', 'triangle', 'trapezium']
calc_type_list = ["area", "perimeter", "both"]

# Initialise question details
# mode = "regular"

question_asked = 0

# List to hold the question details
all_shapes = []
all_area = []
all_perimeter = []

# Question dictionary
question_dict = {
    "Shapes": all_shapes,
    "Area": all_area,
    "Perimeter": all_perimeter
}

# Set to be defined
area_result = np.nan
perimeter_result = np.nan

# Program main heading
make_statement("Area and Perimeter calculator", "🔢")


# # loop for testing purposes
while True:

    question_heading = f"\n❓❓🔢 Question {question_asked + 1} 🔢❓❓"
    print(question_heading)
    entered_shape = string_check("What is the shape? ", shapes_list, 1
                                 )
    # if name is exit code, break out of loop
    if entered_shape == "xxx":
        break

    # get the dimensions of the shape
    # Get dimension of square
    elif entered_shape == "square":
        length_dimension = num_check("What is the side length? ",
                                     "float", "")

        area_result = length_dimension ** 2
        perimeter_result = length_dimension * 4

    # Get dimension of circle
    elif entered_shape == "circle":
        # get the radius  
        radius_dimension = num_check("What is the radius? ",
                                     "float", "")

        area_result = math.pi * (radius_dimension ** 2)
        perimeter_result = 2 * math.pi * radius_dimension

    # Get dimension of rectangle
    elif entered_shape == "rectangle":
        # get the dimensions  
        length_dimension = num_check("Enter the length: ",
                                     "float", "")
        width_dimension = num_check("Enter the width? ",
                                    "float", "")

        area_result = length_dimension * width_dimension
        perimeter_result = 2 * (length_dimension + width_dimension)

    # Get dimension of parallelogram
    elif entered_shape == "parallelogram":
        # get the dimensions  
        calc_chosen = string_check("Do you want to do area, perimeter or both? ", calc_type_list, 1)

        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float", "")
            base_dimension = num_check("Base? ",
                                       "float", "")

            area_result = base_dimension * height_dimension

        elif calc_chosen == "perimeter":
            length_dimension = num_check("Length? ",
                                         "float", "")
            width_dimension = num_check("Width? ",
                                        "float", "")

            perimeter_result = 2 * (length_dimension + width_dimension)

        else:
            base_dimension = num_check("Base? ",
                                       "float", "")
            height_dimension = num_check("Height? ",
                                         "float", "")
            length_dimension = num_check("Side?(not base side) ",
                                         "float", "")

            area_result = base_dimension * height_dimension
            perimeter_result = 2 * (length_dimension + base_dimension)


    # Get dimension of triangle
    elif entered_shape == "triangle":
        # get the dimensions  
        calc_chosen = string_check("Do you want to do area, perimeter or both? ", calc_type_list, 1)

        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float", "")
            base_dimension = num_check("Base? ",
                                       "float", "")

            area_result = 0.5 * base_dimension * height_dimension
            perimeter_result = np.nan

        elif calc_chosen == "perimeter":
            s1_dimension = num_check("Side 1? ",
                                            "float", "")
            s2_dimension = num_check("Side 2? ",
                                         "float", "")
            s3_dimension = num_check("Side 3? ",
                                         "float", "")

            perimeter_result = s1_dimension + s2_dimension + s3_dimension

        else:
            # get sides dimension for perimeter
            # use heron's formula to get area
            s1_dimension = num_check("Side 1? ",
                                     "float", "")
            s2_dimension = num_check("Side 2? ",
                                     "float", "")
            s3_dimension = num_check("Side 3? ",
                                     "float", "")

            perimeter_result = s1_dimension + s2_dimension + s3_dimension
            s = perimeter_result * 0.5
            area_result = (s * (s - s1_dimension) * (s - s2_dimension) * (s - s3_dimension)) ** 0.5


    # Get dimension of trapezium
    else:
        # get the dimensions  
        calc_chosen = string_check("Do you want to do area, perimeter or both? ", calc_type_list, 1)

        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float", "")
            base_a_dimension = num_check("Base (A)? ",
                                         "float", "")
            base_b_dimension = num_check("Base (B)? ",
                                         "float", "")

            area_result = 0.5 * (base_a_dimension + base_b_dimension) * height_dimension

        elif  calc_chosen == "perimeter":
            s1_dimension = num_check("Side 1? ",
                                         "float", "")
            s2_dimension = num_check("Side 2? ",
                                         "float", "")
            s3_dimension = num_check("Side 3? ",
                                         "float", "")
            s4_dimension = num_check("Side 4? ",
                                         "float", "")

            perimeter_result = s1_dimension + s2_dimension + s3_dimension + s4_dimension

        else:
            height_dimension = num_check("Height? ",
                                         "float", "")
            base_a_dimension = num_check("Base (A)? ",
                                         "float", "")
            base_b_dimension = num_check("Base (B)? ",
                                         "float", "")
            s1_dimension = num_check("Side 1?(not base) ",
                                     "float", "")
            s2_dimension = num_check("Side 2?(not base) ",
                                     "float", "")

            area_result = 0.5 * (base_a_dimension + base_b_dimension) * height_dimension
            perimeter_result = s1_dimension + s2_dimension + base_a_dimension + base_b_dimension


    question_asked += 1

    all_shapes.append(entered_shape.capitalize())
    all_area.append(area_result)
    all_perimeter.append(perimeter_result)

# make  panda
result_frame = pandas.DataFrame(question_dict)

# make the results frame into a string with the desired columns
result_string = tabulate(result_frame, headers='keys',
                         tablefmt='psql', showindex=False)


result_panda = result_string

print()
print("=== Area & Perimeter Calculator Result ===")
print(result_panda)





    
