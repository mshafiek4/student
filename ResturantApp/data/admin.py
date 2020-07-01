from django.contrib import admin
from  .models import Professor, Student, Classes

# Register your models here.

admin.site.register([Professor, Student, Classes])
