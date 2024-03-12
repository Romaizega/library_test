from library.celery import app
from celery import shared_task
import time
from community.models import Events


@shared_task
def create_event_with_delay(title, description, organizations, image, date):
    time.sleep(60)

    Events.objects.create(
        title=title,
        description=description,
        image=image,
        date=date
    )
