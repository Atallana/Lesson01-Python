# Создайте переменную
my_heigh = 170
print(my_heigh)


# Перезапишите переменную
my_name = "Татьяна"
my_name = "Татьяна Черкасова"
print(my_name)


# Получите пользовательский ввод
print("Как зовут вашего питомца? ")
pet_name = input()
print("Ваш любимчик - " + pet_name)


# Создание функции
def print_python():
    print("Учу Python!")


print_python()


# Параметризация функций
def print_letter(let):
    print(let, end='')


print_letter('С')
print_letter('т')
print_letter('у')
print_letter('д')
print_letter('е')
print_letter('н')
print_letter('т')
