import sys
print sys.argv
def input (a):
  print type(a)
  i = int(a[1])
  print type(i)
  b=1+i
  return b
print input(sys.argv)

