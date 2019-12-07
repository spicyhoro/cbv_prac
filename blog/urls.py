from django.urls import include, path, re_path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.greeting),
    path('morning/', views.morning_greeting),
    path('evening/', views.evening_greeting),
    path('<int:pk>/edit/', views.post_edit),
    path('posts/', views.index, name='post_index'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    path('archive/', views.post_archive),
    re_path(r'^archive/(?P<year>\d{4})/$', views.PostYearArchiveView.as_view(), name='post_archive_year'),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.PostMonthArchiveView.as_view(), name='post_archive_month'),
    re_path('^archive/(?P<year>\d{4})/week/(?P<week>\d{1,2})/$', views.PostWeekArchiveView.as_view(), name='post_archive_week'),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/', views.PostDayArchiveView.as_view(), name='post_archive_day'),
    re_path(r'^archive/today/$', views.PostTodayArchiveView.as_view(), name='post_archive_today'),
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<pk>\d+)/$', views.PostDateDetailView.as_view(), name='post_archive_today'),
]