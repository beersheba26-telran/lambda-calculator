import re

from lambda_request import calculate_request


def _finish():
    print("\nExiting the calculator. Goodbye!")
def main():
    """ Loop with handling KeyInterrupt  or input containing "exit" 
- The client should enter one input line containing two numbers and operation separated by either space or comma or sharp (#)<br>
- Output should eiter "result=..." or error message 
    """
    print("exit - to exit")
    while True:
        try:
            user_input = input("Enter two numbers and an simple arithmetic operation separated by either space, comma, or sharp (#): \n")
            if "exit" in user_input.lower():
                _finish()
                break
            data = re.split(r'[ ,#]+', user_input.strip())
            calculate_request(data)
        except KeyboardInterrupt:
            _finish()
            break
        except Exception as e:
            print(f"Wrong input: check that you entered two numbers and an operation separated by either space, comma, or sharp (#) and try again. Error details: {e}")
if __name__ == "__main__":
    main()            