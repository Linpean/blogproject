from django.db import models
from django.utils.six import python_2_unicode_compatible


#评论
class Comment(models.Model):
    name = models.CharField(max_length = 100)   #评论用户名称
    email = models.EmailField(max_length = 255) #邮箱
    url = models.URLField(blank = True)         #个人网站地址
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True) 
    #auto_now_add 的作用是，当评论数据保存到数据库时，
    #自动把 created_time 的值指定为当前时间。created_time 
    #记录用户发表评论的时间，我们肯定不希望用户在发表评论时
    #还得自己手动填写评论发表时间，这个时间应该自动生成。
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]

