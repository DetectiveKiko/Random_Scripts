def user_input():
    start_number = int(input("Enter first number in Fibonacci sequence: "))
    second_number = int(input("Enter second number in Fibonacci sequence: "))
    number_of_iterations = int(input("Enter number of iterations: "))
    while(True):
        if number_of_iterations <= 0:
            number_of_iterations = int(input("Please enter a number greater than 0: "))
        else:
            break

    return start_number, second_number, number_of_iterations

def Fibonacci(start, second, iterations):
    if iterations <= 0:
        print("Please enter a number greater than 0")
        return []

    sequence = [start, second]
    for _ in range(iterations - 2):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

def Fibonacci_to_dict(sequence):
    fibonacci_dict = {}
    for i, num in enumerate(sequence, start=1):
        fibonacci_dict[f"Step {i}"] = num
    return fibonacci_dict

def print_fibonacci(fibonacci_dictionary):
    print(f"\n Number of steps: {len(fibonacci_dictionary)}")
    print(f"Fibonacci Dictionary: ")
    for key, value in fibonacci_dictionary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    start, second, iterations = user_input()
    sequence = Fibonacci(start, second, iterations)
    fibonacci_dict = Fibonacci_to_dict(sequence)
    print_fibonacci(fibonacci_dict)



