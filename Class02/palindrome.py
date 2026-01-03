def is_pali(value: str) -> None:
    """
    Get the input and check the value is palindrome or not
    args:
        1. value: word to check the value is palindrome
    """
    old_word = value
    new_word = value[::-1]
    if old_word == new_word:
        print("This is a palindrum!")
    else:
        print("This isn't a palindrum!")


while True:
    input_value = input(
        "This is a Palindrome Checker! Please enter your word.").lower().replace(" ", "")
    is_pali(input_value)
    run_again = input("Do you want to continue?y/n")
    if run_again.lower() == "n":
        print("Process is finishing")
        break
