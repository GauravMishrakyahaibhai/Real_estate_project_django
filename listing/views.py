from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Property, PropertyImage
from .forms import PropertyForm


def property_list(request):
    properties = Property.objects.all().order_by("-id")
    return render(request, "listing/property_list.html", {"properties": properties})


def property_detail(request, id):
    prop = get_object_or_404(Property, id=id)
    return render(request, "listing/property_detail.html", {"property": prop})


def _save_extra_images(form, prop):
    for f in form.cleaned_data.get("extra_images", []):
        PropertyImage.objects.create(property=prop, image=f)


@staff_member_required
def add_property(request):
    form = PropertyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        prop = form.save()
        _save_extra_images(form, prop)
        return redirect("property_list")
    return render(request, "listing/add_property.html", {"form": form})


@staff_member_required
def update_property(request, id):
    prop = get_object_or_404(Property, id=id)
    form = PropertyForm(request.POST or None, request.FILES or None, instance=prop)
    if form.is_valid():
        prop = form.save()
        _save_extra_images(form, prop)
        return redirect("property_detail", id=prop.id)
    return render(request, "listing/update_property.html", {"form": form, "property": prop})


@staff_member_required
def delete_property(request, id):
    prop = get_object_or_404(Property, id=id)
    if request.method == "POST":
        prop.delete()
        return redirect("property_list")
    return render(request, "listing/delete_property.html", {"property": prop})