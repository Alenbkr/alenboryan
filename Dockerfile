FROM python:3.12-slim

# Устанавливаем нужные библиотеки для PostgreSQL
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория в контейнере
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
