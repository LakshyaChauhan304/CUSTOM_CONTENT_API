from django.db import models
from django.contrib.auth.models import AbstractUser
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from django.conf import settings



class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_img', blank=True, null=True)

    def __str__(self):
        return self.username

class ContentPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
class DemoPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

    api_fields = [
        APIField("subtitle"),
        APIField("body"),
    ]

class ContentItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('in_progress', 'In Progress'), ('completed', 'Completed')],
        default='in_progress'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from wagtail.fields import StreamField
from . import blocks

class HomePage(Page):
    body = StreamField([
        ('heading', blocks.HeadingBlock()),
        ('paragraph', blocks.ParagraphBlock()),
        ('image', blocks.ImageBlock()),
        ('cta', blocks.CtaBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        
        # Get all published ContentPage and DemoPage objects
        # You might want to filter by live=True and order by first_published_at
        content_pages = ContentPage.objects.live().public().order_by('-first_published_at')
        demo_pages = DemoPage.objects.live().public().order_by('-first_published_at')
        
        # Combine them or pass them separately. For a "blog", usually it's a mix or just one type.
        # Let's combine them into a list and sort by date if needed, or just pass both.
        # For simplicity, let's pass them as 'blogpages'
        
        from itertools import chain
        from operator import attrgetter
        
        blogpages = sorted(
            chain(content_pages, demo_pages),
            key=attrgetter('first_published_at'),
            reverse=True
        )
        
        context['blogpages'] = blogpages
        return context
