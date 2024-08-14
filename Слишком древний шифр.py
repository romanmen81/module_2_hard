def generate_password(n):
    result = ""

    # Перебираем все уникальные пары (i, j)
    for i in range(1, 21):
        for j in range(i + 1, 21):
            # Вычисляем сумму пары
            pair_sum = i + j
            # Проверяем кратность
            if n % pair_sum == 0:
                # Если кратно, добавляем число в результат в формате: i и j
                result += f"{i}{j}"

    return result

# Примеры использования
for n in range(3, 21):
    print(f"{n} - {generate_password(n)}")