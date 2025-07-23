import numpy as np
import pandas as pd
from tabulate import tabulate
from datetime import date
import math


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


def instructions():
    instructions_heading = make_statement("Instructions", "ℹ️")
    print(instructions_heading)

    print('''
        This program will ask you for....
    -The shape
    - The dimensions of the shape
    -How many decimal places to round up to the results

    Shapes that can be used:
    'circle', 'square', 'rectangle', 'parallelogram', 'triangle', 'trapezium'

    The program would get the dimensions to then calculate
     the area/ perimeter with the dimensions provided.

    After you are done with it, you can use an exit code ('xxx'). 
    The program would then show the results along with the equations 
    used for all the shapes below the table.



        ''')


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
        # If the response is yes its triangle
        if response == "yes" or response == "y":
            return "triangle"
        # If the response is no it's trapezium
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

        # elif response == "":
        #     print(error)

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

question_asked = 0

# List to hold the question details
all_question = []
all_shapes = []
all_area = []
all_perimeter = []

# Question dictionary
question_dict = {
    "Number of Questions": all_question,
    "Shapes": all_shapes,
    "Area": all_area,
    "Perimeter": all_perimeter

}

# Set to be defined
area_result = np.nan
perimeter_result = np.nan

# Program main heading
calc_heading = make_statement("Area and Perimeter Calculator", "🔢")
print(calc_heading)

print()
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# Get dimensions and calculate
while True:

    # Questions heading
    print()
    question_heading = make_statement(f"Question {question_asked + 1}", "❓")
    print(question_heading)

    # asks for tha shapes
    # Words can be identified quickly with their first letter
    # extra question is asked if response is 't'
    entered_shape = string_check("What is the shape? ", shapes_list, 1)
    print(f"You have chosen {entered_shape}")

    # checks that user enter at least one shape
    if entered_shape == "xxx" and len(all_shapes) == 0:
        print("Oops - you have not entered anything. "
              "You need at least one shape")
        continue

    # if name is exit code, break out of loop
    if entered_shape == "xxx":
        break

    # gets the appropriate dimensions of the shape, same with other shapes
    # Get dimension of square and makes its value into float
    elif entered_shape == "square":
        # Get side length dimension
        length_dimension = num_check("What is the side length? ",
                                     "float")
        print(f"You have entered: Length - {length_dimension}")
        area_result = length_dimension ** 2
        perimeter_result = length_dimension * 4

    # Get dimension of circle and makes its value into float
    elif entered_shape == "circle":
        # get the radius dimension
        radius_dimension = num_check("What is the radius? ",
                                     "float")

        print(f"You have entered: Length - {radius_dimension}")
        area_result = math.pi * (radius_dimension ** 2)
        perimeter_result = 2 * math.pi * radius_dimension

    # Get dimension of rectangle and makes its value into float
    elif entered_shape == "rectangle":
        # get the width and height dimensions
        length_dimension = num_check("Enter the length? ",
                                     "float")
        print(f"You have entered: Length - {length_dimension}")
        width_dimension = num_check("Enter the width? ",
                                    "float")
        print(f"You have entered: Width - {width_dimension}")

        area_result = length_dimension * width_dimension
        perimeter_result = 2 * (length_dimension + width_dimension)

    # Get dimension of parallelogram and makes its value into float
    elif entered_shape == "parallelogram":
        # gives user options what to calculate
        calc_chosen = string_check("Do you want to do area, perimeter or both? ", calc_type_list, 1)

        # get the height and base dimensions
        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")
            base_dimension = num_check("Base? ",
                                       "float")
            print(f"You have entered: Base - {base_dimension}")

            area_result = base_dimension * height_dimension

        # get the length  and width dimensions
        elif calc_chosen == "perimeter":
            length_dimension = num_check("Length? ",
                                         "float")
            print(f"You have entered: Length - {length_dimension}")
            width_dimension = num_check("Width? ",
                                        "float")
            print(f"You have entered: Width  - {width_dimension}")

            perimeter_result = 2 * (length_dimension + width_dimension)

        # gets the base, height, and a side that is not the base dimension
        else:
            base_dimension = num_check("Base? ",
                                       "float")
            print(f"You have entered: Base - {base_dimension}")
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            length_dimension = num_check("Side?(not base side) ",
                                         "float")
            print(f"You have entered: Length - {length_dimension}")

            area_result = base_dimension * height_dimension
            perimeter_result = 2 * (length_dimension + base_dimension)


    # Get dimension of triangle and makes its value into float
    elif entered_shape == "triangle":
        # gives user options what to calculate
        calc_chosen = string_check("Do you want to do area, perimeter or both? ", calc_type_list, 1)

        # get the base and height dimensions
        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            base_dimension = num_check("Base? ",
                                       "float")
            print(f"You have entered: Base - {base_dimension}")

            area_result = 0.5 * base_dimension * height_dimension
            perimeter_result = np.nan

        # get all the sides dimensions
        # use heron's formula to get area
        else:
            s1_dimension = num_check("Side 1? ",
                                     "float")
            print(f"You have entered: Side 1 - {s1_dimension}")

            s2_dimension = num_check("Side 2? ",
                                     "float")
            print(f"You have entered: Side 2 - {s2_dimension}")

            s3_dimension = num_check("Side 3? ",
                                     "float")
            print(f"You have entered: Side 3 - {s3_dimension}")

            perimeter_result = s1_dimension + s2_dimension + s3_dimension
            s = perimeter_result * 0.5
            area_result = (s * (s - s1_dimension) * (s - s2_dimension) * (s - s3_dimension)) ** 0.5


    # Get dimension of trapezium  and makes its value into float
    else:
        # gives user options what to calculate
        calc_chosen = string_check("Do you want to do area, perimeter, or both? ", calc_type_list, 1)

        # gets the height, base A, and base B
        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            base_a_dimension = num_check("Base (A)? ",
                                         "float")
            print(f"You have entered: Base A - {base_a_dimension}")

            base_b_dimension = num_check("Base (B)? ",
                                         "float")
            print(f"You have entered: Base B - {base_b_dimension}")

            area_result = 0.5 * (base_a_dimension + base_b_dimension) * height_dimension

        # gets all side of the shape
        elif calc_chosen == "perimeter":
            s1_dimension = num_check("Side 1? ",
                                     "float")
            print(f"You have entered: Side 1 - {s1_dimension}")

            s2_dimension = num_check("Side 2? ",
                                     "float")
            print(f"You have entered: Side 2 - {s2_dimension}")

            s3_dimension = num_check("Side 3? ",
                                     "float")
            print(f"You have entered: Side 3 - {s3_dimension}")

            s4_dimension = num_check("Side 4? ",
                                     "float")
            print(f"You have entered: Side 4 - {s4_dimension}")

            perimeter_result = s1_dimension + s2_dimension + s3_dimension + s4_dimension

        # gets all the dimension
        else:
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            base_a_dimension = num_check("Base (A)? ",
                                         "float")
            print(f"You have entered: Base A - {base_a_dimension}")

            base_b_dimension = num_check("Base (B)? ",
                                         "float")
            print(f"You have entered: Base B - {base_b_dimension}")

            s1_dimension = num_check("Side 1?(not base) ",
                                     "float")
            print(f"You have entered: Side 1 - {s1_dimension}")

            s2_dimension = num_check("Side 2?(not base) ",
                                     "float")
            print(f"You have entered: Side 2 - {s2_dimension}")

            area_result = 0.5 * (base_a_dimension + base_b_dimension) * height_dimension
            perimeter_result = s1_dimension + s2_dimension + base_a_dimension + base_b_dimension

    question_asked += 1

    all_question.append(question_asked)
    all_shapes.append(entered_shape.capitalize())
    all_area.append(area_result)
    all_perimeter.append(perimeter_result)

