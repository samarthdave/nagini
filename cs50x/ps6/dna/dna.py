import sys

def main():

    args = sys.argv
    if len(args) != 3:
        print("Error, invalid usage.")
        print("Try: python3 dna.py databases/large.csv sequences/5.txt")
        return

    # read in both files
    database_file = open(args[1], "r")
    i = 0
    STR_sequences = []
    users = []
    # loop thru & add all relevant data
    for line in database_file:
        row = line.strip().split(",")
        # add header row
        if i == 0:
            STR_sequences = row[1:]
            print(row)
        else:
        # otherwise, add user info
            users.append({
                'name': row[0],
                'str_sequences': [int(x) for x in row[1:]]
            })
        i += 1

    # read DNA file:
    dna_file = open(args[2], "r")
    data_line = dna_file.readline()
    str_lengths = []

    # compute the longest run of each STR you've been given
    for sequence in STR_sequences:
        occurrence_count = 0

        if sequence in data_line:
            occurrence_count = 1
            while True:
                # this is awful and inefficient. But I also want to sleep early
                # and couldn't debug what I had earlier that was more efficient :/
                if sequence*occurrence_count not in data_line:
                    occurrence_count -= 1
                    break
                occurrence_count += 1

        str_lengths.append(occurrence_count)

    # compare the counts against each row of the CSV
    found_match = False
    for user in users:
        if str_lengths == user['str_sequences']:
            found_match = True
            print(user['name'])
    
    if not found_match:
        print('No match')

if __name__ == "__main__":
    main()
