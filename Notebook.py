import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font as tkfont
from tkinter import ttk
import builtins
from datetime import datetime

# Создаём окно
root = tk.Tk()
root.title('Блокнот')
root.geometry('1000x600')
root.iconbitmap('icon.ico')

# Глобальные переменные
search_text = ""
search_indices = []
current_match = -1
current_zoom = 0

# Сторонние функции
# Функция для автоматического переключения с вкладки "+"
def check_plus_tab(event):
    selected_index = notebook.index(notebook.select())
    if notebook.tab(selected_index, "text") == "+":
        # Переключаем на последнюю реальную вкладку (перед "+")
        last_real_index = notebook.index("end") - 2
        if last_real_index >= 0:
            notebook.select(last_real_index)

# Привязываем проверку к событию смены вкладки
root.bind("<<NotebookTabChanged>>", check_plus_tab)

# Функции menubar
# file_menu function
def new_tab():
    # Создаем новую вкладку перед вкладкой "+"
    new_tab_frame = ttk.Frame(notebook)
    notebook.insert(notebook.index("end") - 1, new_tab_frame, text="Без имени")

    # Создаем текстовое поле для новой вкладки
    new_text_area = tk.Text(new_tab_frame, wrap=tk.WORD, font=("Arial", 11), width=80, height=25)
    new_text_area.pack(fill=tk.BOTH, expand=True)

    # Указываем, что файл пока не сохранён
    new_tab_frame.file_path = None

    # Переключаемся на новую вкладку
    notebook.select(new_tab_frame)

def close_tab():
    cur_id = notebook.select()
    if not cur_id:
        return
    if notebook.tab(cur_id, "text") == "+":
        return
    notebook.forget(cur_id)


def close_last_tab():
    last_index = notebook.index("end") - 2
    if last_index >= 0:
        notebook.forget(last_index)

def open_file():
    file_path = filedialog.askopenfilename(
        title="Открыть файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )

    if file_path:
        try:
            with builtins.open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            current_tab = notebook.nametowidget(notebook.select())

            # Проверяем, что это не вкладка "+"
            if notebook.tab(current_tab, "text") == "+":
                messagebox.showwarning("Внимание", "Невозможно открыть файл на вкладке '+'")
                return

            text_area = current_tab.winfo_children()[0]
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, content)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {str(e)}")

def save():
    current_tab = notebook.nametowidget(notebook.select())

    # Получаем текстовое поле
    text_area = current_tab.winfo_children()[0]

    # Проверяем, есть ли уже путь к файлу
    if hasattr(current_tab, "file_path") and current_tab.file_path:
        try:
            with open(current_tab.file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")
    else:
        # Если файла нет, вызываем save_as
        save_as()
        # После save_as() сохраняем путь к файлу в вкладке
        if hasattr(current_tab, "file_path") is False:
            current_tab.file_path = None

def save_as():
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        title="Сохранить как"
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_area.get(1.0, tk.END))
            # Сохраняем путь к файлу в текущей вкладке
            current_tab.file_path = file_path
            notebook.tab(current_tab, text=file_path.split("/")[-1])
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")

