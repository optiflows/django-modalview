# django-modalview

Django app to build bootstrap modal with new class based views and jquery plugin.

## Installation

You can get django-modalview from PyPi:
```bash
pip install django-modalview
```

To use it you should add it to your `INSTALLED_APPS` in `settings.py`.
```python
INSTALLED_APPS = (
    ...
    'django-modalview',
    ...
)
```

## Usage

Django-modalview permit you to build modal with class based view. To use these news behaviors you have to inherit of one of these classes, define the url to call this new view and add a jquery to define the DOM element that will call this view.

### Example

To begin, I am going to show you how to build the most simple modalview.

views.py
```python
...
from django_modalview.generic.base import ModalTemplateView

...

class MyModal(ModalTemplateView):
    '''
         This modal inherit of ModalTemplateView, so it just display a text without logic.
    '''
    def __init__(self, *args, **kwargs):
        '''
            You have to call the init method of the parent, before to overide the values:
                - title: The title display in the modal-header
                - icon: The css class that define the modal's icon
                - description: The content of the modal.
                - close_button: A button object that has several attributes.(explain below)
        '''
        super(MyModal, self).__init__(*args, **kwargs)
        self.title = "My modal"
        self.description = "This is my description"
        self.icon = "icon-mymodal"
        
```

urls.py
```python
  '''
    You have to define your url like with the other class based views
  '''
  from myapp.views import MyModal
  
  urlpatterns = patterns(...
      url(r'^mymodal/', MyModal.as_view(), name='mymodal'),
  ...)

```

mymodal.js
```javascript
    $('#my_modal_runner').DjangoModalRunner();
```

base.html
```html
    <!doctype html>
    <html lang="en">
      <head>
         ...
         //If you use your own bootstrap files you can use them.
        <link rel="stylesheet" href="{% static 'django_modalview/css/bootstrap.min.css' %}" type="text/css" />
        <link rel="stylesheet" href="{% static 'django_modalview/css/modal.css' %}" type="text/css" />
        ...
        <script type="text/javascript" src="{% static 'your jquery files' %}></script>
        <script type="text/javascript" src="{% static 'django_modalview/js/bootstrap.min.js' %}></script>
        <script type="text/javascript" src="{% static 'django_modalview/js/django_modal_view.js' %}></script>
        <script type="text/javascript" src="{% static 'myapp/js/mymodal.js" %}></script>
      </head>
      <body>
        <button id="my_modal_runner">Display modal </button>
      </body>
    </html>
```

This is the most simple case. In the next parts I am going to show you how to add logic in the class based views but also in the Jquery plugin.

## New Class Based Views:

This app add several class based views. As you seen in the example the first is the ModalTemplateView. In this part I will explain the goal of each one.

### ModalTemplateView

This class permit to display a modal without logic. It is stored in django-modalview.generic.base. To see an example read the first example of this doc.

### ModalTemplateUtilView

This class inherit of ModalTemplateView and add a new button. This new button named `util_button` permit to run a method on a GET request. This method may overload the context of the modal to display new datas.

example:
```python
    from django_modalview.generic.base import ModalTemplateUtilView
    from django_modalview.generic.component import ModalResponse
    ...
    
    class MyModalTemplateUtilView(ModalTemplateUtilView):
    
        def __init__(self, *args, **kwargs):
            super(MyModalTemplateUtilView, self).__init__(*args, **kwargs)
            self.title = "My title"
            ...
            #self.util_button has a default value. In the components part you will see how to overide it
            #self.util_name is the name of the method that will be run. The default value is 'util', you can overide it

        def util(self, url_param, *args, **kwargs):
            '''
                 url_param is the name of an url parameter. If you don't have url parameters change the signature.
            '''
            if url_param == 'check':
                self.response = ModalResponse('good game', 'success') #explain in the component part
            else:
                self.response = ModalResponse('Try again', 'danger')
```
In this example the util method is usefull to check an argument value. The response will be displayed in the modal after the click on the submit button. The other files use the same logic that in the first example.

### ModalFormView 

This class permit to handle a django Form in a modal view. A new button named `submit_button` is add in the context.
By default, when the form is invalid, the error are displayed in the modal.

example:
```python
   
    from django_modalview.generic.edit import ModalFormView
    from django_modalview.generic.component import ModalResponse
   
    from myapp.forms import MyForm
    
    class MyFormModal(ModalFormView):
    
        def __init__(self, *args, **kwargs):
            super(MyFormModal, self).__init__(*args, **kwargs)
            self.title = "My title"
            ...
            self.form_class = MyForm #You django form
            #self.submit_button has a default value
        
        def form_valid(self, form, **kwargs):
            self.response = ModalResponse('Form valid', 'success')
    
```

/!\ TO USE A MODAL WITH FORM YOU HAVE TO ADD A SCRIPT IN YOUR HTML HEADER

```html
  <doctype>
  ...
  <head>
      ...
      <script type="text/javascript" src="{% static 'django_modalview/js/jquery.form.js' %}></script>
  </head>
  ...
  
```

