import random
import datetime

# Генерация случайного числа
secret_number = random.randint(1, 100)
attempts = 0
numbers_less = []
numbers_more = []


# Функция для записи в log.txt
def write_log(message):
    with open("log.txt", "a") as log_file:
        log_file.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] [INFO] {message}\n")


write_log("[System]: Загадано число")

# Основной цикл игры
while True:
    try:
        user_input = input("Угадайте число от 1 до 100 (или введите 'exit' для выхода): ")
        if user_input.lower() == 'exit':
            break
        guess = int(user_input)
        attempts += 1
        write_log(f"[User]: Введено число {guess}")

        if guess < secret_number:
            print("Загаданное число больше!")
            numbers_less.append(guess)
        elif guess > secret_number:
            print("Загаданное число меньше!")
            numbers_more.append(guess)
        else:
            print(f"Поздравляем, вы угадали число {secret_number} с {attempts} попыток!")
            write_log("[System]: Число угадано.")
            write_log(f"Попыток: {attempts}")
            break
    except ValueError:
        print("Пожалуйста, введите корректное число.")

# Вывод статистики по числам меньше и больше загаданного
print(f"Чисел меньше загаданного: {numbers_less}")
print(f"Чисел больше загаданного: {numbers_more}")
