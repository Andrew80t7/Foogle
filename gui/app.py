import tkinter as tk
from tkinter import messagebox
from core.indexer import Indexer
from core.search import SearchEngine
import threading
# from utils.threading import run_in_thread


class FoogleApp:
    def __init__(self, index_dir, docs_dir):
        self.root = tk.Tk()
        self.root.title("Foogle")
        self.indexer = Indexer(docs_dir)
        self.search_engine = None
        self.index_dir = index_dir

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)
        self.button = tk.Button(self.root, text="Поиск", command=self.search)
        self.button.pack()
        self.listbox = tk.Listbox(self.root, width=100, height=20)
        self.listbox.pack(pady=10)

        thread = threading.Thread(target=self.build_index())
        thread.start()

        # run_in_thread(self.build_index)

    def build_index(self):
        self.indexer.build()
        self.indexer.save(self.index_dir)
        self.search_engine = SearchEngine(self.indexer.index)
        messagebox.showinfo("Готово", "Индекс построен!")

    def search(self):
        query = self.entry.get()
        if self.search_engine:
            results = self.search_engine.search(query)
            self.listbox.delete(0, tk.END)
            for result in results:
                self.listbox.insert(tk.END, result)
        else:
            messagebox.showerror("Ошибка", "Индекс не загружен!")

    def run(self):
        self.root.mainloop()
