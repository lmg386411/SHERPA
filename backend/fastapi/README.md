# FastApi Usage

> 가상환경 생성 후 라이브러리 설치

📌 python version: 3.11.5

1. 가상환경 생성

   ```bash
   $ pip3 install virtualenv
   $ python -m venv .venv
   $ source .venv/Scripts/activate
   ```

2. package 설치

   ```bash
   $ pip3 install --upgrade pip
   $ pip3 install -r requirements.txt
   ```

<!-- 3. mecab 다운로드

   - Windows 10인 경우

     https://uwgdqo.tistory.com/363를 참고하여 mecab을 설치한다.

   - Ubuntu인 경우

     ```bash
     $ sudo apt-get install curl
     $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
     ``` -->

4. 프로젝트 실행

   ```bash
   $ uvicorn app.main:app
   ```
