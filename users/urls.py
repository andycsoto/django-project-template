""" this document defines the users app urls """
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'users.views',
    url(
        r'^login/$',
        'login',
        name='login'
    ),
    url(
        r'^password-change/$',
        'password_change',
        name='password_change'
    ),
    url(
        r'^logout/$',
        'logout',
        name='logout'
    ),
    url(
        r'^register/$',
        'user_new',
        name='register',
    ),
    url(
        r'^password-email-sent/$',
        'password_reset_email_sent',
        name='password_email_sent'
    ),
    url(
        r'^password-reset/$',
        'password_reset',
        name='password_reset'
    ),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        'password_reset_confirm',
        name='password_reset_confirm'
    ),

    url(
        r'^verify/(?P<uidb36>[0-9A-Za-z]{1,13})-'
        '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'user_new_confirm',
        name='user_new_confirm'
    ),

    url(
        r'^reset/done/$',
        'password_reset_complete',
        name='password_reset_complete'
    ),
    url(
        r'^edit/$',
        'user_edit',
        name='user_edit'
    ),
    url(
        r'^profile/$',
        'user_profile',
        name='user_profile'
    ),
)
