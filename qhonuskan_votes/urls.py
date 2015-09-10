from django.conf.urls import url, patterns

urlpatterns = patterns(
    'qhonuskan_votes.views',

    url(r'^vote/$', view='vote', name='qhonuskan_vote'))
