from django.db import models

def media_upload_to(instance, filename):
    return 'static/gallery/img/media/{}/{}'.format(instance.project.id, filename)

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
      return self.title

class Media(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    file = models.FileField(upload_to=media_upload_to)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
      return self.name