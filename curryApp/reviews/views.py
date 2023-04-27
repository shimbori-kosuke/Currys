from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Q
from django.conf import settings

from .models import Shop, Review
from .forms import SearchForm

def IndexView(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        shops = Shop.objects.filter(Q(name__contains=keyword)|Q(address__contains=keyword)).annotate(
        ovr_avg=Avg('review__ovrpoint__point'),
        pri_avg=Avg('review__price'),
    )
    else:
        searchForm = SearchForm()
        shops = Shop.objects.annotate(
        ovr_avg=Avg('review__ovrpoint__point'),
        pri_avg=Avg('review__price'),
    )

    context = {
        'shops':shops,
        'searchForm': searchForm,
    }
    return render(request, 'reviews/shop_list.html', context)

def ShopDetailView(request, pk):
    shop = get_object_or_404(
        Shop.objects.annotate(
            ovr_avg=Avg('review__ovrpoint__point'),
            cur_avg=Avg('review__curpoint__point'),
            naa_avg=Avg('review__naapoint__point'),
            ser_avg=Avg('review__serpoint__point'),
            int_avg=Avg('review__intpoint__point'),
            toi_avg=Avg('review__toipoint__point'),
            pri_avg=Avg('review__price'),
        ),
        pk=pk
    )

    reviews = Review.objects.filter(name_id = pk)
    mapsAPI = settings.MAPS_API_KEY

    context = {
        'reviews':reviews,
        'shop':shop,
        'maps_api':mapsAPI,
    }
    return render(request, 'reviews/shop_detail.html', context)

class ReviewDetailView(generic.DetailView):
    model = Review

class ShopCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Shop
    fields = ['name', 'address']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ShopCreateView, self).form_valid(form)

class ShopUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Shop
    fields = ['name', 'address']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(ShopUpdateView, self).dispatch(request, *args, **kwargs)

class ShopDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy('reviews:index')

class ReviewCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Review
    fields = ['name', 'menu', 'price', 'memo', 'ovrpoint', 'curpoint', 'naapoint',
              'serpoint', 'intpoint', 'toipoint']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ReviewCreateView, self).form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Review
    fields = ['name', 'menu', 'price', 'memo', 'ovrpoint', 'curpoint', 'naapoint',
              'serpoint', 'intpoint', 'toipoint']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')
        return super(ReviewUpdateView, self).dispatch(request, *args, **kwargs)

class ReviewDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:index')
