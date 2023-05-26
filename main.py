# import tkinter as tk
# from tkinter import messagebox
# import psycopg2

# Функция для создания подключения к базе данных
# def create_connection():
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="libraryv2",
#             user="postgres",
#             password="witcher3"
#         )
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         print("Ошибка при подключении к базе данных:", error)

# Функция для регистрации студента
# def register_student():
#     registration_window = tk.Toplevel(window)
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()

    # Проверка наличия обязательных данных
    # if not student_id or not first_name or not last_name or not group_name:
    #     messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
    #     return

    # Проверка на уникальность ИИН
    #connection = create_connection()
    #if connection:
        #cursor = connection.cursor()
        #cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
        #existing_student = cursor.fetchone()
        #if existing_student:
            #messagebox.showerror("Ошибка", "Студент с таким ИИН уже зарегистрирован.")
            #cursor.close()
            #connection.close()
            #return

        # Регистрация студента в базе данных
        #cursor.execute("INSERT INTO students (id, first_name, last_name, group_name) VALUES (%s, %s, %s, %s)",
                       #(student_id, first_name, last_name, group_name))
        #connection.commit()
        #cursor.close()
        #connection.close()

        #messagebox.showinfo("Успех", "Студент успешно зарегистрирован.")
    #else:
        #messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")

# Функция для входа студента
#def login_student():
    # Получение введенных пользователем данных
    #student_id = id_entry.get()
    #first_name = first_name_entry.get()
    #last_name = last_name_entry.get()
    #group_name = group_entry.get()

    # Проверка наличия обязательных данных
    #if not student_id or not first_name or not last_name or not group_name:
        #messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        #return

    #connection = create_connection()
    #if connection:
        #cursor = connection.cursor()
        #cursor.execute("SELECT id FROM students WHERE id = %s AND first_name = %s AND last_name = %s AND group_name = %s",
                       # (student_id, first_name, last_name, group_name))
        #existing_student = cursor.fetchone()
        #cursor.close()
        #connection.close()

        #if existing_student:
            # messagebox.showinfo("Успех", "Студент успешно вошел в систему.")
        #else:
            #messagebox.showerror("Ошибка", "Неправильные данные.")
    #else:
        #messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")

# Создание графического интерфейса
#window = tk.Tk()
#window.title("Регистрация и вход для студентов")

# Создание и размещение элементов интерфейса
#id_label = tk.Label(window, text="ИИН:")
#id_label.pack()
#id_entry = tk.Entry(window)
#id_entry.pack()

#first_name_label = tk.Label(window, text="Имя:")
#first_name_label.pack()
#first_name_entry = tk.Entry(window)
#first_name_entry.pack()

#last_name_label = tk.Label(window, text="Фамилия:")
#last_name_label.pack()
#last_name_entry = tk.Entry(window)
#last_name_entry.pack()

#group_label = tk.Label(window, text="Название группы:")
#group_label.pack()
#group_entry = tk.Entry(window)
#group_entry.pack()

#register_button = tk.Button(window, text="Регистрация", command=register_student)
#register_button.pack()

#login_button = tk.Button(window, text="Вход", command=login_student)
#login_button.pack()

