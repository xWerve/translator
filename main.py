import tkinter as tk
import sqlite3
import random
from tkinter import messagebox
from deep_translator import GoogleTranslator

def function_button1():
    window1 = tk.Toplevel()
    window1.title("Tłumaczenie: ")
    window1.geometry("1500x750")

    lang_from_var = tk.StringVar()
    lang_to_var = tk.StringVar()
    content_var = tk.StringVar()

    tk.Label(window1, text="Podaj język z którego chcesz tłumaczyć!").pack()
    tk.Entry(window1, textvariable=lang_from_var).pack()

    tk.Label(window1, text="Podaj język na który chcesz tłumaczyć!").pack()
    tk.Entry(window1, textvariable=lang_to_var).pack()

    tk.Label(window1, text="Podaj słowo do przetłumaczenia!").pack()
    tk.Entry(window1, textvariable=content_var).pack()

    label_result = tk.Label(window1, text="")
    label_result.pack()

    def translation():
        lang_from = lang_from_var.get()
        lang_to = lang_to_var.get()
        content = content_var.get()

        try:
            text_translated = GoogleTranslator(source=lang_from, target=lang_to).translate(content)
            label_result.config(text=text_translated)
            try:
                cursor.execute(
                    "INSERT INTO sheet_words (text_to_translation, text_after_translation, language_from, language_to) VALUES (?, ?, ?, ?)",
                    (content, text_translated, lang_from, lang_to)
                )
                conn.commit()
            except Exception as e:
                messagebox.showerror("Błąd", f"Wystąpił błąd zapisu do bazy danych {e}")

        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd tłumaczenia {e}")

    tk.Button(window1, text="Tłumacz", command=translation).pack()


    window1.mainloop()

def function_button2():
    window2 = tk.Toplevel()
    window2.title("Lista słówek w słowniku")
    window2.geometry('1500x750')

    cursor.execute("SELECT * FROM sheet_words")
    rows = cursor.fetchall()

    for row in rows:
        text = " | ".join(str(item) for item in row)
        tk.Label(window2, text=text).pack()

def function_button3():
    window3 = tk.Toplevel()
    window3.title("Nauka słówek")
    window3.geometry('1500x750')

    cursor.execute("SELECT * FROM sheet_words")
    rows = cursor.fetchall()

    guess_val = tk.StringVar()

    label_lang = tk.Label(window3)
    label_lang.pack()

    label_word = tk.Label(window3, font=("Arial", 18))
    label_word.pack()

    entry = tk.Entry(window3, textvariable=guess_val)
    entry.pack()

    label_result = tk.Label(window3, text="")
    label_result.pack()

    def new_word():
        nonlocal rnd_id
        rnd_id = random.randint(0, len(rows) - 1)
        label_lang.config(text=f"Z {rows[rnd_id][2]} na {rows[rnd_id][3]}")
        label_word.config(text=rows[rnd_id][0])
        guess_val.set("")
        label_result.config(text="")
        entry.focus()

    def check():
        guess = guess_val.get()
        if guess == rows[rnd_id][1]:
            label_result.config(text="✅ Poprawna odpowiedź")
        else:
            label_result.config(text=f"❌ Niepoprawna – poprawna to: {rows[rnd_id][1]}")
        window3.after(5000, new_word)

    tk.Button(window3, text="Czy poprawna", command=check).pack()

    rnd_id = 0
    new_word()

    window3.mainloop()


conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sheet_words(
    text_to_translation TEXT NOT NULL,
    text_after_translation TEXT NOT NULL,
    language_from TEXT NOT NULL,
    language_to TEXT NOT NULL
)
    """
)
conn.commit()


window = tk.Tk()
window.title("Translator_App")
window.geometry("1500x750")


tk.Label(window, text="Witaj w tłumaczu!").pack()
tk.Button(window, text="Przetłumacz słowo: ", command=function_button1).pack()
tk.Button(window, text="Wyświetl słowa, które miałeś w słowniku: ", command=function_button2).pack()
tk.Button(window, text="Ucz się fiszek", command=function_button3).pack()


window.mainloop()

cursor.close()
conn.close()