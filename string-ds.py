# The function explains how the string is created in background
def string(text):

    # Insert the Unicode points of characters into the arrays
    code_arr = []
    for char in text:
        code_arr.append(ord(char))
    print(code_arr)

    # Convert the array of Unicode points into the chain of characters
    char_chain = ""
    for char in code_arr:
        char_chain += chr(char)
    print(char_chain)

    return

# The function explains how the uppercase function is worked in string
def upper_case(text):

    # Convert the string into array of Unicode points
    code_arr = [ord(char) for char in text]

    # Convert the lowercase character into uppercase
    upper_text = ""
    for code in code_arr:
        # Check the character is lower case and convert into upper case
        if 97 <= code <= 122:
            code -= 32
            upper_text += chr(code)
        # Check the character is upper case and keep it same
        else:
            upper_text += chr(code)

    print(upper_text)
    return


# The function explains how the lowercase function is worked in string
def lower_case(text):
    # Convert the string into array of Unicode points
    code_arr = [ord(char) for char in text]

    # Convert the uppercase character into lowercase
    lower_text = ""
    for code in code_arr:
        # Check the character is uppercase and convert into lowercase
        if 65 <= code <= 90:
            code += 32
            lower_text += chr(code)
        # Check the character is lowercase and keep it same
        else:
            lower_text += chr(code)

    print(lower_text)
    return


# The function explains how swap case is worked in string
def swap_case(text):
    # Convert string into array of Unicode points
    code_arr = [ord(code) for code in text]

    # Swap uppercase into lowercase and vice versa
    swap_text = ""
    for code in code_arr:
        if 97 <= code <= 122:
            code -= 32
            swap_text += chr(code)
        elif 65 <= code <= 90:
            code += 32
            swap_text += chr(code)
        else:
            swap_text += chr(code)

    print(swap_text)
    return

# The function explains how find method is worked in string
def find(text, character):

    # Convert the text into array of characters
    text_arr = [char for char in text]

    # Find the index number of character from the array
    index = -1
    for i in range(len(text_arr)):
        if text_arr[i] == character:
            index = i
        else:
            pass

    print(index)
    return

find("Hello", "l")