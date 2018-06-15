import math

a = int(input("Digite el valor de a "))
b = int(input("Digite el valor de b "))
c = int(input("Digite el valor de c "))

disc = b ** 2 - (4 * a * c)
print("El valor del discriminante es: {}".format(disc))

if (disc == 0):
    x = -b / (2 * a)
    print("Solo hay una raíz: {}".format(x))

elif (disc > 0):
    x_uno = (-b + math.sqrt(disc)) / (2 * a)
    x_dos = (-b - disc**(1/2)) / (2 * a)
    print("Hay dos raíces: {}, {}".format(x_uno, x_dos))

else:
    print("No hay raíces")
