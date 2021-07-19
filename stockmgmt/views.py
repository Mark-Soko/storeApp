#from django import forms
from django.shortcuts import render, redirect
from .models import*
from .forms import *
from django.http import JsonResponse, HttpResponse
import json
import csv
from django.contrib import messages



def home(request):
    title = 'Locked'
    context = {
        "title": title,
    }
    return render(request, "lockscreen.html", context)


def list_items(request):
    Products = Product.objects.all()
    select_category = Category.objects.all() 
    context = {
        "Products": Products,
    }
    return render(request, "list_items.html", context)




def add_category(request):
    form = CreateCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Category added successful')
        return redirect('/list_items')
    context ={
        'form':form,
    }
    return render(request, 'add_category.html',context)



def add_product(request):
    form = ProductCreateForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Product added successfully')
        return redirect('/list_items')
    
    context = {
        "form": form,
        "title": "Add product",
    }
    return render(request, 'add_product.html', context)


def update_product(request, pk):
    queryset = Product.objects.get(id=pk)
    form = ProductUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST,request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully ')
            return redirect('/list_items')

    context = {
        'form': form
    }
    return render(request, 'add_product.html', context)


def delete_items(request, pk):
    pass
    queryset = Product.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted successfully ')
        return redirect('/list_items')
    return render(request, 'delete_items.html')



def dashboard(request):
    Products = Product.objects.all()
    if request.GET:
        amountPaid = int(request.GET['amountPaid'])
        balance = int(request.GET.get('balance'))
        totalCost = amountPaid - int(balance)
        trans = Order(totalCost=totalCost,
                          amountPaid=amountPaid, balance=balance, completed=True)
        trans.save()
    return render(request, 'dashboard.html', {'Products': Products})












def stock_detail(request, pk):
    pass
# #     queryset = Stock.objects.get(id=pk)
# #     context = {
# #         "queryset": queryset,
# #     }
# #     return render(request, "stock_detail.html", context)


# # def issue_items(request, pk):
# #     queryset = Stock.objects.get(id=pk)
# #     form = IssueForm(request.POST or None, instance=queryset)
# #     if form.is_valid():
# #         instance = formtotalPrice.save(commit=False)
# #         instance.quantity -= instance.issue_quantity
# #         # instance.issue_by = str(request.user)
# #         messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) +
# #                          " " + str(instance.item_name) + "s now left in Store")
# #         instance.save()

# #         return redirect('/stock_detail/'+str(instance.id))
# #         # return HttpResponseRedirect(instance.get_absolute_url())

# #     context = {
# #         "title": 'Issue ' + str(queryset.item_name),
# #         "queryset": queryset,
# #         "form": form,
# #         "username": 'Issue By: ' + str(request.user),
# #     }
# #    return render(request, "add_items.html", context)


# # def receive_items(request, pk):
# #     queryset = Stock.objects.get(id=pk)
# #     form = ReceiveForm(request.POST or None, instance=queryset)
# #     if form.is_valid():
# #         instance = form.save(commit=False)
# #         instance.quantity += instance.receive_quantity
# #         instance.save()
# #         messages.success(request, "Received SUCCESSFULLY. " +
# #                          str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

# #         return redirect('/stock_detail/'+str(instance.id))
# #         # return HttpResponseRedirect(instance.get_absolute_url())
# #     context = {
# #         "title": 'Reaceive ' + str(queryset.item_name),
# #         "instance": queryset,
# #         "form": form,
# #         "username": 'Receive By: ' + str(request.user),
# #     }
# #     return render(request, "add_items.html", context)







# # def saveCart(request):
# #     data = json.loads(request.body)
# #     item_name = data["item_name"]
# #     quantity = data["quantity"]
# #     item_total = data["item_total"]
# #     invoiceNo = random.randint(100, 10000000)
    
# #     print(item_name)
# #     print(invoiceNo)
# #     orderedItems = oderItem(invoiceNo=invoiceNo, item_name=item_name,
# #                             quantity=quantity, item_price=item_total)

# #     return JsonResponse("Saved", safe=False)
