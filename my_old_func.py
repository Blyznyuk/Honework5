a = int(input("Введите сторону "))
b = int(input("Введите сторону "))
c = int(input("Введите сторону "))


def treygolnick(a, b, c):
    if a < b+c and b < a+c and c < a+b:
        if a == b == c:
            y = "Equilateral triangle"
            return y
        elif a==b or a==c or b==c:
            y = "Isosceles triangle"
            return y
        else:
            y = "Versatile triangle"
            return y
    else:
        y = "Not a triangle"
        return y


def triangle(a, b, c):
        if a < b + c and b < a + c and c < a + b:
            return True
        else:
            return False


def year():
    while True:
        try:
            a = int(input("Введите год    "))
        except ValueError:
            print("ne chislo")
        else:
            if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
                y = True
            else:
                y = False
            return y

print(treygolnick(a, b, c))

