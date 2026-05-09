# Задание 2. API-пайплайн: данные → LLM → результат

## Описание задания
Написать рабочий скрипт, который автоматически отправляет данные в LLM через API и получает структурированный ответ в JSON.

## Что делает скрипт
1. читает отзывы из файла input.csv
2. отправляет их в LLM (OpenRouter API)
3. анализирует тональность каждого отзыва (positive/negative/neutral)
4. сохраняет результат в файл result.json

## Установка

1. склонировать репозиторий:
   git clone https://github.com/SevaAlieva/2taska.git
2. установить зависимости:
   pip install -r requirements.txt

3. получить API ключ на https://openrouter.ai/keys

4. в файл .env в корне проекта добавить этот ключ:
   OPENROUTER_API_KEY=sk-or-v1-ваш_ключ

## Запуск

    python main.py

## Структура проекта
    task2/
    ├── .env # API ключ
    ├── input.csv # Входные данные (отзывы)
    ├── main.py # Основной скрипт
    ├── requirements.txt # Зависимости
    ├── result.json # Выходной файл с результатом
    └── README.md # Описание проекта


## Входные данные (input.csv)

Файл с колонками:
- `id` - номер отзыва
- `review_text` - текст отзыва

## Пример результатов (JSON)
      {
        "total_reviews": 20,
        "mood_distribution": {
          "positive": 8,
          "negative": 6,
          "neutral": 6
        },
        "results": [
          {
            "review_id": 1,
            "mood": "positive",
            "reason": "Очень вкусные блюда, хороший сервис"
          },
          {
            "review_id": 2,
            "mood": "positive",
            "reason": "Божественная еда, адекватные цены"
          },