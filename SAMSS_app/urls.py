from django.urls import path
from SAMSS_app import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("courses/", views.CoursesView.as_view(), name="courses"),
    path("teacher", views.TeacherView.as_view(), name="teacher"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("pricing/", views.PricingView.as_view(), name="pricing"),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("courses_create/", views.CouresCreateView.as_view(), name="courses_create"),
]