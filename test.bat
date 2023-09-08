@echo off
echo %cd%
echo %~dp0
call venv\Scripts\activate
python codes.py
call deactivate
pause