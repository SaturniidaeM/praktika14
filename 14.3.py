import tkinter as tk
from tkinter import messagebox

class IceCreamStand:
    def __init__(self, root):
        self.root = root
        self.root.title("Кафе-мороженое")
        self.root.geometry("650x550")
        self.root.configure(bg="#d3d3d3")

        self.flavors = ["Вишнёвое", "Шоколадное", "Клубничное"]
        self.types = ["На палочке", "Мягкое"]

        self.create_widgets()

    def create_widgets(self):
        leftframe = tk.Frame(self.root, bg="#d3d3d3")
        leftframe.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH, expand=True)

        tk.Label(leftframe, text="Сорта мороженого (вкусы)", font=("Arial", 12, "bold"), bg="#d3d3d3", fg="#2c2c2c").pack(pady=5)

        self.listbox_flavors = tk.Listbox(leftframe, height=8, width=25, bg="#f0f0f0", fg="#1a1a1a", font=("Arial", 10))
        self.listbox_flavors.pack(pady=5, fill=tk.BOTH, expand=True)
        for f in self.flavors:
            self.listbox_flavors.insert(tk.END, f)
        btn_add = tk.Button(leftframe, text="Добавить", command=self.add_flavor, bg="#a9a9a9", fg="white", font=("Arial", 10, "bold"))
        btn_add.pack(pady=2, fill=tk.X)
        btn_remove = tk.Button(leftframe, text="Удалить", command=self.remove_flavor, bg="#a9a9a9", fg="white", font=("Arial", 10, "bold"))
        btn_remove.pack(pady=2, fill=tk.X)
        btn_check = tk.Button(leftframe, text="Проверить", command=self.check_flavor, bg="#a9a9a9", fg="white", font=("Arial", 10, "bold"))
        btn_check.pack(pady=2, fill=tk.X)
        rightframe = tk.Frame(self.root, bg="#d3d3d3")
        rightframe.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)
        tk.Label(rightframe, text="Типы мороженого", font=("Arial", 12, "bold"), bg="#d3d3d3", fg="#2c2c2c").pack(pady=5)
        self.listbox_types = tk.Listbox(rightframe, height=8, width=25, bg="#f0f0f0", fg="#1a1a1a", font=("Arial", 10))
        self.listbox_types.pack(pady=5, fill=tk.BOTH, expand=True)
        for t in self.types:
            self.listbox_types.insert(tk.END, t)
        btn_addtype = tk.Button(rightframe, text="Добавить тип", command=self.add_type, bg="#a9a9a9", fg="white", font=("Arial", 10, "bold"))
        btn_addtype.pack(pady=2, fill=tk.X)
        btn_removetype = tk.Button(rightframe, text="Удалить тип", command=self.remove_type, bg="#a9a9a9", fg="white", font=("Arial", 10, "bold"))
        btn_removetype.pack(pady=2, fill=tk.X)
        btn_listtypes = tk.Button(rightframe, text="Список типов", command=self.show_types, bg="#a9a9a9", fg="white", font=("Arial", 10, "bold"))
        btn_listtypes.pack(pady=2, fill=tk.X)
        bottomframe = tk.Frame(self.root, bg="#d3d3d3")
        bottomframe.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
        tk.Label(bottomframe, text="Название:", font=("Arial", 11), bg="#d3d3d3", fg="#2c2c2c").pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(bottomframe, width=20, font=("Arial", 11), bg="#f0f0f0", fg="#1a1a1a")
        self.name_entry.pack(side=tk.LEFT, padx=5)
        btn_ready = tk.Button(bottomframe, text="Готово", command=self.ready, bg="#696969", fg="white", font=("Arial", 10, "bold"))
        btn_ready.pack(side=tk.LEFT, padx=10)
        btn_info = tk.Button(bottomframe, text="Повысить информацию", command=self.show_info, bg="#808080", fg="white", font=("Arial", 9, "bold"))
        btn_info.pack(side=tk.RIGHT, padx=10)

    def add_flavor(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавить сорт")
        dialog.geometry("300x120")
        dialog.configure(bg="#d3d3d3")
        tk.Label(dialog, text="Название вкуса:", bg="#d3d3d3", fg="#2c2c2c").pack(pady=10)
        entry = tk.Entry(dialog, width=25, bg="#f0f0f0")
        entry.pack(pady=5)
        def save():
            new = entry.get().strip()
            if new and new not in self.flavors:
                self.flavors.append(new)
                self.listbox_flavors.insert(tk.END, new)
                dialog.destroy()
            elif new in self.flavors:
                messagebox.showwarning("Ошибка", "Такой вкус уже есть")
            else:
                messagebox.showwarning("Ошибка", "Введите название")
        tk.Button(dialog, text="Добавить", command=save, bg="#a9a9a9", fg="white").pack(pady=5)

    def remove_flavor(self):
        sel = self.listbox_flavors.curselection()
        if sel:
            index = sel[0]
            self.flavors.pop(index)
            self.listbox_flavors.delete(index)
        else:
            messagebox.showwarning("Ошибка", "Выберите вкус для удаления")

    def check_flavor(self):
        sel = self.listbox_flavors.curselection()
        if sel:
            flavor = self.flavors[sel[0]]
            messagebox.showinfo("Проверка", f"Сорт '{flavor}' есть в меню")
        else:
            messagebox.showwarning("Ошибка", "Выберите сорт")

    def add_type(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавить тип")
        dialog.geometry("300x120")
        dialog.configure(bg="#d3d3d3")
        tk.Label(dialog, text="Название типа:", bg="#d3d3d3", fg="#2c2c2c").pack(pady=10)
        entry = tk.Entry(dialog, width=25, bg="#f0f0f0")
        entry.pack(pady=5)
        def save():
            new = entry.get().strip()
            if new and new not in self.types:
                self.types.append(new)
                self.listbox_types.insert(tk.END, new)
                dialog.destroy()
            elif new in self.types:
                messagebox.showwarning("Ошибка", "Такой тип уже есть")
            else:
                messagebox.showwarning("Ошибка", "Введите название")
        tk.Button(dialog, text="Добавить", command=save, bg="#a9a9a9", fg="white").pack(pady=5)

    def remove_type(self):
        sel = self.listbox_types.curselection()
        if sel:
            index = sel[0]
            self.types.pop(index)
            self.listbox_types.delete(index)
        else:
            messagebox.showwarning("Ошибка", "Выберите тип для удаления")

    def show_types(self):
        if self.types:
            msg = "Типы мороженого:\n" + "\n".join(f"- {t}" for t in self.types)
        else:
            msg = "Список типов пуст"
        messagebox.showinfo("Список типов", msg)

    def ready(self):
        name = self.name_entry.get().strip()
        if name:
            messagebox.showinfo("Готово", f"Ваше мороженое \"{name}\" готовится!")
        else:
            messagebox.showwarning("Ошибка", "Введите название мороженого")

    def show_info(self):
        info = (f"В нашем кафе представлены сорта: {', '.join(self.flavors)}\n"
                f"Типы: {', '.join(self.types)}\n"
                f"Приятного аппетита!")
        messagebox.showinfo("Информация о кафе", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamStand(root)
    root.mainloop()
