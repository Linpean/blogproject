from django.conf.urls import url
from . import views # 从当前目录下导入views

app_name = 'blog'
urlpatterns =[
	url(r'^$', views.index, name='index'), 
	url(r'^post/(?P<pk>[0-9]+)/$',views.detail, name = 'detail')
]



