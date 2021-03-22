
from django.urls import path
from FizzBuzz.views import CheckCountView, ChangeParamsView

app_name = "FizzBuzz"

urlpatterns = [
    # Application expects count as an integer. User gets 404 for non integer fields.
    path("<int:count>/", CheckCountView.as_view(), name="count"),
    path("change/", ChangeParamsView.as_view(), name="change")
]
