from django.urls import path, re_path
from . import views

urlpatterns = [
   
    path('', views.index),
    path('signIn/', views.signIn),
    path('signUp/', views.signUp),
    path('signOut/', views.signOut),
    path('current_user/', views.curr_user),
    path('getInventory/', views.getInventory),
    path('addItem/', views.addItem),
    path('addGatheringItem/', views.addGatheringItem),
    path('deleteItem/', views.deleteItem),
    path('character/', views.character),
    path('myInventory/',views.myInventory),
    path('market/', views.market_inventory),
    path('enemies/', views.get_enemies),
    path('update_xp/<int:user_id>/', views.update_xp),
    re_path(r'.*', views.index, name='index'),
]
