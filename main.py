from tkinter import *
from datetime import datetime
from tkinter.messagebox import showinfo

# Глобальные переменные для управления временем и состоянием приложения
temp = 0  # Временной счётчик для секундомера
after_id = ""  # ID для управления задачами после вызова after
hours = 0  # Часы для таймера
minut = 0  # Минуты для таймера
current_mode = "sec"  # Текущий режим работы: "sec" (секундомер) или "timer" (таймер)

def tick():
    """Обновляет значение секундомера каждую секунду."""
    global temp, after_id
    after_id = window.after(1000, tick)  # Планирует вызов функции через 1 секунду
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")  # Форматирует время в MM:SS
    lbl1.configure(text=str(f_temp))  # Обновляет текст метки
    temp += 1

def start():
    """Начинает работу секундомера."""
    lbl.config(text="Время пошло")
    btn.place_forget()  # Убирает кнопку Start
    btn1.place(relx=.5, rely=.7, anchor="c")  # Показывает кнопку Stop
    tick()

def stop():
    """Останавливает секундомер."""
    lbl.config(text="Хотите сбросить Секундомер?")
    btn1.place_forget()  # Убирает кнопку Stop
    btn2.place(relx=.5, rely=.7, anchor="c")  # Показывает кнопку Reset
    window.after_cancel(after_id)  # Останавливает вызовы tick

def reset():
    """Сбрасывает секундомер."""
    lbl.config(text="Для начала нажми на кнопку Start")
    global temp
    temp = 0
    btn2.place_forget()  # Убирает кнопку Reset
    btn.place(relx=.5, rely=.7, anchor="c")  # Показывает кнопку Start
    lbl1.config(text="00:00")

def starttm():
    """Запускает таймер."""
    global after_id, hours, minut, current_mode
    lbl.config(text="Время пошло!")
    btn3.place_forget()
    btn4.place_forget()
    btn5.place_forget()
    btn6.place_forget()
    btn7.place_forget()

    # Проверка, если время таймера закончилось
    if hours == 0 and minut == 0:
        lbl.config(text="Время вышло!")
        showinfo("Время вышло!", "Таймер закончил свою работу!")
        lbl1.config(text="00:00")
        btn8.place_forget()
        timer()  # Возвращает интерфейс в режим ввода времени
        return

    # Логика уменьшения времени
    if minut == 0:
        if hours > 0:
            hours -= 1
            minut = 59
    else:
        minut -= 1

    # Форматирование отображения времени
    h1 = f"{hours:02}:{minut:02}"
    lbl1.config(text=h1)
    after_id = window.after(1000, starttm)  # Запускает обратный вызов через 1 секунду
    lbl.config(text="Чтобы остановить нажмите Stop")
    btn8.place(relx=.5, rely=.8, anchor="c")  # Показывает кнопку Stop

def stoptm():
    """Останавливает таймер."""
    lbl.config(text="Хотите сбросить таймер?")
    btn8.place_forget()
    btn9.place(relx=.5, rely=.8, anchor="c")  # Показывает кнопку Reset
    window.after_cancel(after_id)  # Останавливает вызовы starttm

def resettm():
    """Сбрасывает таймер."""
    lbl.config(text="Для начала нажми на кнопку Start")
    global hours, minut
    hours = 0
    minut = 0
    btn9.place_forget()
    timer()

def timer():
    """Переключает интерфейс в режим таймера."""
    title_label.config(text="Таймер")
    btn.place_forget()
    btn1.place_forget()
    btn2.place_forget()
    lbl.config(text="Введите время для таймера")
    lbl1.config(text="00:00")
    btn3.place(relx=.3, rely=.6, anchor="c")  # Кнопка увеличения часов
    btn4.place(relx=.4, rely=.6, anchor="c")  # Кнопка уменьшения часов
    btn5.place(relx=.6, rely=.6, anchor="c")  # Кнопка увеличения минут
    btn6.place(relx=.7, rely=.6, anchor="c")  # Кнопка уменьшения минут
    btn7.place(relx=.5, rely=.8, anchor="c")  # Кнопка запуска таймера

