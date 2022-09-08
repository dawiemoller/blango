from django.urls import path
from blog import views
import debug_toolbar
from django.urls import path, include
from django.conf import settings

urlpatterns = [
  path('',views.index),
  path("post/<slug>/", views.post_detail, name="blog-post-detail"),
  path("ip/", views.get_ip),

]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]