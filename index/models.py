from django.db import models

# Create your models here.
class Subscriber(models.Model):
    # information's
    email = models.EmailField('E-mail', max_length=63)


    # moderation's
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
        ordering = ('-created_at',)

    def __str__(self):
        return self.email