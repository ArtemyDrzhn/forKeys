from django.contrib import admin
from .models import Questions
from .models import Persons
from django.contrib.auth.models import User
from .models import Answers
from .models import Comments
from .models import Categories

admin.site.register(Questions)
admin.site.register(Persons)
admin.site.register(Answers)
admin.site.register(Comments)
admin.site.register(Categories)

