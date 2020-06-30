# expected output of mario.py
"""
$ ./mario
Height: 4
   #  #
  ##  ##
 ###  ###
####  ####
"""

def main():
    print("### Mario ###")

    user_input = ""
    user_int = 0
    # force loop start
    while not (1 <= user_int <= 8):
        user_input = input("Height: ")
        user_int = int(user_input)
    
    print(f'printing pyramid of {user_int} height')

    # print pyramid
    for row_length in range(1, user_int+1):
        print(" "*(user_int - row_length), "#"*row_length, end="")
        print("  ", end="")
        print("#"*row_length)


if __name__ == "__main__":
    main()