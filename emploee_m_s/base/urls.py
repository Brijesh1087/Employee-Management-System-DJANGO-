from django.urls import path
from . import views
urlpatterns = [	
	path('',views.index,name='index'),
	path('add_emps/',views.add_emps,name='add_emps'),
	path('rem_emps/',views.rem_emps,name='rem_emps'),
	path('rem_emps/<int:emps_id>',views.rem_emps,name='rem_emps/id'),
	path('filter/',views.filter,name='filter'),
]