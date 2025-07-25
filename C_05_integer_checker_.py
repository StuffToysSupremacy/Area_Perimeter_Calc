# Functions go here
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

# loop for testing purposes...
while True:
    # my_int = num_check("How many questions would you like? <enter> for infinite: ",
    #                    "integer", "")
    #
    # if my_int == "":
    #     print("You have chosen infinite mode.")
    # else:
    #     print(f"Thanks. You chose {my_int}")
    #
    # print()

    my_float = num_check("Please enter the length: ", "float")
    print(f"Thanks. You chose {my_float}")
    print()
