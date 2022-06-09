for i in range(2):
    print("Hoala mundo")

try:
    v1 = 0
    v2 = 9
    divi = v2 / v1
    print(divi)
except ZeroDivisionError:
    print("la execcion generada es porque cero no es divisor")
