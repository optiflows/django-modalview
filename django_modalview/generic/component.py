GET_TEMPLATE = "django_modalview/modal.html"
GET_TEMPLATE_CONTENT = "django_modalview/modal_get_content.html"
FORM_TEMPLATE = "django_modalview/modal.html"
FORM_TEMPLATE_CONTENT = "django_modalview/modal_form_content.html"
LAST_FORM_TEMPLATE = "django_modalview/form_content.html"
BASE_TEMPLATE = "django_modalview/base.html"


class ModalButton(object):

    def __init__(self, value=None, button_type='info',
                 display=True, url=None, loading_value="loading...", *args, **kwargs):

        super(ModalButton, self).__init__(*args, **kwargs)
        self.value = value
        self.display = display
        self.type = button_type
        self.url = url
        self.loading_value = loading_value


class ModalResponse(object):

    def __init__(self, text='Result', result='info'):
        self.text = text
        self.result = result
