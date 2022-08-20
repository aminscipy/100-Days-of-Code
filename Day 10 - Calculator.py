def calculator():
    first_number = int(input('What is the first no? '))
    should_continue = True

    while should_continue:
        operator = input('+\n-\n*\n/\nwhat operation you want to perform? ')
        second_number = int(input('what is the next number? '))

        def first_calculation():
            if operator == '+':
                return first_number + second_number
            elif operator == '-':
                return first_number - second_number
            elif operator == '*':
                return first_number * second_number
            elif operator == '/':
                return first_number / second_number

        result = first_calculation()
        print(first_number, operator, second_number, '=', result)

        first_number = result
        want_to_continue = input(f"type 'yes' to continue with {result} or type 'no' to start a new calculation: ")\
            .lower()
        if want_to_continue == 'no':
            calculator()


calculator()
