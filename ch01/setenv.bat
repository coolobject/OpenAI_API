@echo off
echo [1] Create folder
rmdir openai && mkdir openai && cd openai

echo [2] Create venv...
python -m venv myenv

echo [3] Activate venv...
call .\myenv\Scripts\activate

echo [4] Install packages...
python -m pip install --upgrade pip
pip install openai python-dotenv ipykernel

echo [5] register venv myenv
python -m ipykernel install --user --name=myenv

echo Done!
pause
