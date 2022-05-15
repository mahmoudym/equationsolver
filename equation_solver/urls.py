from django.urls import path
from . import views

urlpatterns = [
    path("", views.equation_folder, name="equation_folder"),
    path("<int:pk>/", views.equation_index, name="equation_index"),
    path("equation_detail/<int:pk>/", views.equation_detail, name="equation_detail"),
    path("createfolder/", views.createfolder, name="createfolder"),
    path("deletefolder/<int:pk>/", views.deletefolder, name="deletefolder"),
    path("createequation/<int:pk>/", views.createequation, name="createequation"),
    path("deleteequation/<int:pk>/", views.deleteequation, name="deleteequation"),
    path("solve/<int:pk>/", views.solve, name="solve"),
    path("editequation/<int:pk>/", views.editequation, name="editequation"),
    path("edit_equation/<int:pk>/", views.edit_equation, name="edit_equation"),
]
