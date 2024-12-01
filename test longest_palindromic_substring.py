def longest_palindromic_substring(s):
    palindrom = []
    for i in range(len(s)-1):
        count = i
        substr = ''

        print(i, s[i])
        while(len(s)):
            if count < len(s)-1:
                count += 1
            
            if s[i] == s[count]:
                # print("count === ",count, s[count])
                substr = s[i:count+1]
                # print("substr === ",substr)

                if substr == substr[::-1]:
                    palindrom.append(substr)
                    print("palindrom  ====  ",palindrom[-1])
                    # i = count+2
            if count == len(s)-1:
                break
    
    if palindrom:
        sorted_palindrom = sorted(palindrom, key=len, reverse=True)
        # print(sorted_palindrom[0])
        return sorted_palindrom[0]



# Example usage
s = "mylevelisveryhighinmalayalamlanguage"
longest_palindromic_substring(s)



'''
# efficient looping algo
def longest_palindromic_substring(s):
    palindrom = []
    i = 0
    while(len(s)-1):
        count = i
        substr = ''

        if i == len(s)-1:
            break

        print(i, s[i])
        while(len(s)-1):
            if count < len(s)-1:
                count += 1
            if count == len(s)-1:
                break
            if s[i] == s[count]:
                print("count === ",count, s[count])
                substr = s[i:count+1]
                print("substr === ",substr)

                if substr == substr[::-1]:
                    palindrom.append(substr)
                    print("\n\n =========  palindrom  ====  ",palindrom[-1])
                    i = count
                    count = i
                    break
            if count == len(s)-1:
                break
        
        i += 1

    if palindrom:
        sorted_palindrom = sorted(palindrom, key=len, reverse=True)
        # print(sorted_palindrom[0])
        return sorted_palindrom[0]
'''
