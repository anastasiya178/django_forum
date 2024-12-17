from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from forum.models import Category


# Create your views here.
def get_dashboard(request):
    """Dashboard view"""

    return render(
        request,
        "forum/dashboard.html",
    )


# Categories
class CategoryList(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        """Add context to CategoryList"""
        context = super().get_context_data(**kwargs)
        # context["form"] = PostForm()
        return context


class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = "c_pk"
    template_name = "forum/category_detail.html"


class CategoryCreateView(CreateView):
    fields = "__all__"
    model = Category
    pk_url_kwarg = "c_pk"


class CategoryUpdateView(UpdateView):
    fields = ("name",)
    model = Category
    pk_url_kwarg = "c_pk"


class CategoryDeleteView(DeleteView):
    model = Category
    # TODO: add categories template before enabling this view
    success_url = reverse_lazy("forum:categories")  # after deletion it gets here
    pk_url_kwarg = "c_pk"
