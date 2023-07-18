from django.urls import path
from . import views 


urlpatterns = [
    # path('', views.news_list, name='news'),
    path('', views.NewsListView.as_view(), name='news'),
    # path('detail/<str:slug>/<int:id>', views.news_detail, name='news_detail'),
    path('detail/<str:slug>/<int:id>', views.NewsDetailView.as_view(), name='news_detail'),
    path("add/", views.NewsCreateView.as_view(template_name="add_news.html"), name="news_add"),
    path("update/<int:pk>/", views.NewsUpdateView.as_view(template_name="update_news.html"), name="news_update"),
    path("delete/<int:pk>", views.NewsDeleteView.as_view(template_name="delete_news_confirmation.html"), name="news_delete"),
    path("update/comment/<int:pk>/", views.CommentUpdateView.as_view(template_name="update_comment.html"), name="comment_update"),
    path('delete/comment/<int:pk>/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('report/comment/<int:pk>/', views.CommentReportView.as_view(), name='comment_report')
]