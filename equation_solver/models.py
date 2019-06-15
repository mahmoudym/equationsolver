from django.db import models

class Equation_solver(models.Model):
    name = models.TextField(default= 'No name')
    equation = models.TextField()
    variables = models.TextField()
    finalvars = models.TextField(default = "")
    description = models.TextField(default = 'No description')
    folder = models.IntegerField(default = 0)
class Folder(models.Model):
    name = models.TextField()
