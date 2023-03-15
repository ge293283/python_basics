# Module 3

yearOfBirth = input("Введите год рождения А.С. Пушкина (например: 1900): ")
if yearOfBirth == "1799":
    dayOfBirth = input("Введите день рождения А.С. Пушкина (например: 01.01): ")
    if dayOfBirth == "26.05" or dayOfBirth == "06.06":  # The date can be entered according to the old style or the new one
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")