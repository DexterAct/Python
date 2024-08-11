print("=====FAHRENHEIT KE KELVIN=====")

fahrenheit = float(input("Masukkan suhu fahrenheit:"))
print("suhu fahrenheit adalah",fahrenheit,"Fahrenheit")
kelvin = ((fahrenheit-32)*(5/9))+273.15
print("suhu kelvin adalah",kelvin,"Kelvin")

print("=====KELVIN KE FAHRENHEIT=====")

kelvin = float(input("Masukkan suhu kelvin:"))
print("Suhu kelvin adalah",kelvin,"Kelvin")
fahrenheit = (9/5*(kelvin-273))+32
print("Suhu fahrenheit adalah",fahrenheit,"Fahrenheit")