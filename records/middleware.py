from django.utils.timezone import now
from django.core.mail import send_mail
from .models import APIAccessLog
import threading

_request_local = threading.local()  # Store request per thread

class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Get user if authenticated
        user = request.user if request.user.is_authenticated else None
        endpoint = request.path
        method = request.method
        ip_address = self.get_client_ip(request)
        status_code = response.status_code

        # Save log to database
        APIAccessLog.objects.create(
            user=user,
            endpoint=endpoint,
            method=method,
            ip_address=ip_address,
            status_code=status_code,
            timestamp=now()
        )

        # Send email if unauthorized access attempt occurs
        if status_code == 403:
            send_mail(
                subject="Unauthorized Attempt Detected",
                message=f"User {request.user} attempted to access {request.path} without permission.",
                from_email="belammuia0@gmail.com",
                recipient_list=["belammuia0@gmail.com"],
            )

        return response

    def get_client_ip(self, request):
        """Extract client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
