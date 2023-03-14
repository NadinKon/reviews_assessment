import openai
import pandas as pd
import os

# Устанавливаем API ключ для OpenAI
OPENAI_API_KEY = 'sk-iDluXZf********x0draWrS'
openai.api_key = OPENAI_API_KEY

# Загружаем таблицу
filename = 'Reviews.xlsx'
#df = pd.read_csv(filename)
df = pd.read_excel(filename)

# Создаем новую колонку для оценок
df['rate'] = 0

print('''Анализирую каждый отзыв...
Сейчас будет готово...''')

# Анализируем каждый отзыв и проставляем оценку
for i, row in df.iterrows():
    review = row['review']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Rate the following review from 1 to 10, where 1 is the most negative and 10 is the most positive:\n\n{review}\n\nRating:",
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.7,
    )

    rate = int(response.choices[0].text.strip())
    df.at[i, 'rate'] = rate


# Сортируем отзывы по убыванию оценки
df = df.sort_values(by=['rate'], ascending=False)

print("-----------------------------")
print('Все готово!')

# Создаем новый файл с результатами
new_filename = os.path.splitext(filename)[0] + '_analyzed.xlsx'
df.to_csv(new_filename, index=False)
