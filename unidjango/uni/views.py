from django.http import HttpResponse
from django.views.generic.simple import direct_to_template

import facebook.djangofb as facebook

from uni.models import User

@facebook.require_login()
def canvas(request):
    try:
        newUser = User()
        newUser.uid = request.facebook.uid
        newUser.year = 'Freshman'
        newUser.majorId = 1
        newUser.save()
    except Exception as e:
        return
    
    # User is guaranteed to be logged in, so pass canvas.fbml
    # an extra 'fbuser' parameter that is the User object for
    # the currently logged in user.
    return direct_to_template(request, 'favlang/canvas.fbml', extra_context={'fbuser': user})

def enrollClass(cid, request):
    try:
        # Adds uid, cid to Enroll table
        newEnroll = new Enroll()
        newEnroll.uid = request.facebook.uid
        newEnroll.cid = cid
        newEnroll.save()
    except Exception as e:
        return
    
    return

def rateCourse(cid):
    
    