def save_all():
    for i in range(notebook.index("end")):
        tab = notebook.nametowidget(notebook.tabs()[i])
        tab_text = notebook.tab(tab, "text")

        # Пропускаем вкладку "+"
        if tab_text == "+":
            continue

        text_area = tab.winfo_children()[0]  # Получаем текстовое поле

        # Если вкладка уже имеет путь к файлу, сохраняем напрямую
        if hasattr(tab, "file_path") and tab.file_path:
            try:
                with open(tab.file_path, "w", encoding="utf-8") as file:
                    file.write(text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл '{tab_text}': {str(e)}")
        else:
            # Если файла нет, вызываем save_as для каждой вкладки
            notebook.select(tab)
            save_as()

def exit_window():
    root.destroy()

# edit_menu function
def cancel():
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    try:
        text_area.edit_undo()
    except tk.TclError:
        messagebox.showinfo("Отмена", "Нет действий для отмены.")

def cut():
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    # Копируем выделенный текст в буфер обмена
    selected_text = text_area.selection_get()
    root.clipboard_clear()
    root.clipboard_append(selected_text)

    # Удаляем выделенный текст из поля
    text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

def copy():
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    selected_text = text_area.selection_get()
    root.clipboard_clear()
    root.clipboard_append(selected_text)

def paste():
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    clipboard_text = root.clipboard_get()
    text_area.insert(tk.INSERT, clipboard_text)

def delete():
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

def find():
    global search_text, search_indices, current_match
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    # Диалог для ввода искомого текста
    search_text = simpledialog.askstring("Поиск", "Введите текст для поиска:")

    if not search_text:
        return

    # Удаляем прошлые выделения
    text_area.tag_remove("search_highlight", "1.0", tk.END)

    start_pos = "1.0"
    search_indices = []

    # Ищем все совпадения
    while True:
        start_pos = text_area.search(search_text, start_pos, stopindex=tk.END)
        if not start_pos:
            break
        end_pos = f"{start_pos}+{len(search_text)}c"
        search_indices.append((start_pos, end_pos))
        text_area.tag_add("search_highlight", start_pos, end_pos)
        start_pos = end_pos

    # Настраиваем выделение
    text_area.tag_config("search_highlight", background="yellow", foreground="black")

    if not search_indices:
        messagebox.showinfo("Поиск", "Совпадений не найдено.")
        return

    current_match = 0
    text_area.mark_set(tk.INSERT, search_indices[current_match][0])
    text_area.see(search_indices[current_match][0])


def find_next():
    global current_match, search_indices
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    if not search_indices:
        return

    current_match = (current_match + 1) % len(search_indices)
    start, end = search_indices[current_match]
    text_area.mark_set(tk.INSERT, start)
    text_area.see(start)
    text_area.tag_remove("active_highlight", "1.0", tk.END)
    text_area.tag_add("active_highlight", start, end)
    text_area.tag_config("active_highlight", background="orange", foreground="black")


def find_prev():
    global current_match, search_indices
    current_tab = notebook.nametowidget(notebook.select())

    text_area = current_tab.winfo_children()[0]

    if not search_indices:
        return

    current_match = (current_match - 1) % len(search_indices)
    start, end = search_indices[current_match]
    text_area.mark_set(tk.INSERT, start)
    text_area.see(start)
    text_area.tag_remove("active_highlight", "1.0", tk.END)
    text_area.tag_add("active_highlight", start, end)
    text_area.tag_config("active_highlight", background="orange", foreground="black")

def replace():
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    find_text = simpledialog.askstring("Замена", "Что заменить:")
    replace_text = simpledialog.askstring("Замена", "На что заменить:")
    if find_text:
        content = text_area.get(1.0, tk.END)
        new_content = content.replace(find_text, replace_text)
        text_area.delete(1.0, tk.END)
        text_area.insert(1.0, new_content)

def go_to():
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    line = simpledialog.askinteger("Перейти к строке", "Введите номер строки:")
    if line:
        text_area.mark_set(tk.INSERT, f"{line}.0")
        text_area.see(f"{line}.0")

def select_all():
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    text_area.tag_add(tk.SEL, "1.0", tk.END)
    text_area.mark_set(tk.INSERT, "1.0")
    text_area.see(tk.INSERT)

def time_date():
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    now = datetime.now().strftime("%H:%M %d.%m.%Y")
    text_area.insert(tk.INSERT, now)

def font():
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    font_name = simpledialog.askstring("Шрифт", "Введите название шрифта (например, Arial):")
    font_size = simpledialog.askinteger("Размер", "Введите размер шрифта:")
    if font_name and font_size:
        text_area.config(font=(font_name, font_size))

# view_menu function
def zoom_in():
    global current_zoom
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    current_zoom += 2
    current_font = tkfont.Font(font=text_area['font'])
    text_area.config(font=(current_font.actual('family'), current_font.actual('size') + 2))

def zoom_out():
    global current_zoom
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    current_zoom -= 2
    current_font = tkfont.Font(font=text_area['font'])
    text_area.config(font=(current_font.actual('family'), max(6, current_font.actual('size') - 2)))

def restore_zoom():
    current_tab = notebook.nametowidget(notebook.select())
    text_area = current_tab.winfo_children()[0]
    text_area.config(font=("Arial", 11))

# Создаём menubar
main_menu = tk.Menu(root)

# file_menu
file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label='New tab', command=new_tab)
file_menu.add_command(label='Сlose the tab', command=close_tab)
file_menu.add_command(label='Сlose the last tab', command=close_last_tab)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Save all", command=save_all)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_window)

