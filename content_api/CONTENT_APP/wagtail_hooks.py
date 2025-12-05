from wagtail import hooks
from django.utils.translation import gettext_lazy as _

@hooks.register('after_publish_page')
def do_after_publish_page(request, page):
    """
    After a page is published, store its URL in the session so we can
    open it in a new tab via middleware.
    """
    if hasattr(page, 'get_url'):
        url = page.get_url(request)
        if url:
            request.session['open_new_tab_url'] = url
