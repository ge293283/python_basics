# Module 5

# We ask for the year of birth and check until the correct answer is entered, if ok - go to the next cycle
while True:
    yearOfBirth = input("Введите год рождения А.С. Пушкина (например: 1900): ")
    if yearOfBirth == "1799":
        print()
        break
    else:
        print("Неверный год рождения")

# We request and check the date of birth, if ok - exit the loop and end the program
while True:
    dayOfBirth = input("Введите день рождения А.С. Пушкина (например: 01.01): ")
    if dayOfBirth == "26.05" or dayOfBirth == "06.06": # The date can be entered according to the old style or the new one
        break
    else:
        print("Неверный день рождения")