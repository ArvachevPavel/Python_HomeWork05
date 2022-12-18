# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text = 'Привет, забвение, пока'
print(f"Начальный текст: {text}")

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_words(text)
print(f"Обработанный текст: {text}")