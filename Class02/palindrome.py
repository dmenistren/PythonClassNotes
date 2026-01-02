def is_pali():
    """
    Checks if a word is a Palindrome or not
    Args:
        word (string): The word that the user entered in the program
    Returns:
        returns If a word is a Palindrome or not
    """
    #while loop for Palindrome logic
    while True:
        word = input("This is a Palindrome Checker! Please enter your word.").lower().replace(" ", "")
        old_word = word
        new_word = word[::-1]
        if old_word == new_word:
            print("This is a palindrum!")
        else: 
            print("This isn't a palindrum!")
        # run again logic
        while True:
            run_again=input("Do you want to continue?y/n")
            if run_again.lower() == "y":
                break
            elif run_again.lower() == "n":
                print("Process is finishing")
                return
            print("Please enter only y or n!")


is_pali()
