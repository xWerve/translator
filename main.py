import tkinter as tk
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
    label_result.pack(pady=10)

    def translation():
        lang_from = lang_from_var.get()
        lang_to = lang_to_var.get()
        content = content_var.get()

        text_translated = GoogleTranslator(source=lang_from, target=lang_to).translate(content)
        label_result.config(text=text_translated)


    tk.Button(window1, text="Tłumacz", command=translation).pack()


    window1.mainloop()


window = tk.Tk()
window.title("Translator_App")
window.geometry("1500x750")

label1 = tk.Label(window, text="Witaj w tłumaczu!")
label1.pack()

button1 = tk.Button(window, text="Przetłumacz słowo: ", command=function_button1)
button1.pack()


window.mainloop()