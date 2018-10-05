
import urllib
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from django.urls import reverse
import movecar.settings as setting

class AuthView(View):
    def dispatch(self, request, *args, **kwargs):
        if not ('user' in request.session):
            path = request.get_full_path()
            red_url = '%s?path=%s' % (reverse('wx_auth'), urllib.quote(path))
            return redirect(red_url)

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed

        return handler(request, *args, **kwargs)
