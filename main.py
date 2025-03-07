import tkinter as tk
from tkinter import messagebox


def search_files():
    query = entry.get()
    # Здесь должна быть ваша функция поиска, например, results = search(query)
    results = ["file1.txt", "file2.txt"]  # Пример результатов
    listbox.delete(0, tk.END)  # Очищаем список
    if results:
        for file in results:
            listbox.insert(tk.END, file)  # Добавляем результаты
    else:
        messagebox.showinfo("Результат", "Ничего не найдено.")


root = tk.Tk()
root.title("Foogle")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Поиск", command=search_files)
button.pack()

listbox = tk.Listbox(root, width=100, height=20)
listbox.pack(pady=10)

root.mainloop()