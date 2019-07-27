from django.db import models

# Create your models here.
class Blog(models.Model):
    
    title = models.CharField(max_length = 30) # 타이틀 길이 200 제한 ( 짧은 문자 CharField )
    genre = models.CharField(max_length = 20) # 영화 장르
    rating = models.CharField(max_length = 20) # 영화 평점
    notice = models.CharField(max_length = 20) #영화를 한마디로
    save_date = models.DateTimeField('Movie Release date') # 영화 개봉 날짜
    image = models.ImageField(upload_to="image/") # 이미지
    body = models.TextField() # 본문
    pub_date = models.DateTimeField(auto_now_add=True) # 게시 날짜

    def __str__(self):
        return self.title