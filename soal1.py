#Create a function that converts temperature from Celsius to Fahrenheit and vice versa. 
#The function accepts two parameters, namely the temperature value and the temperature unit ('C' for Celsius, 'F' for Fahrenheit).

def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        print("Unit harus 'C' atau 'F' ")

print("======== KONVERSI SUHU ========")

input_suhu = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan satuan suhu ('C' untuk Celcius atau 'F' untuk Fahrenheit): ")
konversi = convert_temperature(input_suhu, unit)