### ModalCreateView
  This class permit to handle a django modelform to create a new instance of object. As for the ModalFormView, the `submit_button` is added to the context. By default, when the form is invalid, the error are displayed in the modal.
  
example:

```python
    from django_modalview.generic.edit import ModalCreateView
    from django_modalview.generic.component import ModalResponse
   
    from myapp.forms import MyModelForm
    
    
    class MyCreateModal(ModalCreateView):
        
        def __init__(self, *args, **kwargs):
            super(MyCreateModal, self).__init__(*args, **kwargs)
            self.title = "My modal"
            ...
            self.form_class = MyModelForm
        
        def form_valid(self, form, **kwargs):
            '''
                The form_valid have to return the parent form_valid.
                In this example I will show you the two most populare case.
                The first you want just display a success message without the new object
            '''
            self.response = ModalResponse("Good game", "success")
            return super(MyCreateModal, self).form_valid(form, **kwargs)
            
            '''
                The second, you want use the new object
            '''
            self.save(form) #When you save the form an attribute name object is created.
            self.response = ModalResponse("{obj} is created".format(obj=self.object), 'success')
            #When you call the parent method you set commit to false because you have save the object.
            return super(MyCreateModaln self).form_valid(form, commit=False, **kwargs)
```
        
/!\ TO USE A MODAL WITH FORM YOU HAVE TO ADD A SCRIPT IN YOUR HTML HEADER

```html
  <doctype>
  ...
  <head>
      ...
      <script type="text/javascript" src="{% static 'django_modalview/js/jquery.form.js' %}></script>
  </head>
  ...
  
```        

### ModalUpdateView

This class permit to handle a modelform to update an object. It has the same behaviors of the ModalCreateView.

```python
    from django.contrib.auth import get_user_model
  
    from django_modalview.generic.edit import ModalUpdateView
    from django_modalview.generic.component import ModalResponse
   
    from myapp.forms import MyModelForm
    
    
    class MyUpdateModal(ModalUpdateView):
    
        def __init__(self, *args, **kwargs):
            super(MyUpdateModal, self).__init__(*args, **kwargs)
            self.title = "My title"
            ...
            
        def dispatch(self, request, *args, **kwargs):
            # I get an user in the db with the id parameter that is in the url.
            self.object = get_user_model().objects.get(pk=kwargs.get('id'))
            return super(MyUpdateModal, self).dispatch(request, *args, **kwargs)
            
        def form_valid(self, form, **kwargs):
            self.response("Object is updated", "success")
            return super(MyUpdateModal, self).form_valid(form, **kwargs)

```
/!\ TO USE A MODAL WITH FORM YOU HAVE TO ADD A SCRIPT IN YOUR HTML HEADER

```html
  <doctype>
  ...
  <head>
      ...
      <script type="text/javascript" src="{% static 'django_modalview/js/jquery.form.js' %}></script>
  </head>
  ...
  
```

### ModalDeleteView

This class permit to handle the deletion of an object. 

example:

```python
    from django.contrib.auth import get_user_model

    from django_modalview.generic.edit import ModalDeleteView
    from django_modalview.generic.component import ModalResponse
    
    class MyModalDelete(ModalDeleteView):
        def __init__(self, *args, **kwargs):
            super(MyModalDelete, self).__init__(*args, **kwargs)
            self.title = "My title"
            ...
            
        def dispatch(self, request, *args, **kwargs)
            self.object = get_user_model().objects.get(pk=kwargs.get('id'))
            return super(MyModalDelete, self).dispatch(request, *args, **kwargs)
            
        def delete(self, request, *args, **kwargs):
            super(MyModalDelete, self).delete(request, *args, **kwargs)
            self.response = ModalResponse("object is deleted", "success")
```


## New components

The app come with two component that you will use everytimes.
    
### ModalButton

It is the class used for all the button of the django-modalview app. 
Its attribute are:
        - value  the value display in the button
        - display boolean to set if the button is diaplayed or not
        - type  the class of the button. Bootstrap give us several values:
                        *success
                        *info
                        *danger
                        *warning
        - url the url value. None by default. This attribute may is usefull in several cases.


### ModalResponse

See the differents exemples to understand this class. The class are the same than the button class.


## Advanced Javascript

The jquery plugin that handle the client side permit to define several callbacks:
    - on_show_modal  callback call when the modal is displayed
    - on_hide_modal  callback call when the modal is hidden and there wasn't a submit action.
    - on_hide_modal_after_submit  callback call when the modal is hidden and there was a submit action
    - on_submit  callback call after the submit action
    - on_done  callback call after the news are apply in the modal. ex: when a modalresponse is displayed
    
    example:
    ```javascript
        
        $('#my_modal_runner').DjangoModalRunner({
            on_show_modal: function(){
                alert('show');
            },
            on_hide_modal: function(){
                alert('hide without action');
            },
            on_hide_modal_after_submit: function(){
                alert('hide with action');
            },
            on_submit: function(){
                alert('submit');
            },
            on_done: function(){
                alert('done');
            }
            
        });
    ```
