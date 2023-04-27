from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # チャットルームの一覧作成
    path('', views.Index.as_view(), name='index'),
    # チャットルームの作成
    path('create/room', views.CreateRoom.as_view(), name='create_room'),
    # チャットルームの更新
    path('update/room/<int:pk>', views.UpdateRoom.as_view(), name='update_room'),
    # チャットルームの削除
    path('delete/room/<int:pk>', views.DeleteRoom.as_view(), name='delete_room'),
    # チャットルームへの入室
    path('enter/room/<int:pk>', views.EnterRoom.as_view(), name='enter_room'),
]