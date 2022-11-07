from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("user/", views.create_user, name="create-user"),
    path("company/", views.create_company, name="create-company")
]
