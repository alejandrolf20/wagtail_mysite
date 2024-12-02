from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

class HomePage(Page):
    body = models.TextField(default='Contenido predeterminado')

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
