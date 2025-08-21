from django.shortcuts import redirect

class ProgressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If root path and cookie exists, resume progress
        if request.path == "/":
            last = request.COOKIES.get("progress")
            if last:
                return redirect(f"/room/{last}/")
        return self.get_response(request)