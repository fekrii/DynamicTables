from tableBuilder.views import CreateTableView, TableUpdateView, TableRowView
from django.urls import path



urlpatterns = [
    path('', CreateTableView.as_view()),
    path('<name>/', TableUpdateView.as_view()),
    path('<name>/row/', TableRowView.as_view())

]
