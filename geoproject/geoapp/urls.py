from django.urls import path
from .views import run_docker_container
from .views import default_view
from .views import check_jupyterlab_status
from .views import check_error_messages

urlpatterns = [
   path('', default_view, name='default_view'), 
   path('run_docker/', run_docker_container, name='run_docker'),
   path('check_jupyterlab_status/', check_jupyterlab_status, name='check_jupyterlab_status'),
   path('check_error_messages/', check_error_messages, name='check_error_messages'),
]
