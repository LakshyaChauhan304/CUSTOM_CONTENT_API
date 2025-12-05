class OpenNewTabMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if we need to open a new tab
        if request.path.startswith('/admin/') and 'open_new_tab_url' in request.session:
            url = request.session.pop('open_new_tab_url')
            
            # Only inject into HTML responses
            if response['Content-Type'].startswith('text/html'):
                script = f'''
                <script>
                    window.addEventListener('load', function() {{
                        window.open("{url}", "_blank");
                    }});
                </script>
                '''
                content = response.content.decode('utf-8')
                # Inject before the closing body tag
                if '</body>' in content:
                    response.content = content.replace('</body>', script + '</body>').encode('utf-8')
                else:
                    # Fallback: append to end
                    response.content = (content + script).encode('utf-8')

        return response