#window.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import psycopg2
#
# # Функция для создания подключения к базе данных
# def create_connection():
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="libraryv2",
#             user="postgres",
#             password="witcher3"
#         )
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         print("Ошибка при подключении к базе данных:", error)
#
# # Функция для регистрации студента
# def register_student():
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     # Проверка на уникальность ИИН
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
#         existing_student = cursor.fetchone()
#         if existing_student:
#             messagebox.showerror("Ошибка", "Студент с таким ИИН уже зарегистрирован.")
#             cursor.close()
#             connection.close()
#             return
#
#         # Регистрация студента в базе данных
#         cursor.execute("INSERT INTO students (id, first_name, last_name, group_name) VALUES (%s, %s, %s, %s)",
#                        (student_id, first_name, last_name, group_name))
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         messagebox.showinfo("Успех", "Студент успешно зарегистрирован.")
#         open_empty_window()
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
# # Функция для входа студента
# def login_student():
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s AND first_name = %s AND last_name = %s AND group_name = %s",
#                        (student_id, first_name, last_name, group_name))
#         existing_student = cursor.fetchone()
#         cursor.close()
#         connection.close()
#
#         if existing_student:
#             messagebox.showinfo("Успех", "Студент успешно вошел в систему.")
#             open_empty_window()
#         else:
#             messagebox.showerror("Ошибка", "Неправильные данные.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
# # Функция для открытия пустого окна
# def open_empty_window():
#     empty_window = tk.Toplevel(window)
#     empty_window.title("Пустое окно")
#     empty_label = tk.Label(empty_window, text="Пустое окно")
#     empty_label.pack()
#
# # Создание графического интерфейса
# window = tk.Tk()
# window.title("Регистрация и вход для студентов")
#
# # Создание и размещение элементов интерфейса
# id_label = tk.Label(window, text="ИИН:")
# id_label.pack()
# id_entry = tk.Entry(window)
# id_entry.pack()
#
# first_name_label = tk.Label(window, text="Имя:")
# first_name_label.pack()
# first_name_entry = tk.Entry(window)
# first_name_entry.pack()
#
# last_name_label = tk.Label(window, text="Фамилия:")
# last_name_label.pack()
# last_name_entry = tk.Entry(window)
# last_name_entry.pack()
#
# group_label = tk.Label(window, text="Название группы:")
# group_label.pack()
# group_entry = tk.Entry(window)
# group_entry.pack()
#
# register_button = tk.Button(window, text="Регистрация", command=register_student)
# register_button.pack()
#
# login_button = tk.Button(window, text="Вход", command=login_student)
# login_button.pack()
#
# window.mainloop()
# import tkinter as tk
# from tkinter import messagebox
# import psycopg2
#
# # Функция для создания подключения к базе данных
# def create_connection():
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="libraryv2",
#             user="postgres",
#             password="witcher3"
#         )
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         print("Ошибка при подключении к базе данных:", error)
#
# # Функция для закрытия окна с формами и открытия пустого окна
# def close_login_window():
#     login_window.destroy()
#     open_empty_window()
#
# # Функция для регистрации студента
# def register_student():
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     # Проверка на уникальность ИИН
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
#         existing_student = cursor.fetchone()
#         if existing_student:
#             messagebox.showerror("Ошибка", "Студент с таким ИИН уже зарегистрирован.")
#             cursor.close()
#             connection.close()
#             return
#
#         # Регистрация студента в базе данных
#         cursor.execute("INSERT INTO students (id, first_name, last_name, group_name) VALUES (%s, %s, %s, %s)",
#                        (student_id, first_name, last_name, group_name))
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         messagebox.showinfo("Успех", "Студент успешно зарегистрирован.")
#         close_login_window()
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
# # Функция для входа студента
# def login_student():
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s AND first_name = %s AND last_name = %s AND group_name = %s",
#                        (student_id, first_name, last_name, group_name))
#         existing_student = cursor.fetchone()
#         cursor.close()
#         connection.close()
#
#         if existing_student:
#             messagebox.showinfo("Успех", "Студент успешно вошел в систему.")
#             close_login_window()
#         else:
#             messagebox.showerror("Ошибка", "Неправильные данные.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
# # Функция для открытия пустого окна
# def open_empty_window():
#     empty_window = tk.Toplevel(window)
#     empty_window.title("Пустое окно")
#     empty_label = tk.Label(empty_window, text="Пустое окно")
#     empty_label.pack()
#
# # Создание графического интерфейса
# window = tk.Tk()
# window.title("Регистрация и вход для студентов")
#
# # Функция для открытия окна с формой регистрации
# def open_register_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Регистрация студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     register_button = tk.Button(login_window, text="Регистрация", command=register_student)
#     register_button.pack()
#
# # Функция для открытия окна с формой входа
# def open_login_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Вход студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     login_button = tk.Button(login_window, text="Вход", command=login_student)
#     login_button.pack()
#
# # Создание и размещение кнопок "Регистрация" и "Вход"
# register_button = tk.Button(window, text="Регистрация", command=open_register_window)
# register_button.pack()
#
# login_button = tk.Button(window, text="Вход", command=open_login_window)
# login_button.pack()
#
# window.mainloop()
#
#
#
# import tkinter as tk
# from tkinter import messagebox
# import psycopg2
# import datetime
# import re
# book_info_label = None
# issue_book_window = None
#
#
# # Функция для создания подключения к базе данных
# def create_connection():
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="library version 3",
#             user="postgres",
#             password="witcher3"
#         )
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         print("Ошибка при подключении к базе данных:", error)
#
# # Функция для закрытия окна с формами и открытия пустого окна
# def close_login_window():
#     login_window.destroy()
#     open_empty_window()
#
# # Функция для регистрации студента
# def register_student(id_entry, first_name_entry, last_name_entry, group_entry):
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     # Проверка на уникальность ИИН
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
#         existing_student = cursor.fetchone()
#         if existing_student:
#             messagebox.showerror("Ошибка", "Студент с таким ИИН уже зарегистрирован.")
#             cursor.close()
#             connection.close()
#             return
#
#         # Регистрация студента в базе данных
#         cursor.execute("INSERT INTO students (id, first_name, last_name, group_name) VALUES (%s, %s, %s, %s)",
#                        (student_id, first_name, last_name, group_name))
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         messagebox.showinfo("Успех", "Студент успешно зарегистрирован.")
#         close_login_window()
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
# # Функция для входа студента
# def login_student(id_entry, first_name_entry, last_name_entry, group_entry):
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s AND first_name = %s AND last_name = %s AND group_name = %s",
#                        (student_id, first_name, last_name, group_name))
#         existing_student = cursor.fetchone()
#         cursor.close()
#         connection.close()
#
#         if existing_student:
#             messagebox.showinfo("Успех", "Студент успешно вошел в систему.")
#             close_login_window()
#         else:
#             messagebox.showerror("Ошибка", "Неправильные данные.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
# # Функция для открытия пустого окна
# def open_empty_window():
#     global book_info_label
#     empty_window = tk.Toplevel(window)
#     empty_window.title("Пустое окно")
#
#     search_label = tk.Label(empty_window, text="Поиск книги:")
#     search_label.pack()
#
#     search_entry = tk.Entry(empty_window)
#     search_entry.pack()
#
#     search_button = tk.Button(empty_window, text="Найти", command=lambda: search_books(search_entry.get()))
#     search_button.pack()
#
#     empty_label = tk.Label(empty_window, text="Результаты поиска:")
#     empty_label.pack()
#
#     book_info_label = tk.Label(empty_window, text="")
#     book_info_label.pack()
#
#     take_book_button = tk.Button(empty_window, text="Взять книгу",
#                                  command=lambda: open_issue_book_window(book_info_label.cget("text")))
#     take_book_button.pack()
#
# def search_books(query):
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM books WHERE title ILIKE %s OR author ILIKE %s", (f"%{query}%", f"%{query}%"))
#         books = cursor.fetchall()
#         cursor.close()
#         connection.close()
#
#         if books:
#             book_info = ""
#             for book in books:
#                 title, author, pages, status = book
#                 book_info += f"Название: {title}\nАвтор: {author}\nСтраницы: {pages}\nСостояние: {status}\n\n"
#             book_info_label.config(text=book_info)
#         else:
#             book_info_label.config(text="Книги не найдены")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# def open_issue_book_window(book_info):
#     global issue_book_window
#     issue_book_window = tk.Toplevel(window)
#     issue_book_window.title("Выдача книги")
#
#     today_label = tk.Label(issue_book_window, text="Сегодняшняя дата:")
#     today_label.pack()
#
#     today_date = datetime.datetime.now().strftime("%Y-%m-%d")
#
#     today_entry = tk.Entry(issue_book_window, state="readonly")
#     today_entry.insert(tk.END, str(today_date))
#
#     today_entry.pack()
#
#     issue_label = tk.Label(issue_book_window, text="На сколько дней берете книгу:")
#     issue_label.pack()
#
#     days_entry = tk.Entry(issue_book_window)
#     days_entry.pack()
#
#     issue_button = tk.Button(issue_book_window, text="Выдать", command=lambda: issue_book(book_info, days_entry.get(), today_date))
#     issue_button.pack()
#
#
# def issue_book(book_info, days, today_date):
#
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         # Изменение регулярного выражения для извлечения данных из строки book_info
#         match = re.search(r'Название: (.+)\nАвтор: (.+)\nСтраницы: (\d+)\nСостояние: (.+)', book_info)
#         if match:
#             title = match.group(1)
#             author = match.group(2)
#             pages = int(match.group(3))
#             status = match.group(4)
#
#             issue_date = datetime.datetime.now().strftime("%Y-%m-%d")
#             return_date = datetime.datetime.strptime(today_date, "%Y-%m-%d") + datetime.timedelta(days=int(days))
#
#             return_date = str(return_date.date())
#
#             # Исправление SQL-запроса для вставки данных в таблицу issued_books
#             cursor.execute(
#                 "INSERT INTO issued_books (title, author, pages, status, issue_date, return_date) VALUES (%s, %s, %s, %s, %s, %s)",
#                 (title, author, pages, status, issue_date, return_date))
#
#             connection.commit()
#             cursor.close()
#             connection.close()
#             cursor.execute("UPDATE books SET status = %s WHERE title = %s AND author = %s",
#                            ("Недоступно", title, author))
#
#             connection.commit()
#             cursor.close()
#             connection.close()
#
#             messagebox.showinfo("Успех", "Книга успешно выдана.")
#             issue_book_window.destroy()
#         else:
#             messagebox.showerror("Ошибка", "Неправильный формат информации о книге.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
#
# # Создание графического интерфейса
# window = tk.Tk()
# window.title("Регистрация и вход для студентов")
#
# login_window = None
#
# # Функция для открытия окна с формой регистрации
# def open_register_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Регистрация студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     register_button = tk.Button(login_window, text="Регистрация", command=lambda: register_student(id_entry, first_name_entry, last_name_entry, group_entry))
#     register_button.pack()
#
# # Функция для открытия окна с формой входа
# def open_login_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Вход студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     login_button = tk.Button(login_window, text="Вход", command=lambda: login_student(id_entry, first_name_entry, last_name_entry, group_entry))
#     login_button.pack()
#
# # Создание и размещение кнопок "Регистрация" и "Вход"
# register_button = tk.Button(window, text="Регистрация", command=open_register_window)
# register_button.pack()
#
# login_button = tk.Button(window, text="Вход", command=open_login_window)
# login_button.pack()
#
# window.mainloop()
#
# import tkinter as tk
# from tkinter import messagebox
# import psycopg2
# import datetime
# import re
#
# book_info_label = None
# issue_book_window = None
#
#
# # Функция для создания подключения к базе данных
# def create_connection():
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="library version 3",
#             user="postgres",
#             password="witcher3"
#         )
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         print("Ошибка при подключении к базе данных:", error)
#
#
# # Функция для закрытия окна с формами и открытия пустого окна
# def close_login_window():
#     login_window.destroy()
#     open_empty_window()
#
#
# # Функция для регистрации студента
# def register_student(id_entry, first_name_entry, last_name_entry, group_entry):
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     # Проверка на уникальность ИИН
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
#         existing_student = cursor.fetchone()
#         if existing_student:
#             messagebox.showerror("Ошибка", "Студент с таким ИИН уже зарегистрирован.")
#             cursor.close()
#             connection.close()
#             return
#
#         # Регистрация студента в базе данных
#         cursor.execute(
#             "INSERT INTO students (id, first_name, last_name, group_name) VALUES (%s, %s, %s, %s)",
#             (student_id, first_name, last_name, group_name))
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         messagebox.showinfo("Успех", "Студент успешно зарегистрирован.")
#         close_login_window()
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# # Функция для входа студента
# def login_student(id_entry, first_name_entry, last_name_entry, group_entry):
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute(
#             "SELECT id FROM students WHERE id = %s AND first_name = %s AND last_name = %s AND group_name = %s",
#             (student_id, first_name, last_name, group_name))
#         existing_student = cursor.fetchone()
#         cursor.close()
#         connection.close()
#
#         if existing_student:
#             messagebox.showinfo("Успех", "Студент успешно вошел в систему.")
#             close_login_window()
#         else:
#             messagebox.showerror("Ошибка", "Неправильные данные.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# # Функция для открытия пустого окна
# def open_empty_window():
#     global book_info_label
#     empty_window = tk.Toplevel(window)
#     empty_window.title("Пустое окно")
#
#     search_label = tk.Label(empty_window, text="Поиск книги:")
#     search_label.pack()
#
#     search_entry = tk.Entry(empty_window)
#     search_entry.pack()
#
#     search_button = tk.Button(empty_window, text="Найти", command=lambda: search_books(search_entry.get()))
#     search_button.pack()
#
#     empty_label = tk.Label(empty_window, text="Результаты поиска:")
#     empty_label.pack()
#
#     book_info_label = tk.Label(empty_window, text="")
#     book_info_label.pack()
#
#     take_book_button = tk.Button(empty_window, text="Взять книгу",
#                                 command=lambda: open_issue_book_window(book_info_label.cget("text")))
#     take_book_button.pack()
#
#
# def search_books(query):
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM books WHERE title ILIKE %s OR author ILIKE %s", (f"%{query}%", f"%{query}%"))
#         books = cursor.fetchall()
#         cursor.close()
#         connection.close()
#
#         if books:
#             book_info = ""
#             for book in books:
#                 title, author, pages, status = book
#                 book_info += f"Название: {title}\nАвтор: {author}\nСтраницы: {pages}\nСостояние: {status}\n\n"
#             book_info_label.config(text=book_info)
#         else:
#             book_info_label.config(text="Книги не найдены")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# def open_issue_book_window(book_info):
#     global issue_book_window
#     issue_book_window = tk.Toplevel(window)
#     issue_book_window.title("Выдача книги")
#
#     today_label = tk.Label(issue_book_window, text="Сегодняшняя дата:")
#     today_label.pack()
#
#     today_date = datetime.date.today()
#     today_entry = tk.Entry(issue_book_window, state="readonly")
#     today_entry.insert(tk.END, today_date)
#     today_entry.pack()
#
#     issue_label = tk.Label(issue_book_window, text="На сколько дней берете книгу:")
#     issue_label.pack()
#
#     days_entry = tk.Entry(issue_book_window)
#     days_entry.pack()
#
#     issue_button = tk.Button(issue_book_window, text="Выдать",
#                              command=lambda: issue_book(book_info, days_entry.get(), today_date))
#     issue_button.pack()
#
#
# def issue_book(book_info, days, today_date):
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         # Изменение регулярного выражения для извлечения данных из строки book_info
#         match = re.search(r"Название: (.+)\nАвтор: (.+)\nСтраницы: (\d+)\nСостояние: (.+)", book_info)
#         if match:
#             title = match.group(1)
#             author = match.group(2)
#             pages = int(match.group(3))
#             status = match.group(4)
#
#             issue_date = today_date.strftime("%Y-%m-%d")
#             return_date = today_date + datetime.timedelta(days=int(days))
#             return_date = return_date.strftime("%Y-%m-%d")
#
#             # Исправление SQL-запроса для вставки данных в таблицу issued_books
#             cursor.execute(
#                 "INSERT INTO issued_books (title, author, pages, status, issue_date, return_date) VALUES (%s, %s, %s, %s, %s, %s)",
#                 (title, author, pages, status, issue_date, return_date))
#
#             # Изменение статуса книги на "Выдана"
#             cursor.execute("UPDATE books SET status = %s WHERE title = %s AND author = %s",
#                            ("Выдана", title, author))
#
#             connection.commit()
#             cursor.close()
#             connection.close()
#
#             messagebox.showinfo("Успех", "Книга успешно выдана.")
#             issue_book_window.destroy()
#         else:
#             messagebox.showerror("Ошибка", "Неправильный формат информации о книге.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# # Создание графического интерфейса
# window = tk.Tk()
# window.title("Регистрация и вход для студентов")
#
# login_window = None
#
# # Функция для открытия окна с формой регистрации
# def open_register_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Регистрация студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     register_button = tk.Button(login_window, text="Регистрация",
#                                 command=lambda: register_student(id_entry, first_name_entry, last_name_entry, group_entry))
#     register_button.pack()
#
#
# # Функция для открытия окна с формой входа
# def open_login_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Вход студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     login_button = tk.Button(login_window, text="Вход",
#                              command=lambda: login_student(id_entry, first_name_entry, last_name_entry, group_entry))
#     login_button.pack()
#
#
# register_button = tk.Button(window, text="Регистрация", command=open_register_window)
# register_button.pack()
#
# login_button = tk.Button(window, text="Вход", command=open_login_window)
# login_button.pack()
#
# window.mainloop()
# import tkinter as tk
# from tkinter import messagebox
# import psycopg2
# import datetime
# import re
#
# book_info_label = None
# issue_book_window = None
#
#
# # Функция для создания подключения к базе данных
# def create_connection():
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="library version 3",
#             user="postgres",
#             password="witcher3"
#         )
#         return connection
#     except (Exception, psycopg2.Error) as error:
#         print("Ошибка при подключении к базе данных:", error)
#
#
# # Функция для закрытия окна с формами и открытия пустого окна
# def close_login_window():
#     login_window.destroy()
#     open_empty_window()
#
#
# # Функция для регистрации студента
# def register_student(id_entry, first_name_entry, last_name_entry, group_entry):
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     # Проверка на уникальность ИИН
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
#         existing_student = cursor.fetchone()
#         if existing_student:
#             messagebox.showerror("Ошибка", "Студент с таким ИИН уже зарегистрирован.")
#             cursor.close()
#             connection.close()
#             return
#
#         # Регистрация студента в базе данных
#         cursor.execute(
#             "INSERT INTO students (id, first_name, last_name, group_name) VALUES (%s, %s, %s, %s)",
#             (student_id, first_name, last_name, group_name))
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         messagebox.showinfo("Успех", "Студент успешно зарегистрирован.")
#         close_login_window()
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# # Функция для входа студента
# def login_student(id_entry, first_name_entry, last_name_entry, group_entry):
#     # Получение введенных пользователем данных
#     student_id = id_entry.get()
#     first_name = first_name_entry.get()
#     last_name = last_name_entry.get()
#     group_name = group_entry.get()
#
#     # Проверка наличия обязательных данных
#     if not student_id or not first_name or not last_name or not group_name:
#         messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
#         return
#
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute(
#             "SELECT id FROM students WHERE id = %s AND first_name = %s AND last_name = %s AND group_name = %s",
#             (student_id, first_name, last_name, group_name))
#         existing_student = cursor.fetchone()
#         cursor.close()
#         connection.close()
#
#         if existing_student:
#             messagebox.showinfo("Успех", "Студент успешно вошел в систему.")
#             close_login_window()
#         else:
#             messagebox.showerror("Ошибка", "Неправильные данные.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# # Функция для открытия пустого окна
# def open_empty_window():
#     global book_info_label
#     empty_window = tk.Toplevel(window)
#     empty_window.title("Пустое окно")
#
#     search_label = tk.Label(empty_window, text="Поиск книги:")
#     search_label.pack()
#
#     search_entry = tk.Entry(empty_window)
#     search_entry.pack()
#
#     search_button = tk.Button(empty_window, text="Найти", command=lambda: search_books(search_entry.get()))
#     search_button.pack()
#
#     empty_label = tk.Label(empty_window, text="Результаты поиска:")
#     empty_label.pack()
#
#     book_info_label = tk.Label(empty_window, text="")
#     book_info_label.pack()
#
#     take_book_button = tk.Button(empty_window, text="Взять книгу",
#                                 command=lambda: open_issue_book_window(book_info_label.cget("text")))
#     take_book_button.pack()
#
#
# def search_books(query):
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM books WHERE title ILIKE %s OR author ILIKE %s", (f"%{query}%", f"%{query}%"))
#         books = cursor.fetchall()
#         cursor.close()
#         connection.close()
#
#         if books:
#             book_info = ""
#             for book in books:
#                 title, author, pages, status = book
#                 book_info += f"Название: {title}\nАвтор: {author}\nСтраницы: {pages}\nСостояние: {status}\n\n"
#             book_info_label.config(text=book_info)
#         else:
#             book_info_label.config(text="Книги не найдены")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# def open_issue_book_window(book_info):
#     global issue_book_window
#     issue_book_window = tk.Toplevel(window)
#     issue_book_window.title("Выдача книги")
#
#     today_label = tk.Label(issue_book_window, text="Сегодняшняя дата:")
#     today_label.pack()
#
#     today_date = datetime.date.today().strftime("%d-%m-%Y")
#     today_entry = tk.Entry(issue_book_window, state="readonly")
#     today_entry.insert(tk.END, today_date)
#     today_entry.pack()
#
#     issue_label = tk.Label(issue_book_window, text="На сколько дней берете книгу:")
#     issue_label.pack()
#
#     days_entry = tk.Entry(issue_book_window)
#     days_entry.pack()
#
#     issue_button = tk.Button(issue_book_window, text="Выдать",
#                              command=lambda: issue_book(book_info, days_entry.get(), today_date))
#     issue_button.pack()
#
#
# def issue_book(book_info, days, today_date):
#     connection = create_connection()
#     if connection:
#         cursor = connection.cursor()
#         # Изменение регулярного выражения для извлечения данных из строки book_info
#         match = re.search(r"Название: (.+)\nАвтор: (.+)\nСтраницы: (\d+)\nСостояние: (.+)", book_info)
#         if match:
#             title = match.group(1)
#             author = match.group(2)
#             pages = int(match.group(3))
#             status = match.group(4)
#
#             issue_date = today_date.strftime("%Y-%m-%d")
#             return_date = today_date + datetime.timedelta(days=int(days))
#             return_date = return_date.strftime("%Y-%m-%d")
#
#             # Исправление SQL-запроса для вставки данных в таблицу issued_books
#             cursor.execute(
#                 "INSERT INTO issued_books (title, author, pages, status, issue_date, return_date) VALUES (%s, %s, %s, %s, %s, %s)",
#                 (title, author, pages, status, issue_date, return_date))
#
#             # Изменение статуса книги на "Выдана"
#             cursor.execute("UPDATE books SET status = %s WHERE title = %s AND author = %s",
#                            ("Выдана", title, author))
#
#             connection.commit()
#             cursor.close()
#             connection.close()
#
#             messagebox.showinfo("Успех", "Книга успешно выдана.")
#             issue_book_window.destroy()
#         else:
#             messagebox.showerror("Ошибка", "Неправильный формат информации о книге.")
#     else:
#         messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")
#
#
# # Создание графического интерфейса
# window = tk.Tk()
# window.title("Регистрация и вход для студентов")
#
# login_window = None
#
# # Функция для открытия окна с формой регистрации
# def open_register_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Регистрация студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     register_button = tk.Button(login_window, text="Регистрация",
#                                 command=lambda: register_student(id_entry, first_name_entry, last_name_entry, group_entry))
#     register_button.pack()
#
#
# # Функция для открытия окна с формой входа
# def open_login_window():
#     global login_window
#     login_window = tk.Toplevel(window)
#     login_window.title("Вход студента")
#
#     id_label = tk.Label(login_window, text="ИИН:")
#     id_label.pack()
#     id_entry = tk.Entry(login_window)
#     id_entry.pack()
#
#     first_name_label = tk.Label(login_window, text="Имя:")
#     first_name_label.pack()
#     first_name_entry = tk.Entry(login_window)
#     first_name_entry.pack()
#
#     last_name_label = tk.Label(login_window, text="Фамилия:")
#     last_name_label.pack()
#     last_name_entry = tk.Entry(login_window)
#     last_name_entry.pack()
#
#     group_label = tk.Label(login_window, text="Название группы:")
#     group_label.pack()
#     group_entry = tk.Entry(login_window)
#     group_entry.pack()
#
#     login_button = tk.Button(login_window, text="Вход",
#                              command=lambda: login_student(id_entry, first_name_entry, last_name_entry, group_entry))
#     login_button.pack()
#
#
# register_button = tk.Button(window, text="Регистрация", command=open_register_window)
# register_button.pack()
#
# login_button = tk.Button(window, text="Вход", command=open_login_window)
# login_button.pack()
#
# window.mainloop()
import tkinter as tk
from tkinter import messagebox
import psycopg2
import datetime
import re

book_info_label = None
issue_book_window = None

# Функция для создания подключения к базе данных
def create_connection():
    try:
        connection = psycopg2.connect(
            host="ep-autumn-unit-766699-pooler.us-east-2.aws.neon.tech",
            database="neondb",
            user="ersyn2000000",
            password="nJk7wG0hPxQM"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при подключении к базе данных:", error)

# Функция для закрытия окна с формами и открытия пустого окна
def close_login_window():
    login_window.destroy()
    open_empty_window()

# Функция для регистрации студента
def register_student(id_entry, first_name_entry, last_name_entry, group_entry):
    # Получение введенных пользователем данных
    student_id = id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    group_name = group_entry.get()

    # Проверка наличия обязательных данных
    if not student_id or not first_name or not last_name or not group_name:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    # Проверка на уникальность ИИН
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
        existing_student = cursor.fetchone()
        if existing_student:
            messagebox.showerror("Ошибка", "Студент с таким ИИН уже зарегистрирован.")
            cursor.close()
            connection.close()
            return

        # Регистрация студента в базе данных
        cursor.execute(
            "INSERT INTO students (id, first_name, last_name, group_name) VALUES (%s, %s, %s, %s)",
            (student_id, first_name, last_name, group_name))
        connection.commit()
        cursor.close()
        connection.close()

        messagebox.showinfo("Успех", "Студент успешно зарегистрирован.")
        close_login_window()
    else:
        messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")

# Функция для входа студента
def login_student(id_entry, first_name_entry, last_name_entry, group_entry):
    # Получение введенных пользователем данных
    student_id = id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    group_name = group_entry.get()

    # Проверка наличия обязательных данных
    if not student_id or not first_name or not last_name or not group_name:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id FROM students WHERE id = %s AND first_name = %s AND last_name = %s AND group_name = %s",
            (student_id, first_name, last_name, group_name))
        existing_student = cursor.fetchone()
        cursor.close()
        connection.close()

        if existing_student:
            messagebox.showinfo("Успех", "Студент успешно вошел в систему.")
            close_login_window()
        else:
            messagebox.showerror("Ошибка", "Неправильные данные.")
    else:
        messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")

# Функция для открытия пустого окна
def open_empty_window():
    global book_info_label
    empty_window = tk.Toplevel(window)
    empty_window.title("Пустое окно")

    search_label = tk.Label(empty_window, text="Поиск книги:")
    search_label.pack()

    search_entry = tk.Entry(empty_window)
    search_entry.pack()

    search_button = tk.Button(empty_window, text="Найти", command=lambda: search_books(search_entry.get()))
    search_button.pack()

    empty_label = tk.Label(empty_window, text="Результаты поиска:")
    empty_label.pack()

    book_info_label = tk.Label(empty_window, text="")
    book_info_label.pack()

    take_book_button = tk.Button(empty_window, text="Взять книгу", command=lambda: open_issue_book_window(book_info_label.cget("text")))
    take_book_button.pack()

def search_books(query):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books WHERE title ILIKE %s OR author ILIKE %s", (f"%{query}%", f"%{query}%"))
        books = cursor.fetchall()
        cursor.close()
        connection.close()

        if books:
            book_info = ""
            for book in books:
                title, author, pages, status = book
                book_info += f"Название: {title}\nАвтор: {author}\nСтраницы: {pages}\nСостояние: {status}\n\n"
            book_info_label.config(text=book_info)
        else:
            book_info_label.config(text="Книги не найдены")
    else:
        messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")


def open_issue_book_window(book_info):
    global issue_book_window
    issue_book_window = tk.Toplevel(window)
    issue_book_window.title("Выдача книги")

    today_label = tk.Label(issue_book_window, text="Сегодняшняя дата:")
    today_label.pack()

    today_date = datetime.date.today().strftime("%d-%m-%Y")
    today_entry = tk.Entry(issue_book_window, state="normal")
    today_entry.insert(tk.END, today_date)
    today_entry.pack()

    issue_label = tk.Label(issue_book_window, text="На сколько дней берете книгу:")
    issue_label.pack()

    days_entry = tk.Entry(issue_book_window)
    days_entry.pack()

    issue_button = tk.Button(issue_book_window, text="Выдать", command=lambda: issue_book(book_info, days_entry.get(), today_date))
    issue_button.pack()

def issue_book(book_info, days, today_date):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        match = re.search(r"Название: (.+)\nАвтор: (.+)\nСтраницы: (\d+)\nСостояние: (.+)", book_info)
        if match:
            title = match.group(1)
            author = match.group(2)
            pages = int(match.group(3))
            status = match.group(4)

            issue_date = datetime.datetime.strptime(today_date, "%d-%m-%Y").date()
            return_date = issue_date + datetime.timedelta(days=int(days))
            return_date_str = return_date.strftime("%d-%m-%Y")

            cursor.execute(
                "INSERT INTO issued_books (title, author, pages, status, issue_date, return_date) VALUES (%s, %s, %s, %s, %s, %s)",
                (title, author, pages, status, issue_date, return_date))

            cursor.execute("UPDATE books SET status = %s WHERE title = %s AND author = %s",
                           ("Выдана", title, author))

            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Успех", f"Книга успешно выдана. Дата возврата: {return_date_str}")
            issue_book_window.destroy()
        else:
            messagebox.showerror("Ошибка", "Неправильный формат информации о книге.")
    else:
        messagebox.showerror("Ошибка", "Не удалось подключиться к базе данных.")

# Создание графического интерфейса
window = tk.Tk()
window.title("Регистрация и вход для студентов")

login_window = None

# Функция для открытия окна с формой регистрации
def open_register_window():
    global login_window
    login_window = tk.Toplevel(window)
    login_window.title("Регистрация студента")

    id_label = tk.Label(login_window, text="ИИН:")
    id_label.pack()
    id_entry = tk.Entry(login_window)
    id_entry.pack()

    first_name_label = tk.Label(login_window, text="Имя:")
    first_name_label.pack()
    first_name_entry = tk.Entry(login_window)
    first_name_entry.pack()

    last_name_label = tk.Label(login_window, text="Фамилия:")
    last_name_label.pack()
    last_name_entry = tk.Entry(login_window)
    last_name_entry.pack()

    group_label = tk.Label(login_window, text="Название группы:")
    group_label.pack()
    group_entry = tk.Entry(login_window)
    group_entry.pack()

    register_button = tk.Button(login_window, text="Регистрация", command=lambda: register_student(id_entry, first_name_entry, last_name_entry, group_entry))
    register_button.pack()

# Функция для открытия окна с формой входа
def open_login_window():
    global login_window
    login_window = tk.Toplevel(window)
    login_window.title("Вход студента")

    id_label = tk.Label(login_window, text="ИИН:")
    id_label.pack()
    id_entry = tk.Entry(login_window)
    id_entry.pack()

    first_name_label = tk.Label(login_window, text="Имя:")
    first_name_label.pack()
    first_name_entry = tk.Entry(login_window)
    first_name_entry.pack()

    last_name_label = tk.Label(login_window, text="Фамилия:")
    last_name_label.pack()
    last_name_entry = tk.Entry(login_window)
    last_name_entry.pack()

    group_label = tk.Label(login_window, text="Название группы:")
    group_label.pack()
    group_entry = tk.Entry(login_window)
    group_entry.pack()

    login_button = tk.Button(login_window, text="Вход", command=lambda: login_student(id_entry, first_name_entry, last_name_entry, group_entry))
    login_button.pack()

register_button = tk.Button(window, text="Регистрация", command=open_register_window)
register_button.pack()

login_button = tk.Button(window, text="Вход", command=open_login_window)
login_button.pack()

window.mainloop()
