from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.



class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='images/avatar_user',verbose_name='آواتار')
    email = models.EmailField(unique=True,verbose_name='ایمیل')
    about_author = models.TextField(null=True,blank=True,verbose_name='درباره کاربر')
    email_active_code = models.CharField(null=True,blank=True,verbose_name='کد فعال سازی ایمیل')
    address = models.TextField(null=True,blank=True,verbose_name='ادرس')


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        else:
            return self.email



