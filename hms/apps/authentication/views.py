# Copyright (C) 2021 Ibrahem Mouhamad

from rest_auth.registration.views import RegisterView as _RegisterView
from allauth.account import app_settings as allauth_settings

class RegisterView(_RegisterView):
    def get_response_data(self, user):
        data = self.get_serializer(user).data
        data['email_verification_required'] = allauth_settings.EMAIL_VERIFICATION == \
            allauth_settings.EmailVerificationMethod.MANDATORY

        return data
