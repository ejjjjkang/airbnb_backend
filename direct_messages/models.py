from django.db import models
from common.models import CommonModel


# Create your models here.
class ChattingRoom(CommonModel):
    users = models.ManyToManyField("users.User")

class Message(CommonModel):
    """message model definition"""

    text = models.TextField()
    user = models.ForeignKey("users.User",
                             null = True,
                             blank = True,
                             on_delete = models.SET_NULL,
                             )
    
    room = models.ForeignKey("direct_messages.ChattingRoom",
                             on_delete=models.CASCADE,)