from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

from .models import vd_event
from .models import vd_user_profile
from .models import vd_information_type
from .models import vd_user_information
from .models import vd_participent_event
from .models import vd_organizer_event
from .models import vd_club_card

class UserInline(admin.StackedInline):
    model = vd_user_profile
    can_delete = False
    verbose_name_plural = 'Участники'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserInline, )



class EventModelAdmin(admin.ModelAdmin):
    list_display = ["event_name", "data_plan"]
    list_display_links = ["event_name","data_plan"]
    list_filter = ["data_plan", "status", "many_days", "event_type", "level", "country"]
    search_fields = ["event_name", "comment"]

    class Meta:
        model = vd_event

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "middle_name", "role"]
    list_display_links = ["last_name", "role"]
    list_filter = ["role"]
    search_fields = ["last_name", "first_name", "comment"]

    class Meta:
        model = vd_user_profile


class InfoModelAdmin(admin.ModelAdmin):
    list_display = ["inf_name", 'is_primary']
    list_editable = ["inf_name", 'is_primary']

    class Meta:
        model = vd_information_type

class UserInfoModelAdmin(admin.ModelAdmin):
    list_display = ["user", 'inf_type', 'inf_value']
    list_filter = ["inf_type", 'user']
    search_fields = ['inf_value']
    list_editable = ["inf_value"]

    class Meta:
        model = vd_user_information


class ParticipentEventAdmin(admin.ModelAdmin):
    list_display = ["event_id", 'participant_id']
    list_filter = ["event_id"]

    class Meta:
        model = vd_participent_event
    

class OrganizeriEventAdmin(admin.ModelAdmin):
    list_display = ["event_id", "organizer_id", "coeff"]
    list_filter = ["event_id", "organizer_id"]


    class Meta:
        model = vd_organizer_event

class ClubCardAdmin(admin.ModelAdmin):
    list_display = ["card_number", "state", "user_id", "price", "place"]
    list_display_links = ["state", "user_id", "price", "place"]
    list_filter = ["state", "place"]
    search_fields = ["card_number"] 

    class Meta:
         model = vd_club_card


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(vd_event, EventModelAdmin)
admin.site.register(vd_user_profile, UserModelAdmin)
admin.site.register(vd_information_type, InfoModelAdmin)
admin.site.register(vd_user_information, UserInfoModelAdmin)
admin.site.register(vd_participent_event,ParticipentEventAdmin)
admin.site.register(vd_organizer_event,OrganizeriEventAdmin)
admin.site.register(vd_club_card,ClubCardAdmin)