from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('thanks/<int:submission_id>/', views.thanks_view, name='thanks'),
]
