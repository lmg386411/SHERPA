FROM openjdk:11-jdk

# 컨테이너가 포트 8080에서 듣도록 설정
EXPOSE 8080

# JAR_FILE 변수 정의
ARG JAR_FILE=./build/libs/adrec-0.0.1-SNAPSHOT.jar

# JAR 파일 메인 디렉토리에 복사
COPY ${JAR_FILE} app.jar

# 시스템 진입점 정의
ENTRYPOINT ["java","-jar","/app.jar"]

ENV TZ=Asia/Seoul
RUN apt-get install -y tzdata
