from django.db import models

# Create your models here.


class Classes(models.Model):

    class_number = models.IntegerField()
    def __str__(self):
        return " {} فصل رقم ".format(self.class_number)



class Professor(models.Model):

    prof_name = models.CharField(max_length=220, )
    Classes = models.ManyToManyField(Classes)

    def __str__(self):
        return "Pro : {}" .format(self.prof_name)

class Student(models.Model):

    name = models.CharField(max_length=220, )
    age = models.IntegerField()
    address = models.CharField(max_length=220, )
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='std_pic', null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
