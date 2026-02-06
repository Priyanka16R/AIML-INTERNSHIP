temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

first_reading=temperatures.index(22)
last_reading=temperatures[-1]
afternoon_peak=temperatures[3:6]
last3_hours=temperatures[-3:]
print("1st reading:",first_reading)
print("last reading",last_reading)
print("afternoon_peak:",afternoon_peak)
print("last 3 houers:",last3_hours)
