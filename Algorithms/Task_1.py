m = int(input('Введите трехзначное чилсло '))

a = m // 100

b = m // 10 % 10

c = m % 10

summary = a + b + c
multiplication = a * b * c

print(f'{summary = }, \n{multiplication = }')