def plush():
    """Увеличивает часы таймера."""
    global hours, minut
    if hours < 59:
        hours += 1
    else:
        showinfo("Предупреждение!", "Мой таймер не рассчитан на такие цифры!")
    lbl1.config(text=f"{hours:02}:{minut:02}")

def minush():
    """Уменьшает часы таймера."""
    global hours, minut
    if hours > 0:
        hours -= 1
    lbl1.config(text=f"{hours:02}:{minut:02}")

def plusm():
    """Увеличивает минуты таймера."""
    global hours, minut
    if minut < 59:
        minut += 1
    else:
        showinfo("Предупреждение!", "Мой таймер не рассчитан на такие цифры!")
    lbl1.config(text=f"{hours:02}:{minut:02}")

def minusm():
    """Уменьшает минуты таймера."""
    global hours, minut
    if minut > 0:
        minut -= 1
    lbl1.config(text=f"{hours:02}:{minut:02}")

def sec():
    """Переключает интерфейс в режим секундомера."""
    title_label.config(text="Секундомер")
    global current_mode, hours, minut
    hours = 0
    minut = 0
    if current_mode != "sec":
        current_mode = "sec"
        window.after_cancel(after_id)  # Останавливает текущую задачу
        btn3.place_forget()
        btn4.place_forget()
        btn5.place_forget()
        btn6.place_forget()
        btn7.place_forget()
        btn8.place_forget()
        btn9.place_forget()
        lbl.config(text="Для начала нажми на кнопку Start")
        lbl1.config(text="00:00")
        btn.place(relx=.5, rely=.8, anchor="c")

def Timer():
    """Переключает интерфейс в режим таймера."""
    title_label.config(text="Таймер")
    global current_mode, temp
    temp = 0
    if current_mode != "timer":
        current_mode = "timer"
        window.after_cancel(after_id)  # Останавливает текущую задачу
        btn.place_forget()
        btn1.place_forget()
        btn2.place_forget()
        lbl.config(text="Введите время для таймера")
        lbl1.config(text="00:00")
        btn3.place(relx=.3, rely=.6, anchor="c")
        btn4.place(relx=.4, rely=.6, anchor="c")
        btn5.place(relx=.6, rely=.6, anchor="c")
        btn6.place(relx=.7, rely=.6, anchor="c")
        btn7.place(relx=.5, rely=.8, anchor="c")

# Настройка основного окна приложения
window = Tk()
window['bg'] = '#2E3B4E'
window.title("Лабораторная работа №3")
window.geometry("400x400")
window.resizable(False, False)

# Заголовок приложения
title_label = Label(window, text="Секундомер", font=("Arial", 24, 'bold'), bg="#2E3B4E", fg="#E1EFFF")
title_label.pack(pady=20)

# Стили для кнопок
btn_style = {"font": ("Arial", 18), "bg": "#66CDAA", "activebackground": "White", "relief": "solid", "bd": 2}

# Метка для статуса
lbl = Label(window, text="Для начала нажми на кнопку Start", font=("Arial", 16), fg="#F4F4F4", bg="#2E3B4E")
lbl.pack(pady=10)

# Метка для отображения времени
lbl1 = Label(window, text="00:00", font=("Elephant", 50), fg="#F4F4F4", bg="#2E3B4E")
lbl1.pack()

# Кнопки для управления приложением
btn = Button(window, text="Start!",  command=start, **btn_style)
btn.place(relx=.5, rely=.7, anchor="c")

btn1 = Button(window, text="Stop!", command=stop, **btn_style)
btn2 = Button(window, text="Reset?", command=reset, **btn_style)
btn3 = Button(window, text="+", command=plush, **btn_style)
btn4 = Button(window, text="-", command=minush, **btn_style)
btn5 = Button(window, text="+", command=plusm, **btn_style)
btn6 = Button(window, text="-", command=minusm, **btn_style)
btn7 = Button(window, text="Start!", command=starttm, **btn_style)
btn8 = Button(window, text="Stop!", command=stoptm, **btn_style)
btn9 = Button(window, text="Reset!", command=resettm, **btn_style)

# Меню для выбора режима
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label="Таймер", command=Timer)
new_item.add_command(label="Секундомер", command=sec)
menu.add_cascade(label="Сменить режим", menu=new_item)
window.config(menu=menu)

# Запуск основного цикла приложения
window.mainloop()
