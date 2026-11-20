from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from listing.models import Property
from .models import Inquiry
from .forms import InquiryForm


def send_inquiry(request, property_id):
    property = Property.objects.filter(id=property_id).first()
    if property is None:
        return render(request, "404.html", status=404)

    form = InquiryForm(request.POST or None)
    sent = False
    if form.is_valid():
        inquiry = form.save(commit=False)
        inquiry.property = property
        inquiry.save()
        form = InquiryForm()
        sent = True
    return render(request, "inquires/send_inquiry.html", {
        "form": form,
        "property": property,
        "sent": sent,
    })


@staff_member_required
def inquiries(request):
    inquiries = Inquiry.objects.all().order_by("-created_at")
    return render(request, "inquires/inquiries.html", {"inquiries": inquiries})