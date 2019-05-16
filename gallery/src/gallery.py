from gallery.models import Project, Media
from django.db.models import Count, Min, Max


class Gallery():
    def getProject(self):
        result = {}
        try:
            projects = Project.objects.select_related().all()
            result['status'] = '200'
            result['data'] = list(projects.annotate(mid=Min('media__id'), file=Max('media__file')).values('id', 'mid','title','file'))
        except Exception as e:
            result['status'] = '500'
            print(e)
        return result

    def getMedia(self, pk):
        result = {}
        try:
            media = Media.objects.filter(project=pk)
            result['status'] = '200'
            result['data'] = list(media.values())
        except Exception as e:
            result['status'] = '500'
            print(e)
        return result
