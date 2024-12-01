def zeros(n):
    result = 0
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i
#         print(n, i, factorial)
    
    print(n, factorial)
    
#     while (factorial % 10 == 0):
#         result += 1
#         factorial = int(factorial / 10)
#         print(result, factorial)

    reverse = str(factorial)[::-1]
    
    for i in reverse:
        print(i)
        if i == '0':
            result += 1
        else:
            break
            
    return result