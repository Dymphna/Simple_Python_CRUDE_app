from django.urls import path

from .views import(
    crude_list,
    crude_detail,
    crude_create,
    crude_update,
    crude_delete
)


app_name = 'crudes'
urlpatterns =[
    path('', crude_list),
    path('create/', crude_create),
    path('<id>/', crude_detail),
    path('<id>/update/', crude_update),
    path('<id>/delete/', crude_delete)
]
