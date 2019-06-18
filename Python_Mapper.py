class Sample:
  a = ""
  b = ""
  c = ""
  d = ""
  e = ""
c = []
n = int(input("Enter num of objects\n"))
for i in range(n):
  c.append(Sample())
for i in range(n):
  c[i].a = input("Enter value for a\n")
  c[i].b = input("Enter value for b\n")
  c[i].c = input("Enter value for c\n")
  c[i].d = input("Enter value for d\n")
  c[i].e = input("Enter value for e\n")
mapper  = {}
for i in range(n):
  mapper[str(i)] = c[i]
ser_str = input("Enter Search String\n")
for key,value in mapper.items():
  if(value.c == ser_str):
    print(key)
