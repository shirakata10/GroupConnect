from django.shortcuts import render
from django.views import generic

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm, GroupCreateForm
)
from .models import (
    Notice, Group, Member, GroupIcon,Signboard,Post,Situation,Category
)

from django.views.generic.edit import ModelFormMixin


User = get_user_model()

class bordlist(generic.ListView) :
    template_name = 'GroupConnect/bordlist.html'
    model = Signboard
    context_object_name='group_list'


    
    def get_context_data(self, **kwargs):

        
        group =Group.objects.get(id='1')
        context = super().get_context_data(**kwargs)

        context.update({
            'messages' : Signboard.objects.filter(group_id=group),
            'categorys' : Category.objects.filter(group_id=group)
        })
        return context

# html側のname属性に設定しているボタンの名前に応じて削除する

    def post(self,request):
        if 'delete' in request.POST: 
            Signboard_pk = request.POST['delete']
            Signboard.objects.filter(id=Signboard_pk).delete()
            

        elif 'alldelete' in request.POST:
            Signboard_pk = request.POST.getlist('SinboardAlldelete')
            for signboardall_pk in Signboard_pk:
                Signboard.objects.filter(id=signboardall_pk).delete()

        elif 'category-delete' in request.POST:
            Category_pk = request.POST['category-delete']
            Category.objects.filter(id=Category_pk).delete()



        return redirect('GroupConnect:bordlist')  


    

    def get_queryset(self):
        ID = self.request.user.id

        

        members = Member.objects.filter(user_id=ID)
        
        g = []

        for i in members:
            groups = Group.objects.all().filter(id=i.group_id)
            g += groups


        return g


def categoryget(request):
    """ カテゴリーを取得 """
    category_get = request.POST['add']
    group =Group.objects.get(id='1')     
    Category(group_id=group, name=category_get).save()
    return redirect('GroupConnect:bordlist')

def Signboardform(request):
    """ form """
    Signboard_title = request.POST['title']
    Signboard_textarea = request.POST['textarea']
    Signboard_category = Category.objects.get(id=request.POST['category'])
    group = Group.objects.get(id='1')
    Signboard(group_id=group, title=Signboard_title , category_id=Signboard_category , text=Signboard_textarea ).save()
    return redirect('GroupConnect:bordlist')




        
class SignboardView(generic.DetailView):
    model = Signboard
    template_name = 'GroupConnect/signboard_detail.html'

class SignboardDelete(generic.DeleteView):
    model = Signboard
    success_url = 'GroupConnect:bordlist'

class CategoryDelete(generic.DeleteView):
    model = Signboard
    success_url ='GroupConnect:bordlist'
    
    
