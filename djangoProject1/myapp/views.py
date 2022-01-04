from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from djangoProject1.myapp.models import Laptops
from djangoProject1.myapp.models import Order


def home(req):
    return render(req, 'home.html')


def tv(req):
    return render(req, 'tv.html')


def laptops(req):
    laptop_objects = Laptops.objects.all()
    template_name = 'laptops.html'


    item_name = req.GET.get('item_name')
    if item_name != '' and item_name is not None:
        laptop_objects = laptop_objects.filter(title__icontains=item_name)

    paginator = Paginator(laptop_objects, 4)
    page_number = req.GET.get('page')
    laptop_objects = paginator.get_page(page_number)

    return render(req, template_name, {'laptop_objects': laptop_objects})





def detail(request, id):

    obj = Laptops.objects.get(id=id)
    context = {'laptop_objects':obj}
    return render(request,'detail.html',context)





def phones(req):
    return render(req, 'phones.html')


def watches(req):
    return render(req, 'watches.html')


def basked(request):
    return render(request, 'basked.html')


def index(req):
    product_objects = Laptops.objects.all()
    return render(req, 'laptops.html', {'product_objects': product_objects})

def check(req):
    if req.method == 'POST':
        items = req.POST.get('items', "")
        name = req.POST.get('name', "")
        email = req.POST.get('email', "")
        address = req.POST.get('address', "")
        city = req.POST.get('city', "")
        state = req.POST.get('state', "")
        zipcode = req.POST.get('zipcode', "")
        total = req.POST.get('total', '')
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode,
                         total=total)
        order.save()


    return render(req, 'check.html')