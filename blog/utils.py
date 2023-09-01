from django.http import HttpResponseForbidden

# Mixins
class AuthenticatedMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.id != self.get_object().author.id:
            return HttpResponseForbidden()
        return super(AuthenticatedMixin, self).dispatch(request, *args, **kwargs)