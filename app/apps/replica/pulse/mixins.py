from coreExtend.models import Account
from replica import settings as replicaSettings
from .models import Topic, Entry

class PulseViewMixin:
    date_field = 'pub_date'
    paginate_by = replicaSettings.PAGINATE
    month_format = "%m"

    def get_allow_future(self):
        return self.request.user.is_staff

    def get_queryset(self):
        if self.request.user.is_staff:
            return Entry.objects.posts()
        else:
            return Entry.objects.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
