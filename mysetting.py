# my_settings.py

DATABASES = {
    'default':{
        # 1. 사용할 엔진 설정
        'ENGINE': 'django.db.backends.mysql',
        # 2. 연동할 MySQL의 데이터베이스 이름
        'NAME': 'HELLO',
        # 3. DB 접속 계정명  / 연결할 db에 따라 다를 수 있음
        'USER': 'root',
        # 4. DB 패스워드
        'PASSWORD': 'wngh4242730!',
        # 5. DB 주소 / 연결할 db에 따라 다를 수 있음
        'HOST': 'localhost',
        # 6. 포트번호
        'PORT': '3306',
    }
}
SECRET_KEY = 'django-insecure-4wnrdn4wuk2xvz3j4d8d6th8t&xl*vjutwh%(_ej4okv1y32t1'