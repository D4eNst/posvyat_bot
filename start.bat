@echo off

rem Проверяем, существует ли папка venv
if not exist venv (
    echo creating virtual environment ...
    python -m venv venv
)

echo starting virtual environment ...
call venv\Scripts\activate
echo installing files ...
call pip install -r requirements.txt

python main.py

call venv\Scripts\activate

pause