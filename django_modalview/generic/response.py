import json

from django.http.response import HttpResponse


class ModalJsonResponse(HttpResponse):

	content_type = 'application/json'

	def __init__(self, content, *args, **kwargs):
		super(ModalJsonResponse, self).__init__(self.get_content(content,
																**kwargs),
												ModalJsonResponse.content_type,
												*args, **kwargs)

	def get_content(self, content, **kwargs):
		json_dict = {
			'content': content,
		}
		return json.dumps(json_dict)


class ModalHttpResponse(HttpResponse):

	def __init__(self, content, *args, **kwargs):
		super(ModalHttpResponse, self).__init__(content, *args, **kwargs)



