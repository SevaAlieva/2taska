import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv('OPENROUTER_API_KEY')
client = OpenAI(
    api_key=api_key,
    base_url='https://openrouter.ai/api/v1'
)
def load_reviews():
    df = pd.read_csv('input.csv')
    return df['review_text'].tolist()

def analyze_reviews(reviews):
    prompt = f'''
    Проанализируй тональность следующих отзывов о ресторанах.
    Для каждого определи: positive, negative или neutral.
    Отзывы:
    {reviews}
    Верни только JSON без любого другого текста в формате:
    {{
        "total_reviews": число,
        "mood_distribution": {{
            "positive": число,
            "negative": число,
            "neutral": число
        }},
        "results": [
            {{
                "review_id": число,
                "mood": "positive или negative или neutral",
                "reason": "краткое объяснение"
            }}
        ],
        "summary": "общий вывод по настроению отзывов"
    }}
    '''
    response = client.chat.completions.create(
        model='openai/gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.2,
        max_tokens=4000
    )
    content = response.choices[0].message.content.strip()
    if '```json' in content:
        content = content.split('```json')[1].split('```')[0].strip()
    elif '```' in content:
        content = content.split('```')[1].split('```')[0].strip()

    return json.loads(content)

reviews = load_reviews()
result = analyze_reviews(reviews)

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)