from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from issues.views import HomeView
from toucan.invitations.views import InvitedSignupView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # these next 2 lines are important!
    url(r'^accounts/signup/', InvitedSignupView.as_view(), name='account_signup'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^invitations/', include('toucan.invitations.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^org/', include('organisations.urls', 'organisations')),
    url(r'^issues/', include('issues.urls', 'issue_app')),
    url(r'^profile/', include('user_profile.urls', 'user_profile')),
    url(r'^about/$', TemplateView.as_view(template_name='default/landing_page.html'), name='landing_page'),
]


if settings.DEBUG:

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    url(r'^issue/(?P<issue_id>\d+)', HomeView.as_view(), name='home_issue'),
    url(r'^', HomeView.as_view(), name='home'),  # => Single Page App

]


