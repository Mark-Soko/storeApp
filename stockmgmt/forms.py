from django import forms
from .models import Category, Product


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'name', 'qty_in_store',
                  'Buy_price', 'price','image']

        def clean_category(self):
            category = self.cleaned_data.get('category')
            if not category:
                raise forms.ValidationError('This field is required')
            return category

        def clean_item_name(self):
            product_name = self.cleaned_data.get('name')
            if not product_name:
                raise forms.ValidationError('This field is required')
            return product_name


# class StockSearchForm(forms.ModelForm):
#     export_to_CSV = forms.BooleanField(required=False)

#     class Meta:
#         model = Stock
#         fields = ['category', 'item_name']

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields=['name']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'qty_in_store',
                  'Buy_price', 'price','image']


# class IssueForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['issue_quantity', 'issue_to']


# class ReceiveForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['receive_quantity']
