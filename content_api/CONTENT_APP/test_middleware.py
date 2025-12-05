from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpResponse
from .middleware import OpenNewTabMiddleware

class OpenNewTabMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_middleware_injects_script(self):
        # Create a request to an admin URL
        request = self.factory.get('/admin/some-page/')
        
        # Add session to the request
        middleware = SessionMiddleware(lambda r: HttpResponse("<html><body></body></html>"))
        middleware.process_request(request)
        request.session.save()
        
        # Set the session variable
        request.session['open_new_tab_url'] = 'http://example.com/new-page/'
        request.session.save()

        # Initialize the middleware with a simple response
        def get_response(req):
            return HttpResponse("<html><body>Content</body></html>", content_type="text/html")
        
        mw = OpenNewTabMiddleware(get_response)
        
        # Process the request
        response = mw(request)
        
        # Check if script is injected
        content = response.content.decode('utf-8')
        self.assertIn('window.open("http://example.com/new-page/", "_blank")', content)
        
        # Check if session variable is removed (we need to check the session from the request object, 
        # but since the middleware modifies the session object attached to the request, we can check it there)
        # However, the middleware pops it from the request.session object.
        self.assertNotIn('open_new_tab_url', request.session)

    def test_middleware_does_not_inject_script_if_no_session_var(self):
        request = self.factory.get('/admin/some-page/')
        
        middleware = SessionMiddleware(lambda r: HttpResponse("<html><body></body></html>"))
        middleware.process_request(request)
        request.session.save()

        def get_response(req):
            return HttpResponse("<html><body>Content</body></html>", content_type="text/html")
        
        mw = OpenNewTabMiddleware(get_response)
        response = mw(request)
        
        content = response.content.decode('utf-8')
        self.assertNotIn('window.open', content)

    def test_middleware_does_not_inject_script_on_non_admin_url(self):
        request = self.factory.get('/not-admin/')
        
        middleware = SessionMiddleware(lambda r: HttpResponse("<html><body></body></html>"))
        middleware.process_request(request)
        request.session['open_new_tab_url'] = 'http://example.com/'
        request.session.save()

        def get_response(req):
            return HttpResponse("<html><body>Content</body></html>", content_type="text/html")
        
        mw = OpenNewTabMiddleware(get_response)
        response = mw(request)
        
        content = response.content.decode('utf-8')
        self.assertNotIn('window.open', content)
