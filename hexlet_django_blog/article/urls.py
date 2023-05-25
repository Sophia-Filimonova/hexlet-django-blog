from django.urls import path
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<slug:tags>/<int:article_id>/', views.index, name='article'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(),
         name='articles_update'),
    path('<int:id>/delete/', views.ArticleFormDestroyView.as_view(),
         name='articles_destroy'),
    path('<int:id>/', views.ArticleView.as_view(), name='show_article'),
    path('create/', views.ArticleFormCreateView.as_view(),
         name='articles_create'),
]
