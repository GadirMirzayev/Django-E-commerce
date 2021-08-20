from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True,)
    GENDER_CHOICES = (
        (1, 'Man'),
        (2, 'Woman'),
    )
    image = models.ImageField('Image', upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)
    gender = models.IntegerField('Gender', choices=GENDER_CHOICES, default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name' , 'last_name']

    @property
    def profile_picture(self):
        if self.image:
            return self.image.url
        return "https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png" 

    def get_absolute_url(self):
        return reverse_lazy('index:home')