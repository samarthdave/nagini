# ps6 - cs50x

def main():
    print("#### Readability ####")

    user_input = input("Text: ")

    result = get_score(user_input)
    print(f"Grade {result}")

# use Coleman-Liau formula
# 0.0588 * L - 0.296 * S - 15.8
def get_score(_str_input):
    _clean = _str_input.strip()

    # all integers for calculations
    i = 0
    digit_count = 0
    letter_count = 0
    word_count = 1 # start at 1 since we need to count the first occurrence
    sentence_count = 0

    for letter in _clean:
        if letter.isalpha():
            letter_count += 1
        elif letter.isnumeric():
            digit_count += 1
        elif letter == ' ' and _clean[i + 1]:
            word_count += 1
        elif (letter == "!" or letter == "." or letter == "?"):
            sentence_count += 1
        # increment total length
        i += 1

    # L - avg # of letters per 100 words
    L = float(letter_count * 100 / word_count)
    # S is the average number of sentences per 100 words
    S = float(sentence_count * 100 / word_count)

    # calculate & round answer
    result = 0.0588 * L - 0.296 * S - 15.8
    return int(round(result, 0))

if __name__ == "__main__":
    main()