a=input("Enter the string")
b=' '
ch=' '
for i in range(len(a)):
  b+=str(ord(a[i])+3)
print(b)
for i in range(len(b)):
  ch+=chr(int(b[i]))
print(ch)  
