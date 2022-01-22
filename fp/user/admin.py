from django.contrib import admin #장고에서 어드민 모델을 사용하겠다.
from .models import UserModel #지금우리의 위치와 동일하게있는 파이썬 파일을 불러온뒤
#그중에서 usermodel을 가져오겠다.

# Register your models here.
admin.site.register(UserModel) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다