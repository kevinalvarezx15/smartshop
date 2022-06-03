from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict





# Create your models here.
class User(AbstractUser):    

    def toJSON(self):
        item = model_to_dict(self, exclude=['password','id','is_superuser','username','first_name','last_name','email','is_staff','is_active','groups'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        
        return item
        
    class Meta:
        db_table="auth_user"

   
