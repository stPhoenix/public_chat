from django.urls import path
from api.views import MessageCreate, MessageDetail, MessageList

urlpatterns = [
    path('messages/list/<int:page>', MessageList.as_view(), name='messages_list'),
    path('messages/single/<int:pk>', MessageDetail.as_view(), name='messages_detail'),
    path('messages/add', MessageCreate.as_view(), name='messages_add'),
]