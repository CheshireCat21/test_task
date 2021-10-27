from django.urls import path

from message.views import MessageListView, MessageSingleView, MessageCreateView

urlpatterns = [
    path('messages/list/<int:block_number>', MessageListView.as_view(), name='messages_list'),
    path('messages/single/<int:id>', MessageSingleView.as_view(), name='single_message'),
    path('messages/create', MessageCreateView.as_view(), name='create_message')
]