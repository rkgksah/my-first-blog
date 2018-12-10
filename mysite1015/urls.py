from django.conf.urls import include, url
from django.contrib import admin
#from bookmark.views import bookmark_list, bookmark_detail 
from mysite1015.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]
