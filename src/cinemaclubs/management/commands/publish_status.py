from datetime import datetime, timedelta

import redis
from django.utils.translation import ugettext as _
from django.core.management.base import BaseCommand
from django.utils.dateformat import format as django_date
from django.utils import translation
from django.conf import settings

from cinemaclubs.models import CinemaClubEvent
import status
import status.livejournal
import status.facebooklink

REDIS_KEY = 'cinemaclubevent:%s:startsat'
REDIS_EXPIRE = 60 * 60 * 24 * 7  # 7 days in seconds

class Command(BaseCommand):
    help = 'Submit tomorrow events to social networks'

    def handle(self, *args, **options):
        translation.activate('be')

        today = datetime.now()
        tomorrow = today + timedelta(days=1)

        CommandWorker(today, _(u'Today'), self.stdout).publish()
        CommandWorker(tomorrow, _(u'Tomorrow'), self.stdout).publish()

class CommandWorker(object):
    def __init__(self, date, date_text, stdout):
        self.date = date
        self.date_text = date_text
        self.stdout = stdout

    def get_status_text(self, event_text):
        return '%s! %s' % (self.date_text, event_text)

    def filter_new(self, events):
        r = redis.Redis()
        date_str = self.date.strftime('%Y%m%d')

        for event in events:
            key = REDIS_KEY % event.id
            if not r.exists(key) or r.get(key) != date_str:
                r.set(key, date_str)
                yield event

    def get_events(self):
        date_start = datetime(year=self.date.year, month=self.date.month,
                                  day=self.date.day, hour = 0, minute=0,
                                  second=0)
        date_end = datetime(year=self.date.year, month=self.date.month,
                                day=self.date.day, hour = 23, minute=59,
                                second=59)

        date_events = CinemaClubEvent.objects.filter(
            published=True,
            starts_at__gte=date_start,
            starts_at__lte=date_end).order_by('starts_at')

        return self.filter_new(date_events)

    def publish(self):
        date_events = list(self.get_events())

        for event in date_events:
            # Twitter, Vkontakte
            text = self.get_status_text(event.get_short_post())
            url = settings.SITE_URL + event.get_short_url()
            self.stdout.write('Publishing:\n%s\n\n' % text)
            status.publish(text, url)

            # Facebook
            text = self.get_status_text(event.get_post())
            url = settings.SITE_URL + event.get_absolute_url()
            image = settings.SITE_URL + event.get_image_url()
            status.facebooklink.publish(text, url, image)

        if date_events:
            # Livejournal
            lj_subject = u'%s :: %s' % (django_date(self.date, "l, j E"),
                                        settings.SITE_NAME)
            lj_html = '<br />'.join(e.get_html_post() for e in date_events)
            status.livejournal.publish(lj_subject, lj_html)
