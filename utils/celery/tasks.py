from celery import shared_task
from celery.utils.log import get_task_logger
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


logger = get_task_logger(__name__)


@shared_task(name='send_email_task')
def send_mail_task(subject, template_path, from_email, to_email, context=None):
    if context is None:
        context = {}
    text_content = 'Este email incluye el código QR necesario para entrar en el local.'
    html_content = get_template(template_path).render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()