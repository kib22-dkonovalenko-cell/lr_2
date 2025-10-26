import requests
import sys

# Ми перевіряємо не просто 'requests', а й сертифікати, які він використовує
import certifi

API_URL = "https://api.mymemory.translated.net/get?q=test&langpair=en|uk"

print(f"--- 🚀 Початок тесту ---")
print(f"Python версія: {sys.version.split()[0]}")
print(f"Шлях до Python: {sys.executable}")
print(f"Бібліотека requests: {requests.__file__}")
print(f"Сертифікати: {certifi.where()}")
print(f"Спроба підключитися до: {API_URL}\n")

try:
    # Робимо прямий запит з тайм-аутом 10 секунд
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status() # Викине помилку, якщо статус 4xx/5xx

    print(f"--- ✅ УСПІХ! ---")
    print(f"Статус-код: {response.status_code}")
    print("З'єднання з API встановлено.")
    print(f"Отримана відповідь (JSON): {response.json()}")

except Exception as e:
    print(f"--- ❌ ПРОВАЛ! ---")
    print("Не вдалося підключитися. Виникла детальна помилка:")
    print(f"\nТип помилки:\n{type(e)}")
    print(f"\nПовний текст помилки:\n{e}")

print(f"\n--- 🏁 Тест завершено ---")