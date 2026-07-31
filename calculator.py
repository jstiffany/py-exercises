print("------------- Calculator -------------")

# easy calcuator...

while True:
    try:
        num_one = float(input("What is the first number? "))
        num_two = float(input("What is the second number? "))

        operation = input("\nWhat is the operation? Ex. +, -, /, *, %, q to quit").lower()

        if operation == "+":
            print(f"\n{num_one} + {num_two} = {num_one + num_two}")

        elif operation == "-":
            print(f"\n{num_one} - {num_two} = {num_one - num_two}")

        elif operation == "/":
            try:
                print(f"\n{num_one} / {num_two} = {num_one / num_two}")
            except ZeroDivisionError:
                print("\nCannot divide by zero!\n")

        elif operation == "*":
            print(f"\n{num_one} * {num_two} = {num_one * num_two}")

        elif operation == "%":
            print(f"\n{num_one} % {num_two} = {num_one % num_two}")

        elif operation == "q":
            print("Exiting calculator...")
            break

    except ValueError:
        print("\nThat isn't a valid number!\n")