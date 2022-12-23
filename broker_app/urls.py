from . import views
from django.urls import path,include

urlpatterns=[
    path('',views.admin_login,name='login'),
    path('index',views.index,name='index'),
    path('add_investor',views.add_investor,name='add_investor'),
    path('list_investors',views.list_investors,name='list_investors'),
    path('add_project',views.add_project,name="add_project"),
    path('list_projects',views.list_projects,name="list_projects"),
    path('view_project/<str:name>',views.view_project,name='view_project'),
    path('add_profit',views.add_profit,name='add_profit'),
    path('view_profit',views.view_profit,name='view_profit'),
    path('view_payments',views.view_payments,name="view_payments"),
    path('add_payment',views.add_payment,name='add_payment'),
    path('statements',views.statements,name="statements")
]
