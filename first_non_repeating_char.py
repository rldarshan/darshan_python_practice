def first_non_repeating_letter(s):
    result = ""

    for i in s:
        # print(i, s)
        char_count = s.lower().count(i.lower())
        if char_count == 1:
            return i
        elif char_count == 0:
            return result

    return result

print(first_non_repeating_letter("sTreSS"))