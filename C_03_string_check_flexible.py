# Functions go here
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

        print(f"Please choose an option from {valid_ans_list}")


# Main routine go here
yes_no_list = ['yes', 'no']
# shapes_list = ['circle', 'square', 'rectangle', 'parallelogram', 'triangle', 'trapezium']

while True:
    want_instructions = string_check("Do you want to see the instructions? ", yes_no_list, 1)
    print(f"You chose {want_instructions}")
    # entered_shape = string_check("What is the shape? ", shapes_list, 1)
    # print(f"You choose {entered_shape}")

