from django.utils.deprecation import MiddlewareMixin
from .models import ErrorLog
from datetime import timedelta
from django.utils.timezone import now

class ClearOldLogsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        two_days_ago = now() - timedelta(days=2)
        old_logs = ErrorLog.objects.filter(created_at__lt=two_days_ago)
        old_logs.delete()
        print(two_days_ago)
        return None