# Module 5

while True:
    yearOfBirth = input("Введите год рождения А.С. Пушкина (например: 1900): ")
    if yearOfBirth == "1799":
        print()
        break
    else:
        print("Неверный год рождения")

while True:
    dayOfBirth = input("Введите день рождения А.С. Пушкина (например: 01.01): ")
    if dayOfBirth == "26.05" or dayOfBirth == "06.06":
        break
    else:
        print("Неверный день рождения")