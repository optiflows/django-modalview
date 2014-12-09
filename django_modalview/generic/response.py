import json

from django.http import HttpResponse
from django.core.exceptions import ImproperlyConfigured


class BaseModalJsonResponse(HttpResponse):
    content_type = 'application/json'

    def __init__(self, *args, **kwargs):
        jsn_content = json.dumps(self.get_content())
        super(BaseModalJsonResponse, self).__init__(jsn_content,
                                                    self.content_type,
                                                    *args, **kwargs)

    def get_content(self):
        raise ImproperlyConfigured("No method get_content")


class ModalJsonResponse(BaseModalJsonResponse):

    type = 'normal'

    def __init__(self, content, *args, **kwargs):
        self.modal_content = content
        super(ModalJsonResponse, self).__init__(*args, **kwargs)

    def get_content(self):
        return {
            'type': self.type,
            'content': self.modal_content
        }


class ModalJsonResponseRedirect(BaseModalJsonResponse):
    type = 'redirect'

    def __init__(self, redirect_to, *args, **kwargs):
        self.redirect_to = redirect_to
        super(ModalJsonResponseRedirect, self).__init__(*args, **kwargs)

    def get_content(self):
        return {
            'type': self.type,
            'redirect_to': self.redirect_to
        }
