# 📝 Word Segmentation (Avito Intern Task)

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📌 Описание
Проект решает задачу восстановления пробелов в русском тексте, где они были удалены (например, после OCR или ASR).  
Метрика качества — **F1 по позициям пробелов**.

Используется **динамическое программирование (DP)** + словарь частотности слов из пакета [`wordfreq`](https://github.com/rspeer/wordfreq).

---

## 📂 Структура проекта
```
avito_intern/
│── data/
│ └── data.txt # входной файл (скачивается со Stepik)
│── src/
│ ├── segmenter.py # реализация DP-сегментатора
│ ├── test_segmenter.py # unit-тесты
│ └── run.py # основной скрипт для генерации submission.csv
│── requirements.txt # зависимости
│── README.md # документация
│── .gitignore # игнорируем лишние файлы
```

---

## 🚀 Установка
```
git clone git@github.com:V1a6imir/Avito-intern.git
cd Avito-intern
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## ▶️ Запуск
Скачайте [`dataset_1937770_3.txt`](https://stepik.org/api/attempts/1471200512/file) с Stepik и положите в папку data/.

Выполните:
```
python src/run.py
```
В корне проекта появится файл submission.csv. Его можно загрузить на Stepik.

🧪 Тесты
Для проверки работы сегментатора на примерах:

```
python src/test_segmenter.py
```
📊 Пример submission.csv
```
id,predicted_positions
0,"[5, 11, 14]"
1,"[3, 6, 7, 19]"
2,"[4, 12, 13, 21, 22, 29]"
```
