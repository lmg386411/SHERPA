FROM tiangolo/uvicorn-gunicorn:python3.11

# 작업디렉토리 설정
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

### install dependencies ###

# install python packages
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# 현재경로에 존재하는 app의 모든 소스파일을 /code/app 경로 이미지에 복사
COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]