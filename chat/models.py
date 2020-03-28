from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from micro.models import TimeStampModel
from tasks.models import Task, TaskDeal


UserModel = get_user_model()


class Chat(TimeStampModel):
    room_name = models.CharField(max_length=200, blank=True, null=True)
    deal = models.OneToOneField(TaskDeal, on_delete=models.SET_NULL, 
                                    related_name='deal_chat', blank=True, null=True)
    active = models.NullBooleanField(blank=True, null=True)
    chat_owner = models.OneToOneField(UserModel, on_delete=models.CASCADE, 
                                        related_name='chat_owner')

    def __str__(self):
        return self.room_name

@receiver(post_save, sender=TaskDeal)
def create_chat(sender, instance, created, *args, **kwargs):
    if created and instance.is_accepted == True:
        Chat.objects.create(
            room_name= "Chat for task number " + str(instance.task.id), 
            deal=instance, active=True, chat_owner=instance.task.client
            )



class Message(TimeStampModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='message')
    sender = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='sender_message')
    message = models.TextField()

    def __str__(self):
        return "message (%s) on Chat (%s)"% (self.id, self.chat.id)

# TODO use it when creat message
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# channel_layer = get_channel_layer()

# async_to_sync(channel_layer.group_send)("message_" + str(message_id), 
#                                         {"type": "new message",
#                                         "chat": str(chat_id),
#                                         "sender": str(sender_username),
#                                         "message": str(message),
#                                         })


