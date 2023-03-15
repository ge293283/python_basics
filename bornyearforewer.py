# Module 4

# А.С. Пушкин
yearOfBirth_Pushkin = input("Введите год рождения А.С. Пушкина (например: 1900): ")
while yearOfBirth_Pushkin != "1799":
    print("Неверно")
    yearOfBirth_Pushkin = input("Введите год рождения А.С. Пушкина (например: 1900): ")
print("Верно\n")

# М.А. Булгаков
while True:
    yearOfBirth_Bulgakov = input("Введите год рождения М.А. Булгакова (например: 1900): ")
    if yearOfBirth_Bulgakov == "1891":
        print("Верно")
        break
    else:
        print("Неверно")