def print_s():
    """Return the 7xN grid for the letter 'S'."""
    return [
        "* * * * * *",
        "*",
        "*",
        "* * * * * *",
        "        *",
        "        *",
        "* * * * * *"
    ]

def print_a():
    """Return the 7xN grid for the letter 'A'."""
    return [
        "  * * *  ",
        " *     * ",
        "* * * * *",
        "*         *",
        "*         *",
        "*         *",
        "*         *"
    ]

def print_l():
    """Return the 7xN grid for the letter 'L'."""
    return [
        "*",
        "*",
        "*",
        "*",
        "*",
        "*",
        "* * * * * *"
    ]

def print_m():
    """Return the 7xN grid for the letter 'M'."""
    return [
        "*       *",
        "*     *",
        "* *   * *",
        "*   *   *",
        "*       *",
        "*       *",
        "*       *"
    ]

def print_o():
    """Return the 7xN grid for the letter 'O'."""
    return [
        "  * * *  ",
        " *     * ",
        "*       *",
        "*       *",
        "*       *",
        " *     * ",
        "  * * *  "
    ]

def print_n():
    """Return the 7xN grid for the letter 'N'."""
    return [
        "*       *",
        "**      *",
        "* *     *",
        "*  *    *",
        "*   *   *",
        "*    *  *",
        "*       *"
    ]

def gather_input():
    """Gather valid word input from the user."""
    valid_letters = set("SALMON")
    while True:
        word = input("Enter a valid word (or 'END' to quit): ").strip()
        if word == "END":
            return word
        if all(letter.upper() in valid_letters for letter in word) and word.isalpha():
            return word.upper()
        print("Invalid input. Please enter a word using only the letters S, A, L, M, O, N.")

def print_word_in_grid(word):
    """Print the word in a grid format."""
    letter_functions = {
        'S': print_s,
        'A': print_a,
        'L': print_l,
        'M': print_m,
        'O': print_o,
        'N': print_n
    }
    
    # Create a list to hold each row of the grid
    grid = [""] * 7
    for letter in word:
        letter_grid = letter_functions[letter]()
        for i in range(7):
            grid[i] += letter_grid[i] + " "  # Add a space between letters

    for row in grid:
        print(row)

def main():
    """Main function to run the program."""
    while True:
        word = gather_input()
        if word == "END":
            print("Exiting the program.")
            break
        print_word_in_grid(word)

if __name__== "_main_":
    main()