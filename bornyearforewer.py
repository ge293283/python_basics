# Module 4

yearOfBirth = input("Введите год рождения А.С. Пушкина (например: 1900): ")
while yearOfBirth != "1799":
    print("Неверно")
    yearOfBirth = input("Введите год рождения А.С. Пушкина (например: 1900): ")
print("Верно")

while True:
    yearOfBirth = input("Введите год рождения А.С. Пушкина (например: 1900): ")
    if yearOfBirth == "1799":
        print("Верно")
        break