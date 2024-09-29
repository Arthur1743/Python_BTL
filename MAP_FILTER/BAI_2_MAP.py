def celsius_sang_fahrenheit(celsius):
    return celsius * 9/5 + 32
# Danh sách nhiệt độ Celsius
celsius_temperatures = [0, 20, 37, 100]
# Sử dụng map để chuyển đổi sang Fahrenheit
fahrenheit_temperatures = list(map(celsius_sang_fahrenheit, celsius_temperatures))
# In danh sách nhiệt độ Fahrenheit
print(f"Nhiệt độ Fahrenheit: {fahrenheit_temperatures}")