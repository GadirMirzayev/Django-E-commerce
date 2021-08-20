from django.db import models

# Create your models here.
class Contact_Info(models.Model):
    name = models.CharField('Name',max_length=127)
    email = models.EmailField('E-mail', max_length=63)
    subject = models.CharField('Subject', max_length=127)
    message = models.TextField('Message')

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name