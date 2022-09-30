from ast import arg
from calendar import month
from http.client import HTTPResponse
import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

month_name = {
    "january": "January, Eat no meat for entire month !!!",
    "february": "February, Walk for atleast 20 mins every-day.",
    "march": "March, Learn Django for atleast 20 mins everyday 💻",
    "april": "April, Eat no meat for entire month !!!",
    "may": "May, Walk for atleast 20 mins every-day.",
    "june": "June, Learn Django for atleast 20 mins everyday 💻",
    "july": "July, Eat no meat for entire month !!!",
    "august": "August, Walk for atleast 20 mins every-day.walk",
    "september": "September, Learn Django for atleast 20 mins everyday 💻",
    "october": "October, Eat no meat for entire month !!!",
    "november": "November, Walk for atleast 20 mins every-day.",
    # "december": "December, Learn Django for atleast 20 mins everyday 💻",
    "december": None
}


def show_month_list(request):
    month_list = list(month_name.keys())
    """
    # Old code
    month_str = ""
    for items in month_list:
        capitalized_month = items.capitalize()
        month_path = reverse("month-challenge", args=[items])
        month_str += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    final_response = f"<h2><ul>{month_str}</ul></h2>"
    return HttpResponse(final_response)
    """
    return render(request, "challenges/index.html", {
        "months": month_list
    })


def redirect_monthly_challenges(request, month):
    month_list = list(month_name.keys())
    if month > len(month_list) or month == 0:
        return HttpResponseNotFound("<h2>Month not supported 🛑</h2>")
    redirect_month = month_list[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    """
    try:
        challenge_text = month_name[month]
        return HttpResponse(f"<h2>{challenge_text}</h2>")
    except:
        return HttpResponseNotFound("<h2>Given month not supported !!!</h2>")
    """
    try:
        challenge_text = month_name[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "mc_ct": challenge_text,
            "mc_m": month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()
