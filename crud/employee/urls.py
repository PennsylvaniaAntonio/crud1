from django.urls import path
from django.urls.conf import include
from employee import views

urlpatterns = [
    path('emp',views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy)
]