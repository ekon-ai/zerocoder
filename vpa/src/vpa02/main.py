import requests
import logging

# Настраиваем вывод сообщений, чтобы было красиво и понятно
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def ping_google() -> bool:
    """Проверяет доступность google.com через легкий HTTP-запрос."""
    url = "https://www.google.com"
    try:
        # Используем HEAD-запрос: он получает только заголовки, не скачивая весь сайт (экономит трафик и время)
        response = requests.head(url, timeout=5)

        if response.status_code == 200:
            logging.info(f"✅ Успех! {url} отвечает (Код: {response.status_code})")
            return True
        else:
            logging.warning(
                f"⚠️ {url} ответил, но с неожиданным кодом: {response.status_code}"
            )
            return False

    except requests.exceptions.Timeout:
        logging.error(f"❌ Превышено время ожидания (timeout) при подключении к {url}")
        return False
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Ошибка сети при подключении к {url}: {e}")
        return False


def main():
    """Точка входа в программу. Вызывается автоматически при запуске скрипта."""
    logging.info("🚀 Запуск проверки доступности Google...")
    ping_google()


# Эта проверка позволяет запускать файл напрямую (например, через F5 в VS Code)
if __name__ == "__main__":
    main()
