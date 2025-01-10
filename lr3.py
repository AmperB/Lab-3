import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

# Генерация ключа по указанным правилам
def generate_key():
    input_number = entry.get()
    # Проверка на то, что введено шестизначное число
    if not input_number.isdigit() or len(input_number) != 6:
        messagebox.showerror("Ошибка", "Введите шестизначное число.")
        return

    # Выделение цифр для формата ключа
    block1_digits = input_number[3:6]  # 4, 5, 6 цифры
    block2_digits = input_number[0:3]  # 1, 2, 3 цифры

    # Генерация случайных букв
    letters1 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    letters2 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))

    # Подсчет суммы цифр в блоках 1 и 2
    sum_block = sum(int(digit) for digit in block1_digits + block2_digits)

    # Форматирование ключа
    generated_key = f"{block1_digits}{letters1}-{block2_digits}{letters2}-{sum_block:04d}"
    
    # Отображение сгенерированного ключа
    result_label.config(text=f"Сгенерированный ключ: {generated_key}")

# Инициализация окна Tkinter
root = tk.Tk()
root.title("Keygen")  # Заголовок окна
root.geometry("400x300")  # Размер окна

# Добавление фонового изображения
background_image = Image.open("aoe2.png")
background_image = background_image.resize((400, 300), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Добавление надписи с инструкцией
instruction_label = tk.Label(root, text="Введите шестизначное число:", bg="white", font=("Arial", 12))
instruction_label.pack(pady=10)

# Поле для ввода пользователем числа
entry = tk.Entry(root, font=("Arial", 12), width=10)
entry.pack(pady=5)

# Кнопка для генерации ключа
generate_button = tk.Button(root, text="Генерировать ключ", command=generate_key, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

# Метка для отображения сгенерированного ключа
result_label = tk.Label(root, text="", bg="white", font=("Arial", 12))
result_label.pack(pady=10)

# Запуск основного цикла
root.mainloop()