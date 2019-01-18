from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class Temp_entryView(generic.TemplateView):
    template_name = 'GroupConnect/temp_entry.html'

class Temp_entry_resultView(generic.TemplateView):
    template_name = 'GroupConnect/temp_entry_result.html'

class Main_entryView(generic.TemplateView):
    template_name = 'GroupConnect/main_entry.html'

class Main_entry_confView(generic.TemplateView):
    template_name = 'GroupConnect/main_entry_conf.html'

class Main_entry_compView(generic.TemplateView):
    template_name = 'GroupConnect/main_entry_comp.html'

class MypageView(generic.TemplateView):
    template_name = 'GroupConnect/mypage.html'

class ProfileView(generic.TemplateView):
    template_name = 'GroupConnect/profile.html'

class Pass_settingView(generic.TemplateView):
    template_name = 'GroupConnect/pass_setting.html'

class Pass_setting_compView(generic.TemplateView):
    template_name = 'GroupConnect/pass_setting_comp.html'

class Mail_settingView(generic.TemplateView):
    template_name = 'GroupConnect/mail_setting.html'

class WithdrawView(generic.TemplateView):
    template_name = 'GroupConnect/withdraw.html'

class GrouptopView(generic.TemplateView):
    template_name = 'GroupConnect/grouptop.html'

class GrouplistView(generic.TemplateView):
    template_name = 'GroupConnect/grouplist.html'

class Group_settingView(generic.TemplateView):
    template_name = 'GroupConnect/group_setting.html'

class CreategroupView(generic.TemplateView):
    template_name = 'GroupConnect/creategroup.html'

class BordlistView(generic.TemplateView):
    template_name = 'GroupConnect/bordlist.html'

class BordView(generic.TemplateView):
    template_name = 'GroupConnect/bord.html'

class NotFoundView(generic.TemplateView):
    template_name = 'GroupConnect/notfound.html'