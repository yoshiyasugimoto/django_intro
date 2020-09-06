from django.urls import path
from . import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('book/', views.book_list, name='book_list'),  # 一覧
    path('book/add/', views.book_edit, name='book_add'),  # 登録
    path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),
    path('book/del/<int:book_id>/', views.book_del, name='book_del'),
]
