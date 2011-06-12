def is_palindrome (num):
        s = str(num)
        l = len(s) / 2
        return s[:l] == s[-l:][::-1]


max = 0
for a in range(0,999)[::-1]:
        for b in range(0,999)[::-1]:
                if is_palindrome (a * b):
                        if a * b > max:
                                max = a * b

print max
