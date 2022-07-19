from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict





# Create your models here.
class User(AbstractUser):    

    def toJSON(self):
        item = model_to_dict(self, exclude=['password','id','is_superuser','username','first_name','last_name','email','is_staff','is_active','groups'])
        if self.last_login:
            item['last_loginfor'] = self.last_login.strftime("%Y")
        item['date_joinedfor'] = self.date_joined.strftime("%Y")
        
        return item
    
    def __str__(self) -> str:
        return self.last_login.strftime("%Y")
        
    class Meta:        
        db_table="auth_user"

   
