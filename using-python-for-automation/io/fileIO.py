# read in inputFile.txt and use builtin open function
file_name = 'inputFile.txt'
# writing to files
pass_file_name = 'PassFile.txt'
pass_file = open(pass_file_name, 'w')
# writing failes
fail_file_name = 'FailFile.txt'
fail_file = open(fail_file_name, 'w')

f = open(file_name, 'r')

# print the entire file
# print(f.read())

# read line by line
count = 0
for line in f:
    count += 1
    # split by space & check for pass or fail ("p" or "f")
    line_split = line.split()
    # f string syntax supported in Python 3.6 or 3.7, I forgot which
    # (eg. f'{3+3}') but use .format for now
    write_str = '{} - {}'.format(count, line)
    print(write_str, end='')
    # check if equals 'P' or 'F' (no check for else)
    if line_split[2] == 'P':
        pass_file.write(write_str)
    elif line_split[2] == 'F':
    # or could use else clause
        fail_file.write(write_str)

print()

# close the streams
f.close()
pass_file.close()