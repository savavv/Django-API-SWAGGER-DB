from rest_framework.decorators import api_view
from django.http import JsonResponse
import subprocess

@api_view(['POST'])
def uptime_view(request):
    try:
        result = subprocess.run(['uptime'], capture_output=True, text=True, check=True)
        return JsonResponse({'uptime': result.stdout})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def ifconfig_view(request):
    try:
        result = subprocess.run(['ifconfig'], capture_output=True, text=True, check=True)
        return JsonResponse({'ifconfig': result.stdout})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)