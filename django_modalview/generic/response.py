import json

from django.http.response import HttpResponse


class ModalJsonResponse(HttpResponse):

    content_type = 'application/json'
    response_type = 'normal'

    def __init__(self, content='empty', response_type='normal',
                 redirect_to='none', *args, **kwargs):
        opt = {
            'response_type': response_type,
            'redirect_to': redirect_to
        }
        super(ModalJsonResponse, self).__init__(self.get_content(content,
                                                                 **opt),
                                                self.content_type, *args,
                                                **kwargs)

    def get_content(self, content, **kwargs):
        json_dict = {
            'type': kwargs['response_type'],
            'content': content,
            'redirect_to': kwargs['redirect_to']
        }
        return json.dumps(json_dict)


class ModalHttpResponse(HttpResponse):

    def __init__(self, content, *args, **kwargs):
        super(ModalHttpResponse, self).__init__(content, *args, **kwargs)
