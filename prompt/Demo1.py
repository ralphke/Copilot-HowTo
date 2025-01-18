# create a function to add two numbers and make it error proof plus call the function from main()
def add_two_numbers(num1, num2):
    try:
        return num1 + num2
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    result = add_two_numbers(5, 7)
    if result is not None:
        print(f"The result is {result}")
    else:
        print("The operation could not be completed.")

if __name__ == "__main__":
    main()