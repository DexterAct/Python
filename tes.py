#program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius :'))
print("Suhu adalah",celcius,"Celcius")

#reamur(4/5*C)
reamur = (4/5)*celcius
print("Suhu dalam reamur adalah",reamur,"reamur")

#fahrenheit
fahrenheit = ((9/5)*celcius)+32
print("Suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")

#kelvin
kelvin = celcius+273
print("Suhu dalam kelvin adalah",kelvin,"kelvin")