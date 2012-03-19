import django.dispatch


user_signed_up = django.dispatch.Signal(providing_args=["user"])
user_sign_up_attempt = django.dispatch.Signal(providing_args=["username",  "email", "result"])
signup_code_sent = django.dispatch.Signal(providing_args=["signup_code"])
signup_code_used = django.dispatch.Signal(providing_args=["signup_code_result"])
email_confirmed = django.dispatch.Signal(providing_args=["email_address"])
email_confirmation_sent = django.dispatch.Signal(providing_args=["confirmation"])