print()
# Round to the number of decimal place
round_to = num_check("Round to (d.p): ", "integer")

# make  panda
result_frame = np.round(pd.DataFrame(question_dict), round_to)

# make the results frame into a string with the desired columns
result_string = tabulate(result_frame, headers='keys',
                         tablefmt='psql', showindex=False)

result_panda_string = result_string

# strings / output area


# **** Get current date for heading and filename ****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Headings / Strings...
main_heading_string = make_statement("Area & Perimeter Calculator ", "=")
result_heading_string = make_statement("Result Details", "-")

equation_details_heading = make_statement("Area & Perimeter Equations", "=")
equations_details = \
    ('''                     Area                           Perimeter
Square:              length²                        4 x length 
Rectangle:           length x width                 2(length + width)
Circle:              pi(3.14...) x r²               2x pi(3.14...) x r
Triangle:            0.5 x base x height            s1 + s2 + s3   
Parallelogram:       Base x height                  2(side1 + side2)
Trapezium:           0.5 x (base1 + base2)x height  s1 + s2 + s3+ s4
     ''')

# Print area

# List of strings to be outputted / written to file
to_write = [main_heading_string, "\n", result_heading_string,
            result_panda_string, equation_details_heading,
            "\n", equations_details]

# print the output...
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = f"Area_Perimeter_calc_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
import numpy as np
import pandas as pd
from tabulate import tabulate
from datetime import date
import math


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


