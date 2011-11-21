import facebook

from django.conf import settings


class FacebookStatus(object):
    '''
    Pyres class for submitting status to Facebook.
    '''
    queue = settings.PYRES_DEFAULT_QUEUE

    @staticmethod
    def perform(text):
        '''
        Delayed task.
        '''
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        graph = facebook.GraphAPI(settings.PUBLISHING_FACEBOOK_ACCESS_TOKEN)
        graph.put_object("me", "feed", message=text)