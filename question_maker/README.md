# Deployment Tool: AWS EC2 (ubuntu 22.04)

## 1. 최신 패키지 업데이트

``` shell
# 설치된 패키지의 버전 확인
sudo apt-get update

# 확인된 패키지 버전 업그레이드
sudo apt-get upgrade
```

<br>

## 2. git 설치

```shell
sudo apt-get install git
```

<br>

## 3. python 설치

```shell
sudo apt-get install python3-pip
```

<br>

## 4. 가상환경 생성 및 세팅

```shell
# 루트 폴더로 이동
cd question-maker-django
```

```shell
# venv 패키지 설치
sudo apt-get install python3-venv

# venv라는 이름의 가상환경 생성
python3 -m venv venv

# 가상환경 구동
source venv/bin/activate

# 가상환경에 패키지 설치
pip install -r requirements.txt
```

<br>

## 5. secrets.py 최신화

```shell
# 프로젝트 폴더로 이동
cd question_maker
```

```shell
# vi 편집기 secrets.py 열기
# 파일이 없을 경우 자동생성 후 편집
vi secrets.py
```

### 5-1. vi 편집기 내 동작

1. `i`: 입력 모드(insert mode)로 전환
2. 별도 보관된 `secrets.py` 복사, 붙여넣기
3. `esc`: 입력 모드 종료
4. `:wq`: vi 편집기 종료

<br>

## 6. production_settings.py 최신화

```shell
# vi 편집기 production_settings.py 열기
# 파일이 없을 경우 자동생성 후 편집
vi production_settings.py
```

### 6-1. vi 편집기 내 동작

1. `i`: 입력 모드(insert mode)로 전환
2. 별도 보관된 `production_settings.py` 복사, 붙여넣기
3. `esc`: 입력 모드 종료
4. `:wq`: vi 편집기 종료

<br>

## 7. 백그라운드에서 Django 실행

```shell
nohup python3 manage.py runserver 0:8000 &
```

### 7-1. 백그라운드 실행 로그를 보고 싶은 경우

```shell
# 백그라운드 실행을 하게 되면 자동으로 nuhup.out 파일을 생성해 로그를 남기게 된다.
# 해당 실행 로그를 표기하는 명령어이다.
tail -f nohup.out

# 로그 확인 후 nohup.out 종료
control + c
```

<br>

## 8. 터미널 종료

```shell
# 터미널을 종료해도, 백그라운드 프로세스는 계속 실행된다.
exit
```

<br>

## Django 프로세스 종료를 원하는 경우

```shell
# 8000번 포트 프로세스의 id 확인
sudo lsof -t -i:8000

# 프로세스 종료
kill -9 [프로세스 id]
```

<br>

## 용량이 커진 nohup.out을 비우고 싶은 경우

```shell
cat /dev/null > nohup.out
```





