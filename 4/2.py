# Pasport processing
# Day 4 advent of code 2020


def validate_range(value, min, max):
    value = int(value)
    return value >= min and value <= max


def validate_byr(value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return validate_range(value, 1920, 2002)


def validate_iyr(value):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return validate_range(value, 2010, 2020)


def validate_eyr(value):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return validate_range(value, 2020, 2030)


def validate_hgt(value):
    value_cm = value.split("cm")
    value_in = value.split("in")
    is_valid = False
    # If cm, the number must be at least 150 and at most 193.
    if len(value_cm) > 1:
        is_valid = validate_range(value_cm[0], 150, 193)

    # If in, the number must be at least 59 and at most 76.
    if len(value_in) > 1:
        is_valid = validate_range(value_in[0], 59, 193)

    return is_valid


def validate_hcl(value):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if value[0] == "#" and len(value) == 7:
        hcl = value[1:]
        for char in hcl:
            if char.isdigit() and int(char) <= 9:
                continue

            elif char <= "f" and char >= "a":
                continue
            else:
                return False

        # Return as true if there was not invalid field
        return True

    else:
        return False


def validate_pid(value):
    return value.isnumeric()


def validate_ecl(value):
    valids_ecl = ["amb", "blu, brn", "gry", "grn", "hzl", "oth"]
    if value in valids_ecl:
        return True


def validate_cid(value):
    "currently it is not required"
    return True


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
    pasp_fields = {
        "byr": validate_byr,
        "iyr": validate_iyr,
        "eyr": validate_eyr,
        "hgt": validate_hgt,
        "hcl": validate_hcl,
        "ecl": validate_ecl,
        "pid": validate_pid,
        "cid": validate_cid,
    }
    valid_fields = []
    for item in user_doc.split():
        field, value = item.split(":")
        if field in pasp_fields:
            # store the the result of the validation in the list
            valid_fields.append(pasp_fields[field](value))
        else:
            return False

    return all(valid_fields)


if __name__ == "__main__":
    main()
