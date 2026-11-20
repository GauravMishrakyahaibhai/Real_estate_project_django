import json
import re

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST

from listing.models import Property


def home(request):
    latest = Property.objects.all().order_by("-id")[:3]
    return render(request, "home/home.html", {"latest": latest})


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")


def _cards(qs):
    return [
        {
            "title": f"{p.title} ({p.city}) - ₹{int(p.price):,}",
            "url": reverse("property_detail", args=[p.id]),
        }
        for p in qs[:3]
    ]


@require_POST
def chatbot(request):
    try:
        text = json.loads(request.body).get("message", "").lower().strip()
    except (ValueError, AttributeError):
        text = ""

    if not text:
        return JsonResponse({"reply": "Please type a message."})

    if re.search(r"\b(hi|hello|hey)\b", text):
        return JsonResponse({
            "reply": "Hello! Tell me a city or number of bedrooms, e.g. 'flats in Nagpur' or '2 bhk'."
        })

    if any(w in text for w in ["thanks", "thank you"]):
        return JsonResponse({"reply": "You're welcome! Let me know if you need anything else."})

    if any(w in text for w in ["contact", "phone", "call", "email", "office"]):
        return JsonResponse({
            "reply": "You can visit our Contact page or send an enquiry on any property. We'll get back to you soon.",
            "links": [{"title": "Contact page", "url": reverse("contact")}],
        })

    qs = Property.objects.all().order_by("-id")

    cities = Property.objects.values_list("city", flat=True).distinct()
    for c in cities:
        if c and c.lower() in text:
            qs = qs.filter(city__iexact=c)
            break

    m = re.search(r"(\d+)\s*(bhk|bed|beds|bedroom|bedrooms)", text)
    if m:
        qs = qs.filter(bedrooms=int(m.group(1)))

    m2 = re.search(r"(?:under|below|budget|less than)\s*(\d+)", text)
    if m2:
        qs = qs.filter(price__lte=int(m2.group(1)))

    searched = bool(m) or bool(m2) or qs.count() != Property.objects.count() or any(
        w in text for w in ["property", "properties", "flat", "house", "latest", "show", "plot"]
    )
    if searched:
        if qs.exists():
            return JsonResponse({"reply": "Here are some matching properties:", "links": _cards(qs)})
        return JsonResponse({"reply": "No properties found for this search. Try a different city or bedroom count."})

    return JsonResponse({
        "reply": "Sorry, I didn't understand that. Try: 'show properties', '2 bhk', 'flats in Nagpur', or 'under 5000000'."
    })