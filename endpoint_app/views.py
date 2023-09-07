from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import datetime
import pytz

def endpoint_view(request):
    # Get query parameters from the GET request
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get the current UTC time within a +/-2 minute window
    current_utc_time = datetime.datetime.now(pytz.utc)
    current_utc_time_str = current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Define GitHub repository and file URLs
    github_repo_url = "https://github.com/username/repo"
    github_file_url = f"{github_repo_url}/blob/main/manage.py"


    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)