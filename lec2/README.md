# Data Engineering Homework — Sales API Extraction and Transformation

## Структура проєкту

```
lec2/
├── file_storage/
│   ├── raw/
│   └── stg/
├── job1/
│   ├── main.py
│   └── bll/
│       └── sales_api.py
├── job2/
│   ├── main.py
│   └── bll/
│       └── transform.py
├── .env
├── requirements.txt
├── test_job1.py
├── test_job2.py
```

## Налаштування

1. У `.env` файл у папці `lec2/` додати API_AUTH_TOKEN

2. Встановити залежності:

```
pip install -r lec2/requirements.txt
```

## Запуск

1. Запустити сервер першої джоби:

```
python lec2/job1/main.py
```

2. У новому терміналі запустити сервер другої джоби:

```
python lec2/job2/main.py
```

3. Викликати тестовий запит на першу джобу:

```
python lec2/test_job1.py
```

4. Викликати тестовий запит на другу джобу:

```
python lec2/test_job2.py
```

## Результат

- Після `test_job1.py`: файли JSON з'являються в `lec2/file_storage/raw/sales/2022-08-09/`
- Після `test_job2.py`: файли Avro з'являються в `lec2/file_storage/stg/sales/2022-08-09/`