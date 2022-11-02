from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.login,name='login'),
   path('',views.logout,name='logout'),
   path('dashboard/',views.dashboard,name="dashboard"),
   # ###############customer################################
   path('new_customer/',views.new_customer,name = "new_customer"),
   path('delete_customer/<int:id>',views.delete_customer,name="delete_customer"),
   path('manage_customer/',views.manage_customer,name="manage_customer"),
   path('edit_customer/',views.edit_customer,name="edit_customer"),
   # ############# imigani ####################################
   path('new_herbal/',views.add_herbal,name = "add_herbal"),
   path('manage_herbal/',views.manage_herbal,name="manage_herbal"),
   path('delete_herbal/<int:id>',views.delete_herbal,name="delete_herbal"),
   # ############# herbal ####################################
   path('add_imigani/',views.add_imigani,name="add_imigani"),
   path('manage_imigani/',views.manage_imigani,name="manage_imigani"),
   path('delete_imigani/<int:id>',views.delete_imigani,name="delete_imigani"),
   ############################################################
   path('add_amateka/',views.add_amateka,name="add_amateka"),
   path('manage_amateka/',views.manage_amateka,name="manage_amateka"),
   path('delete_amateka/<int:id>',views.delete_amateka,name="delete_amateka"),
   ###########################################################
   path('add_diy/',views.add_diy,name="add_diy"),
   path('manage_diy/',views.manage_diy,name="manage_diy"),
   path('delete_diy/<int:id>',views.delete_diy,name="delete_diy"),
   ###########################################################
   path('add_sakwe/',views.add_sakwe,name="add_sakwe"),
   path('manage_sakwe/',views.manage_sakwe,name="manage_sakwe"),
   path('delete_sakwe/<int:id>',views.delete_sakwe,name="delete_sakwe"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)