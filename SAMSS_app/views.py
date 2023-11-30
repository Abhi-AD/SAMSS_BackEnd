from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "SAMSS/index.html"

class CoursesView(TemplateView):
    template_name = "SAMSS/courses.html"


class TeacherView(TemplateView):
    template_name = "SAMSS/teacher.html"

class AboutView(TemplateView):
    template_name = "SAMSS/about.html"

class PricingView(TemplateView):
    template_name = "SAMSS/pricing.html"
    
class BlogView(TemplateView):
    template_name = "SAMSS/blog.html"

class ContactView(TemplateView):
    template_name = "SAMSS/contact.html"
    
class LoginView(TemplateView):
    template_name = "SAMSS/login.html"
    
class CouresCreateView(TemplateView):
    template_name = "SAMSS/courescreate.html"
    
