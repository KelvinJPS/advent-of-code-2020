# Pasport processing
# Day 4 advent of code 2020
def main():
    valid_pasp = 0

    with open("input", "r") as input:
        user_doc = ""
        for line in input:
            user_doc += line
            if line == "\n":
                if validate_doc(user_doc):
                    valid_pasp += 1

                user_doc = ""

        if validate_doc(user_doc):
            valid_pasp += 1
        print(valid_pasp)


def validate_doc(user_doc):
    fields = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
    }
    for item in user_doc.split():
        field = item.split(":")[0]
        if field in fields:
            fields[field] = True

    return all(fields.values())


if __name__ == "__main__":
    main()
