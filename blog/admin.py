from django.contrib import admin
from .models import Questions
from .models import Users
from .models import Answers
from .models import Comments
from .models import Categories

admin.site.register(Questions)
admin.site.register(Users)
admin.site.register(Answers)
admin.site.register(Comments)
admin.site.register(Categories)

