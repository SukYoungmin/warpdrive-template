import django.views.generic

class Index(django.views.generic.TemplateView):
    template_name = "index.html"
index = Index.as_view()