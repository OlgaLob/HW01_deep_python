# Программа загадывает число от 0 до 1000. Необходимо угадать число за
# 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой
# попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT_TRY = 10

enigmatic_number = randint(LOWER_LIMIT, UPPER_LIMIT + 1)

for i in range(1, COUNT_TRY + 1):
    number = (UPPER_LIMIT + LOWER_LIMIT) // 2

    if number > enigmatic_number:
        UPPER_LIMIT = number
        i += 1
    elif number < enigmatic_number:
        LOWER_LIMIT = number
        i += 1
    else:
        print(f"Вы победили с {i} попытки! Загаданное число {number}")
        break