def instructions():
    instructions_heading = make_statement("Instructions", "ℹ️")
    print(instructions_heading)

    print('''
        This program will ask you for....
    -The shape
    - The dimensions of the shape
    -How many decimal places to round up to the results

    Shapes that can be used:
    'circle', 'square', 'rectangle', 'parallelogram', 'triangle', 'trapezium'

    The program would get the dimensions to then calculate
     the area/ perimeter with the dimensions provided.

    After you are done with it, you can use an exit code ('xxx'). 
    The program would then show the results along with the equations 
    used for all the shapes below the table.



        ''')


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
        # If the response is yes its triangle
        if response == "yes" or response == "y":
            return "triangle"
        # If the response is no it's trapezium
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

        # elif response == "":
        #     print(error)

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

question_asked = 0

# List to hold the question details
all_question = []
all_shapes = []
all_area = []
all_perimeter = []

# Question dictionary
question_dict = {
    "Number of Questions": all_question,
    "Shapes": all_shapes,
    "Area": all_area,
    "Perimeter": all_perimeter

}

# Set to be defined
area_result = np.nan
perimeter_result = np.nan

# Program main heading
calc_heading = make_statement("Area and Perimeter Calculator", "🔢")
print(calc_heading)

print()
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

# Get dimensions and calculate
while True:

    # Questions heading
    print()
    question_heading = make_statement(f"Question {question_asked + 1}", "❓")
    print(question_heading)

    # asks for tha shapes
    # Words can be identified quickly with their first letter
    # extra question is asked if response is 't'
    entered_shape = string_check("What is the shape? ", shapes_list, 1)
    print(f"You have chosen {entered_shape}")

    # checks that user enter at least one shape
    if entered_shape == "xxx" and len(all_shapes) == 0:
        print("Oops - you have not entered anything. "
              "You need at least one shape")
        continue

    # if name is exit code, break out of loop
    if entered_shape == "xxx":
        break

    # gets the appropriate dimensions of the shape, same with other shapes
    # Get dimension of square and makes its value into float
    elif entered_shape == "square":
        # Get side length dimension
        length_dimension = num_check("What is the side length? ",
                                     "float")
        print(f"You have entered: Length - {length_dimension}")
        area_result = length_dimension ** 2
        perimeter_result = length_dimension * 4

    # Get dimension of circle and makes its value into float
    elif entered_shape == "circle":
        # get the radius dimension
        radius_dimension = num_check("What is the radius? ",
                                     "float")

        print(f"You have entered: Length - {radius_dimension}")
        area_result = math.pi * (radius_dimension ** 2)
        perimeter_result = 2 * math.pi * radius_dimension

    # Get dimension of rectangle and makes its value into float
    elif entered_shape == "rectangle":
        # get the width and height dimensions
        length_dimension = num_check("Enter the length? ",
                                     "float")
        print(f"You have entered: Length - {length_dimension}")
        width_dimension = num_check("Enter the width? ",
                                    "float")
        print(f"You have entered: Width - {width_dimension}")

        area_result = length_dimension * width_dimension
        perimeter_result = 2 * (length_dimension + width_dimension)

    # Get dimension of parallelogram and makes its value into float
    elif entered_shape == "parallelogram":
        # gives user options what to calculate
        calc_chosen = string_check("Do you want to do area, perimeter or both? ", calc_type_list, 1)

        # get the height and base dimensions
        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")
            base_dimension = num_check("Base? ",
                                       "float")
            print(f"You have entered: Base - {base_dimension}")

            area_result = base_dimension * height_dimension

        # get the length  and width dimensions
        elif calc_chosen == "perimeter":
            length_dimension = num_check("Length? ",
                                         "float")
            print(f"You have entered: Length - {length_dimension}")
            width_dimension = num_check("Width? ",
                                        "float")
            print(f"You have entered: Width  - {width_dimension}")

            perimeter_result = 2 * (length_dimension + width_dimension)

        # gets the base, height, and a side that is not the base dimension
        else:
            base_dimension = num_check("Base? ",
                                       "float")
            print(f"You have entered: Base - {base_dimension}")
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            length_dimension = num_check("Side?(not base side) ",
                                         "float")
            print(f"You have entered: Length - {length_dimension}")

            area_result = base_dimension * height_dimension
            perimeter_result = 2 * (length_dimension + base_dimension)


    # Get dimension of triangle and makes its value into float
    elif entered_shape == "triangle":
        # gives user options what to calculate
        calc_chosen = string_check("Do you want to do area, perimeter or both? ", calc_type_list, 1)

        # get the base and height dimensions
        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            base_dimension = num_check("Base? ",
                                       "float")
            print(f"You have entered: Base - {base_dimension}")

            area_result = 0.5 * base_dimension * height_dimension
            perimeter_result = np.nan

        # get all the sides dimensions
        # use heron's formula to get area
        else:
            s1_dimension = num_check("Side 1? ",
                                     "float")
            print(f"You have entered: Side 1 - {s1_dimension}")

            s2_dimension = num_check("Side 2? ",
                                     "float")
            print(f"You have entered: Side 2 - {s2_dimension}")

            s3_dimension = num_check("Side 3? ",
                                     "float")
            print(f"You have entered: Side 3 - {s3_dimension}")

            perimeter_result = s1_dimension + s2_dimension + s3_dimension
            s = perimeter_result * 0.5
            area_result = (s * (s - s1_dimension) * (s - s2_dimension) * (s - s3_dimension)) ** 0.5


    # Get dimension of trapezium  and makes its value into float
    else:
        # gives user options what to calculate
        calc_chosen = string_check("Do you want to do area, perimeter, or both? ", calc_type_list, 1)

        # gets the height, base A, and base B
        if calc_chosen == "area":
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            base_a_dimension = num_check("Base (A)? ",
                                         "float")
            print(f"You have entered: Base A - {base_a_dimension}")

            base_b_dimension = num_check("Base (B)? ",
                                         "float")
            print(f"You have entered: Base B - {base_b_dimension}")

            area_result = 0.5 * (base_a_dimension + base_b_dimension) * height_dimension

        # gets all side of the shape
        elif calc_chosen == "perimeter":
            s1_dimension = num_check("Side 1? ",
                                     "float")
            print(f"You have entered: Side 1 - {s1_dimension}")

            s2_dimension = num_check("Side 2? ",
                                     "float")
            print(f"You have entered: Side 2 - {s2_dimension}")

            s3_dimension = num_check("Side 3? ",
                                     "float")
            print(f"You have entered: Side 3 - {s3_dimension}")

            s4_dimension = num_check("Side 4? ",
                                     "float")
            print(f"You have entered: Side 4 - {s4_dimension}")

            perimeter_result = s1_dimension + s2_dimension + s3_dimension + s4_dimension

        # gets all the dimension
        else:
            height_dimension = num_check("Height? ",
                                         "float")
            print(f"You have entered: Height - {height_dimension}")

            base_a_dimension = num_check("Base (A)? ",
                                         "float")
            print(f"You have entered: Base A - {base_a_dimension}")

            base_b_dimension = num_check("Base (B)? ",
                                         "float")
            print(f"You have entered: Base B - {base_b_dimension}")

            s1_dimension = num_check("Side 1?(not base) ",
                                     "float")
            print(f"You have entered: Side 1 - {s1_dimension}")

            s2_dimension = num_check("Side 2?(not base) ",
                                     "float")
            print(f"You have entered: Side 2 - {s2_dimension}")

            area_result = 0.5 * (base_a_dimension + base_b_dimension) * height_dimension
            perimeter_result = s1_dimension + s2_dimension + base_a_dimension + base_b_dimension

    question_asked += 1

    all_question.append(question_asked)
    all_shapes.append(entered_shape.capitalize())
    all_area.append(area_result)
    all_perimeter.append(perimeter_result)

