import sys


def password_validator(password_input):
    # password_input = password_input.replace(" ", "")
    password_input = password_input.strip()
    password_input = password_input.split(":")
    policy = password_input[0]
    password = password_input[1]

    # Separate word key
    policy = policy.split(" ")
    word_key = policy[1]
    # Separate limits
    policy = policy[0].split('-')
    lower_limit = int(policy[0])
    upper_limit = int(policy[1])
    count = 0

    for c in password:
        if c == word_key:
            count += 1

    if count >= lower_limit and count <= upper_limit:
        return True

    else:
        return False


# example data
def main():
    correct_pass = 0
    with open("2input") as f:
        for line in f:
            if password_validator(line):
                correct_pass += 1
    print(correct_pass)


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
