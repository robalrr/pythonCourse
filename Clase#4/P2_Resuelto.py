import math
def Perimetro(n_vertices,long_lado):
 if(n_vertices<=2):
   print("No se puede realizar una figura con esa cantidad de vertices")
 else:
   result=n_vertices*long_lado

 return result

def main():
 n= int(input("Cantidad de vertices: "))
 t= int(input("Tamano del lado: "))
 perimeter = Perimetro(n,t)
 print("El perimetro es: ",perimeter)


if __name__ == '__main__':
 try:
  main()
 except KeyboardInterrupt:
  sys.exit(0)
