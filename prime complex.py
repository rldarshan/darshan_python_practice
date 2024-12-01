def find_emirp(n):
    prime_no = []
    result = []
    
    def isPrime(n):
        if n < 2:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if n > 12:
        for i in range(13, n):
            if isPrime(i) and isPrime(int(str(i)[::-1])):
                if (len(str(i)) > 2 and i != int(str(i)[::-1])):
                    prime_no.append(i)
                elif len(str(i)) < 3:
                    prime_no.append(i)

        print(prime_no)
        result.append(len(prime_no))
        
        result.append(max(prime_no))

        result.append(sum(prime_no))
        
        return result

    else:
        return [0,0,0]

print(find_emirp(200))