import math
def desigualdad(lado_a,lado_b,lado_c):
 temp1 = lado_a+lado_b
 temp2 = lado_b+lado_c
 temp3 = lado_c+lado_a

 if(temp1>lado_c and temp2>lado_a and temp3 >lado_c):
   print("Es un triangulo")
   return True
 else:
   print("No es un triangulo")
   return False	
	
 return result

def main():
 a= int(input("Lado 1: "))
 b= int(input("Lado 2: "))
 c= int(input("Lado 3: "))
 desigualdad(a,b,c)


if __name__ == '__main__':
 try:
  main()
 except KeyboardInterrupt:
  sys.exit(0)
