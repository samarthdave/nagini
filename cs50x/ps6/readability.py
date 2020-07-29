# ps6 - cs50x
import re # use regex

def main():
    print("#### Readability ####")

    # user_input = input("Text: ")
    user_input = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"

    result = get_score(user_input)
    print(f"Grade {result}")

# use Coleman-Liau formula
# 0.0588 * L - 0.296 * S - 15.8
# L - avg # of letters per 100 words
# S is the average number of sentences per 100 words
def get_score(_str_input):
    _clean = _str_input.strip()

    _split_words = re.split(r'[ .!?\']+', _clean)
    total_sentence_count = len(list(filter(lambda x: len(x) > 0, re.split(r'[.!?]+', _clean))))
    total_letter_count = sum([len(word) for word in _split_words])

    sum_until_100 = sum([len(word) for word in _split_words[:100]])
    L = sum_until_100 / min(len(_split_words), 100)

    print(f"Total letters: {total_letter_count}")
    print(f"Sentence count: {total_sentence_count}")
    print(f"L value: {L}")

    # result = 0.0588 * L - 0.296 * S - 15.8
    return 1

if __name__ == "__main__":
    main()