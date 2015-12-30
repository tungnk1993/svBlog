from requests import request, HTTPError
from django.core.files.base import ContentFile

from .models import MyUser

def save_profile(backend, user, response, *args, **kwargs):
    print "Saving profile is called"
    if backend.name == 'facebook':
        (profile, created) = MyUser.objects.get_or_create(user_id=user.id)
        print "User instance", user.__dict__
        print "Response instance", response

        profile.name = response['name']
        profile.user.email = response['email']

        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        try:
            response_large = request('GET', url, params={'type': 'large'})
            response_icon = request('GET', url, params={'type': 'square'})
            response_large.raise_for_status()
            response_icon.raise_for_status()
        except HTTPError:
            print "Error getting picture"

        if not created:
            # delete previous image
            import os
            from django.conf import settings
            os.remove(os.path.join(settings.MEDIA_ROOT, str(profile.profile_pic.name)))
            print "Deleted previous profile image"

        profile.profile_pic.save('{0}_social.jpg'.format(user.username),
                                   ContentFile(response_large.content))
        profile.profile_icon.save('{0}_icon.jpg'.format(user.username),
                                   ContentFile(response_icon.content))
        profile.save()