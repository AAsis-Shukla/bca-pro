from django.shortcuts import render,redirect
from primary.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db.models.functions import Lower

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['customerName']
        email = request.POST['customerEmail']
        contact = request.POST['number']
        msg = request.POST['w3review']

        # Check if a record with the same data already exists
        existing_record = PrimaryPageContact.objects.filter(
            email=email, number=contact, 
        ).exists()

        if not existing_record:
            # Save the record to the database
            PrimaryPageContact(name=name, email=email, number=contact, message=msg).save()
            success_message = "Your Record has been submitted!"
        else:
            # Record already exists, show a message
            success_message = "Record already exists!"

        return render(request, "index.html", {'success_message': success_message})
    
    return render(request, "index.html")

def signUp(request):
    if request.method == "POST":
        name = request.POST['Name']
        phone = request.POST['Phone']
        email = request.POST['email']
        role = request.POST['User']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        if password != confirm_password:
            return render(request,'signUp.html',{'success_msg':'Password do not match!'})
        if User.objects.filter(email=email):
            return render(request,'signUp.html',{'success_msg':'Email already exists!'})
        user = User.objects.create_user(first_name = name, username=email)
        user.set_password(password)
        user.save()
        PrimaryUserSignUp.objects.create(
            user=user,
            name = name,
            phone=phone,
            email=email,
            role=role, 
        )
        return render(request,'Login.html',{'success_msg':'Account created successfully!'})
    return render(request,'signUp.html')
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        # role = request.POST['User']
        password = request.POST['password']
        if not User.objects.filter(username = email):
            return render(request,'Login.html',{'success_msg':'Invalid Username!'})
        user = authenticate(username = email , password =  password)
        if user is None:
            return render(request,'Login.html',{'success_msg':'Invalid password!'})
        else:
            login(request, user) 
            return redirect(IoIndex)             
    return render(request,'Login.html')

@never_cache
@login_required(login_url='login')
def IoIndex(request):
    if request.method == "GET":
        filter_by = request.GET.get('filter_by', None)
        filter_input = request.GET.get('filter_input', None)
        sort_by = request.GET.get('sort_by', None)

        if filter_by and filter_input:  # Check if both parameters exist
            if filter_by == 'name':
                form = Product_Entry.objects.filter(Product_name__icontains=filter_input)
            elif filter_by == 'Product_inOut':
                form = Product_Entry.objects.filter(Product_inOut__icontains=filter_input)
            elif filter_by == 'Product_quantity':
                form = Product_Entry.objects.filter(Product_quantity__icontains=filter_input)
            else:
                form = None
            return render(request, 'index.html', {'form': form,'form_length':len(form)})
        if sort_by == 'name':
            form = Product_Entry.objects.all().order_by(Lower('Product_name'))
            return render(request, 'IoIndex.html', {'form': form,'form_length':len(form)})
        if sort_by == 'latest':
            form = Product_Entry.objects.all().order_by('-id')
            return render(request, 'IoIndex.html', {'form': form,'form_length':len(form)})
        else:
            pass
    if request.method == 'POST':
    # Extract form data from the POST request
        product_name = request.POST.get('Product_name')
        product_id = request.POST.get('Product_id')
        product_quantity = request.POST.get('Product_quantity')
        Product_image = request.FILES.get('Product_image')
        product_inOut = request.POST.get('Product_inOut')

        # Create and save the ProductEntry instance
        product_entry = Product_Entry(
            Product_name=product_name,
            Product_id=product_id,
            Product_quantity=product_quantity,
            Product_inOut=product_inOut,
            Product_image=Product_image
        )
        product_entry.save()
    return render(request, 'IoIndex.html',{'form':Product_Entry.objects.all(),'form_length':len(Product_Entry.objects.all())})
@login_required()
def deleteEntry(request,id):
    previous = Product_Entry.objects.get(id=id)
    previous.Product_image.delete()
    previous.Product_image = None
    previous.delete()
    return redirect(IoIndex)
@login_required()
def IoUpdate(request,id):
    previous = Product_Entry.objects.get(id=id)
    if request.method == "POST":
        previous.Product_name  = request.POST['Product_name']
        previous.Product_id  = request.POST['Product_id']
        previous.Product_inOut = request.POST['Product_inOut']
        previous.Product_quantity = request.POST['Product_quantity']
        Product_image = request.FILES.get('Product_image')
        if Product_image:
            previous.Product_image.delete()
            previous.Product_image = Product_image
            previous.save()
        else:
            previous.save()
        return redirect(IoIndex)
    return render(request,'IoUpdate.html',{'form':previous})
def user_logout(request):
    logout(request)
    return redirect('login')