# edit_menu
edit_menu = tk.Menu(tearoff=0)
edit_menu.add_command(label="Cancel", command=cancel)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Delete", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Find", command=find)
edit_menu.add_command(label="Find next", command=find_next)
edit_menu.add_command(label="Find previous", command=find_prev)
edit_menu.add_command(label="Replace", command=replace)
edit_menu.add_command(label="Go to", command=go_to)
edit_menu.add_separator()
edit_menu.add_command(label="Select all", command=select_all)
edit_menu.add_command(label="Time & Date", command=time_date)
edit_menu.add_separator()
edit_menu.add_command(label="Font", command=font)

# zoom_menu in view_menu
zoom_menu = tk.Menu(tearoff=0)
zoom_menu.add_command(label="Zoom in", command=zoom_in)
zoom_menu.add_command(label="Zoom out", command=zoom_out)
zoom_menu.add_command(label="Restore default zoom", command=restore_zoom)

# view_menu
view_menu = tk.Menu(tearoff=0)
view_menu.add_cascade(label="Zoom", menu=zoom_menu)

# menu
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="View", menu=view_menu)

root.config(menu=main_menu)


# Создаем notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Создаем первую вкладку с текстовым полем
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Без имени")

# Создаем текстовое поле
text_area = tk.Text(tab1, wrap=tk.WORD, font=("Arial", 11), width=80, height=25, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

# Добавляем вкладку "+"
plus_tab = ttk.Frame(notebook)
notebook.add(plus_tab, text="+")

# Функция для создания новой вкладки при клике на "+"
def click_tab(event):
    x, y = event.x, event.y
    index = notebook.index(f"@{x},{y}")
    if notebook.tab(index, "text") == "+":
        new_tab()
        return "break"

notebook.bind("<Button-1>", click_tab)

# сочетания клавиш
# file
root.bind("<Control-n>", lambda e: new_tab())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save())
root.bind("<Control-Shift-S>", lambda e: save_as())
root.bind("<Control-Alt-s>", lambda e: save_all())
root.bind("<Control-w>", lambda e: close_tab())

# edit
root.bind("<Control-z>", lambda e: cancel())
root.bind("<Control-x>", lambda e: cut())
root.bind("<Control-c>", lambda e: copy())
root.bind("<Control-v>", lambda e: paste())
root.bind("<Delete>", lambda e: delete())
root.bind("<Control-f>", lambda e: find())
root.bind("<F3>", lambda e: find_next())
root.bind("<Shift-F3>", lambda e: find_prev())
root.bind("<Control-h>", lambda e: replace())
root.bind("<Control-g>", lambda e: go_to())
root.bind("<Control-a>", lambda e: select_all())
root.bind("<Control-t>", lambda e: time_date())

# view
root.bind("<Control-plus>", lambda e: zoom_in())
root.bind("<Control-KP_Add>", lambda e: zoom_in())

root.bind("<Control-minus>", lambda e: zoom_out())
root.bind("<Control-KP_Subtract>", lambda e: zoom_out())

root.bind("<Control-0>", lambda e: restore_zoom())
root.bind("<Control-KP_0>", lambda e: restore_zoom())

root.mainloop()