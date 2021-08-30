from intl.models import Person
from django.shortcuts import render
from django.utils.translation import gettext as _


def intl(request):
    context = {
        "data":[
            _("daftarlar"), _("kitoblar"), _("ruchkalar"), _("telefonlar"), _("qalamlar")
        ],
        "people":Person.objects.all()
    }
    return render(request, "intl/index.html", context)