def lengthOfLongestSubstring(s):
    start = 0
    end = 0
    max_length = 0
    seen = set()
    longest_substring = ""

    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            if end - start > max_length:
                max_length = end - start
                longest_substring = s[start:end]
        else:
            seen.remove(s[start])
            start += 1

    return longest_substring

a = lengthOfLongestSubstring("geeksforgeeks")
print(a)