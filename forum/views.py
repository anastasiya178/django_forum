from django.shortcuts import render


# Create your views here.
def get_dashboard(request):
    """Dashboard view"""

    return render(
        request,
        "forum/dashboard.html",
    )