import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import random


def generate_file():
    """Создает новый текстовый файл с заданным количеством случайных чисел."""
    try:
        count = int(number_entry.get())
        filepath = filedialog.asksaveasfilename(defaultextension=".txt")
        if filepath:
            with open(filepath, "w") as file:
                for _ in range(count):
                    file.write(str(random.randint(1, 100)) + "\n")
            messagebox.showinfo("Успех", f"Файл '{filepath}' создан с {count} случайных чисел.")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


def read_and_calculate(filepath):
    """Читает текстовый файл с числами, вычисляет среднее и выводит результат."""
    try:
        with open(filepath, "r") as file:
            numbers = [int(line) for line in file]
            avg = sum(numbers) / len(numbers)
            result_text = f"Содержимое файла:\n" + "\n".join(
                str(num) for num in numbers) + f"\n\nСреднее значение: {avg:.2f}"
            result_label.config(text=result_text)
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


def calculate(op):
    """ Математическая операция над двумя числами."""
    try:
        num1 = float(a_value.get())
        num2 = float(b_value.get())
        if op == "Сложение":
            result = num1 + num2
        elif op == "Умножение":
            result = num1 * num2
        result_label.config(text=f"Результат: {result}")
    except ValueError as e:
        messagebox.showerror("Ошибка", f"Некорректный ввод: {e}")


def read_file():
    """Открывает диалоговое окно для выбора файла и вычисляет среднее значние."""
    filepath = filedialog.askopenfilename(defaultextension=".txt")
    if filepath:
        read_and_calculate(filepath)


def addition():
    calculate("Сложение")


def multiply():
    calculate("Умножение")



root = tk.Tk()
root.title("Обработка данных")
root.geometry("350x600")

style = ttk.Style()
style.configure("TButton", padding=5, font=("Arial", 12), background="#FFFFFF")

result_frame = ttk.LabelFrame(text="Результат")
result_label = ttk.Label(result_frame, text="", wraplength=300)
result_label.pack(pady=10)
result_frame.grid(row=20, column=0, columnspan=2, sticky="nsew")

number_label = ttk.Label(text="Кол-во случайных чисел:", font=("Arial", 12))
number_label.grid(row=0, column=0, padx=5, pady=5)
number_entry = ttk.Entry(width=20)
number_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = ttk.Button(text="Создание файла", command=generate_file, style="TButton")
generate_button.grid(row=1, column=0, columnspan=1, pady=5, sticky="ew")

read_button = ttk.Button(text="Открыть файл", command=read_file, style="TButton")
read_button.grid(row=1, column=1, columnspan=1, pady=5, sticky="ew")

number_value = ttk.Label(text="Введите два числа для операций:", font=("Arial", 12))
number_value.grid(row=2, column=0, columnspan=2, pady=5)

a_value = ttk.Entry(width=20)
a_value.grid(row=3, column=0, padx=5, pady=5)
b_value = ttk.Entry(width=20)
b_value.grid(row=3, column=1, padx=5, pady=5)

addition_button = ttk.Button(text="Сложение", command=addition, style="TButton")
addition_button.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")
multiply_button = ttk.Button(text="Умножение", command=multiply, style="TButton")
multiply_button.grid(row=6, column=0, columnspan=2, pady=5, sticky="ew")


root.mainloop()