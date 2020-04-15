from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    """
    one-to-one model, one user can have one account

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
                              upload_to='static/images/profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Commented out since it does not work with S3 this way
    # If I want to use this in need to use the 'AWS lambda function' that resizes automatically when they are uploaded to S3

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
