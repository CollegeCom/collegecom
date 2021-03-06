from django.urls import path
from . import views
urlpatterns = [
    path("chat/", views.chathome, name="chathome"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('chat-search', views.chatsearch, name='chatsearch'),
]