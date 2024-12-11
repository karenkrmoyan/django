from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as _logout, login as auth_login

from .models import Question, Choice, PollUser


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list,
               "user": request.user
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def register(request):
    if request.method == "GET":
        return render(request, "polls/register.html", {})
    else:
        try:
            first_name = request.POST["firstname"]
            last_name = request.POST["lastname"]
            email = request.POST["email"]
            country = request.POST["country"]
            password = request.POST["password"]
            repeat_password = request.POST["repeat_password"]
        except:
            return render(request, "polls/register.html", {"error_message": "Missed Field"})

        if password != repeat_password:
            return render(request, "polls/register.html", {"error_message": "Password not much"})

    user = User.objects.create_user(username=email, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    poll_user = PollUser(user=user, country=country)
    poll_user.save()

    return HttpResponseRedirect("/polls/login/")


def login(request):
    if request.method == "GET":
        return render(request, "polls/login.html", context={})
    else:
        email = request.POST["email"]
        password = request.POST["password"]

    user = authenticate(username=email, password=password)

    if user:
        print(user)
        auth_login(request, user)
        return HttpResponseRedirect("/polls/")

    else:
        return render(request, "polls/login.html", {"error message": "Invalid email or password"})


def logout(request):
    _logout(request)
    return HttpResponseRedirect("/polls/login")