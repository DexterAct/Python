# Operasi Komparasi

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# Lebih dari >
print("=====LEBIH BESAR DARI (>)=====")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# Kurang dari <
print("=====KURANG DARI (<)=====")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# Lebih dari sama dengan >=
print("=====LEBIH DARI SAMA DENGAN (>=)=====")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# Kurang dari sama dengan >=
print("=====KURANG DARI SAMA DENGAN (<=)=====")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# Sama dengan ==
print("=====SAMA DENGAN (==)=====")
hasil= a == 4
print(a,'==',4,'=',hasil)
hasil= b == 4
print(b,'==',4,'=',hasil)

# Tidak sama dengan !=
print("=====TIDAK SAMA DENGAN (!=)=====")
hasil= a != 4
print(a,'!=',4,'=',hasil)
hasil= b != 4
print(b,'!=',4,'=',hasil)

print("=====OBJECT IDENTITY (is)=====")
# 'is' sebagai komparasi object identity
x = 5 #ini adalah assignment membuat object
y = 5
print('Nilai x =',x,',id = ',hex(id(x)))
print('Nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 #ini adalah assignment membuat object
y = 6
print('Nilai x =',x,',id = ',hex(id(x)))
print('Nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

print("=====OBJECT IDENTITY (is not)=====")
# 'is' sebagai komparasi object identity
x = 5 #ini adalah assignment membuat object
y = 5
print('Nilai x =',x,',id = ',hex(id(x)))
print('Nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5 #ini adalah assignment membuat object
y = 6
print('Nilai x =',x,',id = ',hex(id(x)))
print('Nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)
