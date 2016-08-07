"""
Definition of views.
"""

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from models import Item,Photo
from forms import AlbumForm,PhotoForm
from django.core.urlresolvers import reverse
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    all_items=Item.objects.all()
    
    return render(request,'app/index.html',{'title':'InstaKiloGram','year':datetime.now().year,'all_items':all_items})

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(  
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def view_items(request):
    all_items=Item.object.all()
    thumbnail=all_items.photo_set().first().image.thumb_url
    return render(request,'app/index.html',{'all_items':all_items,'thumbnail':thumbnail})
    
def item_detail(request,id):
    album=get_object_or_404(Item,id=id)
    images=album.photo_set.all()
    
    return render(request,'app/ItemDetails.html',{'album':album,'images':images})
    
def add_photo(request,id):
    album=get_object_or_404(Item,id=id)
    if request.method=='POST':
        form=PhotoForm(request.POST,request.FILES  )
        if form.is_valid():
            instance=form.save(commit=False)
            instance.item=album
            instance.save()
            return redirect(reverse('home'))
    form=PhotoForm()
    return render(request,'app/AddPhoto.html',{'form':form})
        
def photo_detail(request):
    return HttpResponse("<h1>Photots</h1>")

def create_album(request):
    form=AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        #use reverse always with the HttpResponseRedirect
        return HttpResponseRedirect(reverse('home'))
    return render(request,'app/createform.html',{'form':form})        

def delete_album(request,id):
    item=get_object_or_404(Item,id=id)
    for photos in item.photo_set.all():
        photos.image.delete()
    item.delete()
    return HttpResponseRedirect(reverse('home'))