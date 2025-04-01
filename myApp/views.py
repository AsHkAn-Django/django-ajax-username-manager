from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.middleware.csrf import get_token
import json
from .models import UserName


def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})


@csrf_protect
def get_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name", "Guest")

        # Save the name to the database
        user_entry = UserName(name=name)
        user_entry.save()

        return JsonResponse({"message": f"Hello, {name}! Your name is saved."})
    return JsonResponse({"message": "Send a POST request with a name!"})


def get_saved_names(request):
    names = UserName.objects.order_by("-created_at").values_list("name", flat=True)  # Get names list
    return JsonResponse({"names": list(names)})


def delete_name(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")

        user_entry = get_object_or_404(UserName, name=name)  # Find the name
        user_entry.delete()  # Delete it

        return JsonResponse({"message": f"{name} deleted successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)


def edit_name(request):
    if request.method == "POST":
        data = json.loads(request.body)
        old_name = data.get("old_name")
        new_name = data.get("new_name")
        
        if old_name and new_name:
            name_obj = get_object_or_404(UserName, name=old_name)
            name_obj.name = new_name
            name_obj.save()
            return JsonResponse({"message": f"Name updated: {old_name} → {new_name}"})
        return JsonResponse({"message": "Both old and new names are required!"}, status=400)
    return JsonResponse({"message": "Invalid request!"}, status=400)


def home(request):
    return render(request, 'myApp/index.html')
