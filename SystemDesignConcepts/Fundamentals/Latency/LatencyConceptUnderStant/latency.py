# views.py
import time

from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import AllowAny

from .models import Customer


@api_view(["GET"])
@permission_classes([AllowAny])  # Demo only
def customer_list(request):
    start = time.perf_counter()

    customers = list(
        Customer.objects.values(
            "id", "name", "email"
        )[:100]
    )

    elapsed_ms = (
        time.perf_counter() - start
    ) * 1000

    return JsonResponse({
        "customers": customers,
        "server_processing_ms": round(
            elapsed_ms, 2
        )
    })