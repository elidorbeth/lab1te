import math
import tkinter as tk
from tkinter import messagebox


def count_ordered_sequences(n, base=10):
    """
    Повертає кількість впорядкованих послідовностей довжиною n
    (не спадних + не зростних - усі однакові) та загальну кількість.

    :param n: Довжина послідовності (кількість елементів).
    :param base: Кількість можливих «цифр» (за замовчуванням 10: 0..9).
    :return: (ordered, total) - кількість впорядкованих, загальна кількість.
    """
    # Кількість не спадних (через комбінації з повтореннями):
    # C(base + n - 1, n)
    non_decreasing = math.comb(base + n - 1, n)

    # Кількість не зростних:
    # така ж сама формула, симетрично
    non_increasing = math.comb(base + n - 1, n)

    # Послідовності, де всі елементи однакові (щоб не рахувати двічі):
    all_equal = base

    # Кількість впорядкованих (принцип включень-виключень)
    ordered = non_decreasing + non_increasing - all_equal

    # Загальна кількість усіх можливих послідовностей
    total = base ** n

    return ordered, total


def compute_probability():
    """
    Зчитує n з поля введення, рахує кількість впорядкованих послідовностей,
    загальну кількість і ймовірність, а тоді виводить результати на екран.
    """
    try:
        # Зчитуємо введене користувачем значення n
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("n має бути додатнім цілим числом!")

        ordered, total = count_ordered_sequences(n)
        prob = ordered / total

        # Формуємо текст для відображення
        result_text = (
            f"Кількість впорядкованих: {ordered}\n"
            f"Загальна кількість: {total}\n"
            f"Ймовірність: {prob:.4f} "
            f"({prob * 100:.2f}%)"
        )

        # Виводимо результат у відповідну мітку
        label_result.config(text=result_text)
    except ValueError:
        # Якщо користувач ввів щось некоректне (не число або число <= 0),
        # показуємо діалогове вікно з помилкою.
        messagebox.showerror("Помилка", "Будь ласка, введіть додатне ціле число!")


# Створюємо головне вікно
root = tk.Tk()
root.title("Ймовірність впорядкованої послідовності")

# Мітка з інструкцією
label_instruction = tk.Label(root, text="Введіть кількість елементів у послідовності (n):")
label_instruction.pack(pady=5)

# Поле введення для n
entry_n = tk.Entry(root)
entry_n.pack(pady=5)

# Кнопка "Обчислити"
button_compute = tk.Button(root, text="Обчислити", command=compute_probability)
button_compute.pack(pady=5)

# Мітка для відображення результату
label_result = tk.Label(root, text="", justify=tk.LEFT)
label_result.pack(pady=10)

# Запуск головного циклу подій
root.mainloop()