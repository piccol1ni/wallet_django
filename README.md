# Wallet Manager

Wallet Manager - это веб-приложение для управления кошельками и транзакциями.

## Запуск проекта

Проект использует Docker и Docker Compose для удобного развертывания. Убедитесь, что у вас установлены Docker и Docker Compose.

### Шаг 1: Клонирование репозитория

```python
git clone https://github.com/piccol1ni/wallet_django
cd wallet-manager
```


### Шаг 2: Настройка окружения
Создайте файл .env в корне проекта и укажите необходимые переменные окружения:

```bash
DEBUG=True
SECRET_KEY=your_secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DATABASE_URL=postgres://wallet_manager:password@db:5432/wallet_manager
```