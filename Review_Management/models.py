from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubmittedBy(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ViewedBy(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ReviewMedia(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(SubmittedBy, on_delete=models.CASCADE)
    file_size = models.CharField(max_length=50)
    file_path = models.CharField(max_length=50)
    file_type = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    comments = models.CharField(max_length=100)
    viewed_by = models.ForeignKey(ViewedBy, on_delete=models.CASCADE)
    modified_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project}-{self.department}"
