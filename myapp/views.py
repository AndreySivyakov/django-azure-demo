from django.shortcuts import render, render_to_response
#from django.http import HttpResponse, JsonResponse
from .forms import ClaimForm, VendorForm, mult_vendor
from .models import *
from .filters import ClaimFilter, VendorFilter
import json
import datetime
#from dal import autocomplete as autocomplete
from django.forms.models import model_to_dict

def home(request):
    return render(request, 'myapp/user_form2.html', {'form_claim':ClaimForm(),'form_vendor':mult_vendor()})


def user_form2(request):

    form_claim = ClaimForm()
    form_vendor = mult_vendor()

    if request.method == "POST":
        form_claim = ClaimForm(request.POST)
        form_vendor = mult_vendor(request.POST)

    if form_claim.is_valid() and form_vendor.is_valid():
        form_claim.save(commit=True)
        obj = form_claim.save()
        for vendor_instance in form_vendor.cleaned_data:
            if len(vendor_instance) !=0:
                Vendor.objects.create(vendor_claim_ref = obj,
                                    vendor_number = vendor_instance['vendor_number'],
                                    vendor_name = vendor_instance['vendor_name'])
        return render(request, 'myapp/user_form2.html', {'form_claim':ClaimForm(),'form_vendor':mult_vendor()})
    else:
        print('ERROR FORM INVALID')

    return render(request, 'myapp/user_form2.html', {'form_claim':form_claim,'form_vendor':form_vendor})


def  post_record(request, record):

    form_claim = ClaimForm()
    form_vendor = mult_vendor()

    record = list(record.values())
    record_pk = record[0]['id']
    record_vendors = Vendor.objects.filter(vendor_claim_ref_id=record_pk)
    record_vendors = list(record_vendors.values())

    global myconverter
    def myconverter(object):
        if isinstance(object, datetime.datetime):
            return object.__str__()

    record = json.dumps(record[0], default = myconverter)
    record_vendors = json.dumps(record_vendors)

    if request.POST['action'] == 'Save':
            if form_claim.is_valid() and form_vendor.is_valid():
                form_claim.save(commit=True)
                form_vendor.save(commit=True)

                return view_records(request)

    return render(request, 'myapp/modify_record.html',
        {'form_claim':form_claim,
        'record':record,
        'form_vendor':form_vendor,
        'record_vendors':record_vendors}
        )



def view_records(request):
    form_claim = ClaimForm()
    form_vendor = mult_vendor()
    claim_list = Claim.objects.all()
    claim_filter = ClaimFilter(request.GET, queryset=claim_list)

    if request.method == 'POST':
        if request.POST['action'] == 'Submit':
            global record_pk
            record_pk = request.POST['RecID']
            print()
            try:
                global record
                record = Claim.objects.filter(pk=record_pk)
            except ValueError:
                return render(request, 'myapp/modify_record.html',
                    {'form_claim':form_claim,
                    'record':record,
                    'form_vendor':form_vendor,
                    'record_vendors':record_vendors}
                )
            return post_record(request, record)
        else:
            form_claim = ClaimForm(request.POST)
            form_vendor = mult_vendor(request.POST)
            if form_claim.is_valid() and form_vendor.is_valid():

                claim = Claim.objects.get(id=record_pk)
                claim.open_date = form_claim.cleaned_data['open_date']
                claim.claim_type = form_claim.cleaned_data['claim_type']
                claim.contract = form_claim.cleaned_data['contract']
                claim.po = form_claim.cleaned_data['po']
                claim.original_value = form_claim.cleaned_data['original_value']
                claim.estimated_value = form_claim.cleaned_data['estimated_value']
                claim.nature = form_claim.cleaned_data['nature']
                claim.initiated_by = form_claim.cleaned_data['initiated_by']
                claim.responsible_rep = form_claim.cleaned_data['responsible_rep']
                claim.projects = form_claim.cleaned_data['projects']
                claim.status = form_claim.cleaned_data['status']
                claim.bus_unit = form_claim.cleaned_data['bus_unit']
                claim.description = form_claim.cleaned_data['description']
                claim.resolution = form_claim.cleaned_data['resolution']
                claim.close_date = form_claim.cleaned_data['close_date']
                claim.save()

                vendor_obj = Vendor.objects.filter(vendor_claim_ref=record_pk).delete()
                obj = Claim.objects.get(id=record_pk)
                for vendor_instance in form_vendor.cleaned_data:
                    if len(vendor_instance) !=0:
                        Vendor.objects.create(vendor_claim_ref = obj,
                                            vendor_number = vendor_instance['vendor_number'],
                                            vendor_name = vendor_instance['vendor_name'])
            return render(request, 'myapp/get_records.html', {'filter': claim_filter})
    else:
        return render(request, 'myapp/get_records.html', {'filter': claim_filter})
