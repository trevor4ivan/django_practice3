#from typing import Any
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.http import HttpResponse
import textwrap

class HomePageView(View):
    def dispatch(request, *args, **kwargs):
        response_text= textwrap.dedent('''
                                      <html>
<head>
<h1>Greetings to the world</h1>
</head
<body>
<b>Hello world</b>
</body>
</html>
''' )
        return HttpResponse(response_text)
class CourseView(TemplateView):
    template_name = "course.html"
        
	


    
