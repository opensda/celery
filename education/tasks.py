from celery import shared_task
from django.core.mail import send_mail
from config import settings
from education.models import Subscription
import datetime

from dateutil.parser import *

from users.models import User


@shared_task
def send_upd_info(course_name):
    emails = []
    subs = Subscription.objects.all()
    for sub in subs:
        if sub.is_subscribed == True:
            emails.append(sub.user.email)

    subject = f'Информирование об обновление курса'
    message = f'Курс {course_name} обновился'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails
    )


def deactivate_user():
    users = User.objects.all()
    current_time = datetime.datetime.now()

    for user in users:
        if user.last_login is None:
            continue
        user_time = user.last_login
        u_check_time = user_time + datetime.timedelta(days=30)
        u_check_time_str = u_check_time.strftime("%Y-%m-%d %H:%M:%S")

        if parse(u_check_time_str).timestamp() < current_time.timestamp():
            user.is_active = False
            user.save()

