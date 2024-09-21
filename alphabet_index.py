# Highest Index (With a Twist)
# Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.

# Examples
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# alphabet_index(alphabet, "Flavio") ➞ "22v"

# alphabet_index(alphabet, "Andrey") ➞ "25y"

# alphabet_index(alphabet, "Oscar") ➞ "19s"
# Notes
# If you're stuck, check the Resources tab.
# sorted() is not best practice.




def alphabet_index(alphabet, name):
    highest_index = -1  # Set to -1 initially, since indexes will start from 0
    highest_letter = ''  # Variable to track the highest letter

    # Iterate over each letter in the name (convert to lowercase)
    for letter in name.lower():
        # Get the index of the current letter in the alphabet
        index = alphabet.index(letter)
        
        # Update if this letter has a higher index than the current highest
        if index > highest_index:
            highest_index = index
            highest_letter = letter

    # Return the index + 1 (for 1-based index) and the corresponding letter
    return f"{highest_index + 1}{highest_letter}"

# Test cases
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(alphabet_index(alphabet, "Flavio"))  # ➞ "22v"
print(alphabet_index(alphabet, "Andrey"))  # ➞ "25y"
print(alphabet_index(alphabet, "Oscar"))  # ➞ "19s"
