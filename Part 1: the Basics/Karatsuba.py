if __name__ == '__main__':

    def Karatsuba(x, y):
        n = len(str(x))
        x_string = str(x)
        y_string = str(y)
        if n == 1:
            return x * y
        else:
            a = x_string[:int(n / 2)]
            b = x_string[int(n / 2):]
            c = y_string[:int(n / 2)]
            d = y_string[int(n / 2):]
            p = int(a) + int(b)
            q = int(c) + int(d)
            ac = Karatsuba(int(a), int(c))
            bd = Karatsuba(int(b), int(d))
            pq = Karatsuba(int(p), int(q))

        adbc = pq - ac - bd
        step1 = 10**n * ac
        step2 = 10**(n/2) * (adbc)
        step3 = bd
        result = step1 + step2 + step3
        return int(result)

print(Karatsuba(1234, 4321))
