
from django.urls import path
from aasha import views


urlpatterns=[
    
    path('about',views.about,name='about'),
    path('course_details',views.course_details,name='course_details'),
    path('index',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('events',views.events,name='events'),
    path('courses',views.courses,name='courses'),
    path('pricing',views.pricing,name='pricing'),
    path('trainers',views.trainers,name='trainers'),

]


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=50)
    description = models.TextField(default='Its too yummy')
    image = models.ImageField(upload_to='images')
    order_status = models.BooleanField(default=False)
    items = models.IntegerField(default=0)

    def __str__(self):
        return self.name