from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls")),
    path("simpleforms/", include("simpleforms.urls")),
    path("profile/", include("profileapp.urls")), 
    path("", include("store.urls")),
    path("", include("shopping.urls")),

 ) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += [
#         path('rosetta/', include('rosetta.urls'))
#     ]