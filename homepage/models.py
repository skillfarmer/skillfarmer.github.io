from django.db import models

# Create your models here.

class SignUp(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=10)
    join_date = models.DateField()
    region = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fname 
    
    def verifyFields(self):
        i = 0
        if self.fname.isalpha():
            i+=1
        if self.lname.isalpha():
            i+=1
        if not self.state.isnumeric():
            i+=1
        if self.city.isalpha():
            i+=1
        if self.region.isalpha():
            i+=1
        if self.pincode.isnumeric():
            i+=1
        if self.phoneno.isnumeric() and len(self.phoneno) >=10:
            i+=1
        if len(self.password)>=8:
            i+=1
        
        if i>=8 :
            return True
        else:
            return False
