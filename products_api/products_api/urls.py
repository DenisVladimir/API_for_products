from django.urls import path
from api.views import ProductCreateView, ProductListView
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),  # add this line
    path('products/', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
]