from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(TestQuestion)
admin.site.register(Answer)
admin.site.register(Result)
