if __name__ == '__main__':
    def RecurIntMult(x, y):
        n = len(str(x))
        x_string = str(x)
        y_string = str(y)
        if n == 1:
            return x * y
        else:
            a = x_string[:int(n/2)]
            b = x_string[int(n/2):]
            c = y_string[:int(n/2)]
            d = y_string[int(n/2):]
            ac = RecurIntMult(int(a), int(c))
            ad = RecurIntMult(int(a), int(d))
            bc = RecurIntMult(int(b), int(c))
            bd = RecurIntMult(int(b), int(d))

        step1 = 10**n * ac
        step2 = 10**(n/2) * (ad+bc)
        step3 = bd
        result = step1 + step2 + step3
        return int(result)

print(RecurIntMult(5678, 1234))

