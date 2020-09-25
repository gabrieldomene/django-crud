from django.urls import include, path
from rest_framework import routers

from api.views import views

"""
The urlpatterns is the definition of routes in the `api` project,
the main routes are all caught by urls.py in the main app and redirect to this file.

Each URL can be provided with one view and will be used with their actions.

`court/` can be used for getting all records or passed with an ID for PUT and POST actions.
`court/personal/:id` can be used for specific details in the client records.
`court/decision/:id` can be used for getting the sum of decisions for one client. 
"""
urlpatterns = [
    path('court/', views.AllCourtDecision.as_view()),
    path('court/<int:id>', views.AllCourtDecision.as_view()),
    path('court/personal/<int:id_cliente>', views.ClientCourtDecisions.as_view()),
    path('court/decision/<int:id_cliente>', views.CountClientCourtDecisions.as_view())
]