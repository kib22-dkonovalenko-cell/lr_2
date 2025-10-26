import sys
from googletrans import Translator, LANGUAGES


translator = Translator()


def TransLate(text_str, lang):
    lang_norm = str(lang).lower().strip()
    target_code = None

    if lang_norm in LANGUAGES:
        target_code = lang_norm
    else:
        for code, name in LANGUAGES.items():
            if name == lang_norm:
                target_code = code
                break

    if target_code is None:
        return f"Помилка: Мову '{lang}' не знайдено."

    try:
        translation = translator.translate(text_str, dest=target_code)
        return translation.text
    except Exception as e:
        if "HTTP Error 429" in str(e):
            return "Помилка: Забагато запитів (HTTP 429). Спробуйте пізніше."
        return f"Помилка під час перекладу: {e}"


def LangDetect(txt):
    try:
        detection = translator.detect(txt)
        return (detection.lang, detection.confidence)
    except Exception as e:
        return (f"Помилка визначення: {e}", None)


def CodeLang(lang):
    lang_norm = str(lang).lower().strip()

    if lang_norm in LANGUAGES:
        return LANGUAGES[lang_norm]

    for code, name in LANGUAGES.items():
        if name == lang_norm:
            return code

    return f"Мову або код '{lang}' не знайдено."

def main_loop():
    print("--- Програма-перекладач (googletrans 3.1.0a0) ---")
    print("Для виходу введіть 'exit' або 'вихід'.\n")

    while True:
        try:
            text_to_translate = input("Введіть текст для перекладу: ")
        except EOFError:
            break

        if text_to_translate.lower() in ['exit', 'вихід']:
            break

        if not text_to_translate:
            continue

        lang_code, confidence = LangDetect(text_to_translate)

        if confidence is not None:
            lang_name = CodeLang(lang_code)
            print(f"Виявлена мова: {lang_name.capitalize()} (код: {lang_code}), впевненість: {confidence:.2f}")
        else:
            print(f"Не вдалося визначити мову. {lang_code}")
            continue

        try:
            target_lang = input("Введіть мову для перекладу (наприклад, English або en): ")
        except EOFError:
            break

        if target_lang.lower() in ['exit', 'вихід']:
            break

        if not target_lang:
            print("Мову не введено. Спроба скасована.")
            continue

        translated_text = TransLate(text_to_translate, target_lang)

        if "Помилка:" in translated_text:
            print(translated_text)
        else:
            print("--------------------")
            print(f"Результат перекладу: {translated_text}")

        print("-" * 20 + "\n")

if __name__ == "__main__":
    main_loop()