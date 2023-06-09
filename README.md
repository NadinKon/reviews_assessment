## Reviews assessment
Скрипт для анализа отзывов с использованием OpenAI API. 
Он загружает данные из Excel-файла, анализирует каждый отзыв и проставляет оценку от 1 до 10, где 1 - самый негативный отзыв, а 10 - самый положительный. 
Затем отзывы сортируются по убыванию оценки и сохраняются в новом Excel-файле.

### Установка и запуск:
Для запуска этого кода необходимо установить следующие зависимости:

openai (API для взаимодействия с OpenAI) <br>
pandas (библиотека для работы с данными в формате таблиц) <br>
os (встроенная библиотека для работы с операционной системой) <br>

### Использование:
Получите API-ключ OpenAI и установите его в переменную OPENAI_API_KEY. <br>
Подготовьте Excel-файл с отзывами, которые вы хотите проанализировать. Файл должен содержать столбец 'review' с текстом отзывов. <br>
Замените значение переменной filename на путь к вашему Excel-файлу. <br>
Запустите скрипт. Он анализирует каждый отзыв, проставит оценку и сохранит результаты в новом Excel-файле с суффиксом '_analyzed'. <br>

### Примечание:
Обратитесь к документации OpenAI, чтобы получить инструкции по получению API-ключа и дополнительной информации о взаимодействии с API. <br>
Вы можете настроить параметры запроса API, такие как модель (engine), длина ответа (max_tokens), количество вариантов (n), чтобы получить желаемые результаты.
