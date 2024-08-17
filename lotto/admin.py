from django.contrib import admin
# 불러오려는 파일이 현재 파일과 동일한 폴더에 있으면 상위 폴더명 생략 가능
from .models import GuessNumbers
# from lotto.models import GuessNumbers

# Register your models here.
admin.site.register(GuessNumbers)
