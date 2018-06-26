import math
def Function(Parameter_a,Parameter_b):
 n = Parameter_a+Parameter_b
 result = math.cos(n)
 return result

def main():
 a = 20
 b = 10
 r=Function(a,b)
 print(r)


if __name__ == '__main__':
 try:
  main()
 except KeyboardInterrupt:
  sys.exit(0)
