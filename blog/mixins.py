from django.http import HttpResponseForbidden
from django.contrib import messages
from django.utils.timezone import now
from django.shortcuts import redirect
from django.db.models import Q

class AuthorOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return HttpResponseForbidden("Ви не автор цього об'єкта")
        return super().dispatch(request, *args, **kwargs)

class AutoAuthorMixin:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SuccessMessageMixin:
    success_message = None
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response

class UpdatedByMixin:
    def form_valid(self, form):
        if hasattr(form.instance, "updated_by"):
            form.instance.updated_by = self.request.user
        return super().form_valid(form)

class PublishedOnlyMixin:
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class SearchMixin:
    search_param = 'q'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get(self.search_param)
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return queryset

class DateFilterMixin:
    date_field = 'created_at'
    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(**{f"{self.date_field}__date": date})
        return queryset

class OwnerOrStaffMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user and not request.user.is_staff:
            return HttpResponseForbidden("Доступ заборонено")
        return super().dispatch(request, *args, **kwargs)

class RedirectIfAuthenticatedMixin:
    redirect_url = '/'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)

class TimestampMixin:
    def form_valid(self, form):
        if hasattr(form.instance, "updated_at"):
            form.instance.updated_at = now()
        return super().form_valid(form)
