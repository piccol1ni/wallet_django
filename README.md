# Wallet Manager

Wallet Manager - это веб-приложение для управления кошельками и транзакциями.

## Запуск проекта

Проект использует Docker и Docker Compose для удобного развертывания. Убедитесь, что у вас установлены Docker и Docker Compose.

### Шаг 1: Клонирование репозитория

```python
git clone https://github.com/piccol1ni/wallet_django
cd wallet-manager
```


### Шаг 2: Запуск Docker Compose

```bash
docker-compose up --build
```

Это создаст и запустит контейнеры Docker для приложения и базы данных.

### Шаг 3: Применяем миграции

```bash
docker-compose run --rm web-app sh -c "python3 manage.py makemigrations"
docker-compose run --rm web-app sh -c "python3 manage.py migrate"
```

### Шаг 4: Создаем пользователя

```bash
docker-compose run --rm web-app sh -c "python3 manage.py createsuperuser"
```

### Шаг 5: Создаем файл для логов

```bash
docker-compose run --rm web-app sh -c "touch service/logs/debug.log"
```

## Проект готов к работе! Создавать транзакции возможно как в Админке пользователя, так и при поиощи API по адресу:
http://127.0.0.1:8000/api/transactions

## Создавать кошельки так же возможно и в админке и при помощи API по адресу:
http://127.0.0.1:8000/api/wallets

## Тестирование производится при поиощи команды:
```bash
docker-compose run --rm web-app sh -c "python3 manage.py tests"
```
## Ограничения:
1. Нельзя переводить деньги RUB/USD и USD/RUB
2. Нельзя переводить деньги, которых у вас нет!
