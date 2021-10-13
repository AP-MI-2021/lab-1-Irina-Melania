# 1. Sa se stabilieasca daca un numar n este prim
def verify_if_prime(n):
    if n <= 1:
        return 0

    if n == 2:
        return 1

    if n % 2 == 0:
        return 0

    for i in range(3, n // 2, 2):
        if n % i == 0:
            return 0

    return 1


# 2. Sa se calculeze produsul a n numere naturale
def product(numbers):
    p = 1

    for number in numbers:
        p *= number

    return p


# 3. CMMDC a doua numere
def cmmdc_first(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


def cmmdc_second(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def menu():
    return "1. Verifica daca un numar este prim\n" \
           "2. Calculeaza produsul a n numere naturale\n" \
           "3. CMMDC a doua numere prin doua metode diferite\n" \
           "0. Stop\n"


def main():
    ok = 1

    while ok:
        print(menu())
        choice = int(input(">>> "))

        if choice == 1:
            n = int(input("n = "))
            prime = verify_if_prime(n)

            if prime == 1:
                print("Numarul este prim\n")
            else:
                print("Numarul nu este prim\n")

        elif choice == 2:
            n = int(input("n = "))
            numbers = []

            print("numerele: ")
            for i in range(n):
                a = int(input())
                numbers.append(a)

            print("Produsul este: ", product(numbers), "\n")

        elif choice == 3:
            a = int(input("a = "))
            b = int(input("b = "))
            print("CMMDC #1: ", cmmdc_first(a, b), "\n")
            print("CMMDC #2: ", cmmdc_second(a, b), "\n")

        else:
            ok = 0

main()