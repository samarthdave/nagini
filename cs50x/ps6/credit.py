# Credit - Validate credit card numbers
# https://cs50.harvard.edu/x/2020/psets/1/credit/

# usage:
# $ python credit.py
# Number: 378282246310005
# AMEX

def main():
    print("### Credit ###")
    # usually lengths of 13, 15, 16
    user_card_num_str = input("Number: ")
    user_card_num = int(user_card_num_str)

    # are we checking the first digit?
    is_first_sum = False
    # sum of even & odd numbered locations
    # could do with just one but this is more explicit
    first_sum = 0
    second_sum = 0

    first_str_out = ''
    second_str_out = ''

    # Luhn's Algorithm (see link below)
    # https://cs50.harvard.edu/x/2020/psets/1/credit/#luhns-algorithm
    # 4003600000000014
    while True:
        remaining = user_card_num % 10
        if is_first_sum:
            sum_of_digits = sum(int(d) for d in str(remaining*2))
            first_str_out += f'{remaining}, '
            first_sum += sum_of_digits
        else:
            second_str_out += f'{remaining}, '
            second_sum += remaining
        # alternate state
        is_first_sum = not is_first_sum

        user_card_num = int(user_card_num / 10)
        if user_card_num <= 0:
            break

    print("First set of numbers:")
    print(f'[{first_str_out}]')
    print("========")
    print("Second set of numbers:")
    print(f'[{second_str_out}]')

    # check if valid credit card
    final_sum = first_sum + second_sum
    final_sum_remainder = final_sum % 10

    is_valid_credit_card = final_sum_remainder == 0
    if is_valid_credit_card:
        print("Valid credit card!")

        # American Express start w/ 34 or 37;
        # MasterCard start with 51, 52, 53, 54, or 55
        # all Visa numbers start with 4
        master_card_startings = ["51", "52", "53", "54", "55"]
        if user_card_num_str.startswith("34") or user_card_num_str.startswith("37"):
            print("AMEX")
        elif any([user_card_num_str.startswith(x) for x in master_card_startings]):
            print("Mastercard")
        elif user_card_num_str.startswith("4"):
            print("VISA")
    else:
        print("Invalid credit card!")

if __name__ == "__main__":
    main()