print()
# Round to the number of decimal place
round_to = num_check("Round to (d.p): ", "integer")

# make  panda
result_frame = np.round(pd.DataFrame(question_dict), round_to)

# make the results frame into a string with the desired columns
result_string = tabulate(result_frame, headers='keys',
                         tablefmt='psql', showindex=False)

result_panda_string = result_string

# strings / output area


# **** Get current date for heading and filename ****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Headings / Strings...
main_heading_string = make_statement("Area & Perimeter Calculator ", "=")
result_heading_string = make_statement("Result Details", "-")

equation_details_heading = make_statement("Area & Perimeter Equations", "=")
equations_details = \
    ('''                     Area                           Perimeter
Square:              length²                        4 x length 
Rectangle:           length x width                 2(length + width)
Circle:              pi(3.14...) x r²               2x pi(3.14...) x r
Triangle:            0.5 x base x height            s1 + s2 + s3   
Parallelogram:       Base x height                  2(side1 + side2)
Trapezium:           0.5 x (base1 + base2)x height  s1 + s2 + s3+ s4
     ''')

# Print area

# List of strings to be outputted / written to file
to_write = [main_heading_string, "\n", result_heading_string,
            result_panda_string, equation_details_heading,
            "\n", equations_details]

# print the output...
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = f"Area_Perimeter_calc_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
