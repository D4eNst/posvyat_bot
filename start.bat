@echo off

rem Проверяем, существует ли папка venv
if not exist venv (
    echo Создание виртуального окружения...
    python -m venv venv
    pip install -r requirements.txt
)

call venv\Scripts\activate

python main.py

call venv\Scripts\activate

pause