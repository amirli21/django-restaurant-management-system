from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def detect_user(user):
    roles = {1: 'vendor-dashboard', 2: 'customer-dashboard'}
    if user.role in roles:
        return roles[user.role]
    if user.is_superadmin:
        return '/admin'
    
    
def send_verification_email(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Activation email'
    message = render_to_string
    (
        'accounts/emails/account_verification_email.html',
        {
            'user': user,
            'domain': current_site,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        }
    )
    to_email = user.email
    mail = EmailMessage(mail_subject, message, to=[to_email])
    mail.send()