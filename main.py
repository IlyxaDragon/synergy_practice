def sum_negative_between_min_max(arr):
    """
    Находит сумму отрицательных элементов в одномерном массиве,
    расположенных между максимальным и минимальным элементами.

    Args:
        arr: Список (одномерный массив) чисел.

    Returns:
        Сумма отрицательных элементов между максимальным и минимальным.
        Возвращает 0, если массив слишком короткий или нет отрицательных чисел в диапазоне.
    """
    if not arr or len(arr) < 2:
        print("Массив слишком короткий для выполнения операции.")
        return 0

    # Шаг 2: Поиск максимального и минимального элементов и их индексов
    # Инициализируем max_val, min_val первым элементом
    max_val = arr[0]
    min_val = arr[0]
    max_index = 0
    min_index = 0

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
        # Важно: если есть несколько одинаковых минимальных элементов,
        # min_index будет указывать на первое вхождение.
        # Если нужно последнее, условие должно быть arr[i] <= min_val
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i

    print(f"Максимальный элемент: {max_val} (индекс: {max_index})")
    print(f"Минимальный элемент: {min_val} (индекс: {min_index})")

    # Шаг 3: Определение границ диапазона
    # Гарантируем, что start_index всегда меньше end_index для правильной итерации
    if min_index < max_index:
        start_index = min_index
        end_index = max_index
    else:
        start_index = max_index
        end_index = min_index

    # Если максимальный и минимальный элементы находятся в одном и том же индексе
    # (например, массив из одного элемента или все элементы одинаковы),
    # или если они стоят рядом друг с другом, между ними нет элементов.
    if end_index - start_index <= 1:
        print("Между максимальным и минимальным элементами нет других элементов.")
        return 0

    current_sum = 0
    print(f"Ищем отрицательные элементы в диапазоне индексов от {start_index + 1} до {end_index - 1}")

    # Шаг 4: Итерация и суммирование
    # Итерируемся от элемента *после* первого найденного до элемента *перед* вторым найденным.
    # То есть, если диапазон [min_index, max_index], мы рассматриваем arr[min_index+1] до arr[max_index-1]
    for i in range(start_index + 1, end_index):
        if arr[i] < 0:
            current_sum += arr[i]
            print(f"Найден отрицательный элемент: {arr[i]}. Текущая сумма: {current_sum}")

    # Шаг 5: Вывод результата
    return current_sum


# Здесь начинается основной блок программы
if __name__ == "__main__":
    print("--- Программа для поиска суммы отрицательных элементов между Min и Max ---")

    while True:
        try:
            n = int(input("Введите размерность массива (N), минимум 2: "))
            if n < 2:
                print("Размерность должна быть не менее 2. Пожалуйста, попробуйте снова.")
            else:
                break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    user_array = []
    print(f"Теперь введите {n} целых чисел для массива, нажимая Enter после каждого:")
    for i in range(n):
        while True:
            try:
                element = int(input(f"Элемент {i + 1}: "))
                user_array.append(element)
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")

    print(f"\nВаш введенный массив: {user_array}")

    final_result = sum_negative_between_min_max(user_array)
    print(f"\nИтоговая сумма отрицательных элементов между максимальным и минимальным: {final_result}")