

from django.urls import path



from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('brew-guide',views.brew_guide,name='brew-guide'),
    path('partnerships',views.partnerships,name='partnerships'),
    path('ourstory',views.ourstory,name='ourstory'),
]