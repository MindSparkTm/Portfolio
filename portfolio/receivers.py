from django.dispatch import receiver
from .signals import *

@receiver(test_signal)
def send_mail_on_publish(sender, **kwargs):
    # contains the logic to send the email to author.
    print('User',sender)