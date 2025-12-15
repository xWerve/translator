from deep_translator import GoogleTranslator

import sqlite3
conn = sqlite3.connect("sheet_words.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS eng_pol(
    text_to_translation TEXT NOT NULL,
    text_after_translation TEXT NOT NULL,
    language_from TEXT NOT NULL,
    language_to TEXT NOT NULL
)
    """
)
conn.commit()

print("Witaj w tłumaczu")

while 1:
    start = input("Podaj język w jakim chcesz tłumaczyć: ")
    if start in ('pl', 'en', 'de', 'es'):
        break
    print("Podałeś język który nie jest obsługiwany przez nasz translator")

while 1:
    stop = input("Podaj język na jaki chcesz przetlumaczyc: ")
    if start in ('pl', 'en', 'de', 'es'):
        break
    print("Podałeś język który nie jest obsługiwany przez nasz translator")


text = input("Podaj tekst do przetłumaaczenia: ")
print(text)
translated_text = GoogleTranslator(source=start, target=stop).translate(text)
print(translated_text)

cursor.execute("INSERT INTO sheet_words (text_to_translation, text_after_translation, language_from, language_to) VALUES ($, $, $, $), (text, translated_text, start, stop)")

conn.close()
