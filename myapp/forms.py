from django import forms
from django.forms import widgets, formset_factory
from bootstrap_datepicker_plus import DatePickerInput
from .models import Claim, Vendor

CLAIM_TYPE = [("",""),('Claim', 'Claim'),('Possible Claim','Possible Claim')]

NATURE = [("",""),('Disputed Change in Scope','Disputed Change in Scope'),
('Vendor Audit','Vendor Audit'), ('Disputed Contract Terms','Disputed Contract Terms'),
('Suspension or Termination','Suspension or Termination'),
('Warranty/Defective or Deficient Work','Warranty/Defective or Deficient Work'),
('Liability and Indemnification','Liability and Indemnification'),
('Other Contract Disputes','Other Contract Disputes'),
('Delays','Delays'), ('Compensation/Rates','Compensation/Rates'),
('ECA (incl. Vendor Audit)','ECA (incl. Vendor Audit)'),
('Lien','Lien'),('Other','Other')]

BINARY = [('',''),('Yes', 'Yes'),('No','No')]

OPEN_CLOSE = [('',''),('Open','Open'),('Closed','Closed')]

BU = [('',''),('Upstream','Upstream'),('Human Resources','Human Resources'),
('Finance','Finance'),('Legal','Legal'),('Downstream','Downstream'),
('Strategy & Operations Services', 'Strategy & Operations Services'),
('Chief Sustainability Office','Chief Sustainability Office'),
('Transformation Management Office','Transformation Management Office'),
('Fort Hills','Fort Hills'),('E & P','E & P')]

RESOLUTION = [('',''),('Monetary Settlement','Monetary Settlement'),('Future Discounts','Future Discounts'),
('New Commercial Agreement','New Commercial Agreement'),
('Lien Discharged through Court','Lien Discharged through Court'),
('Flag Management in Avetta','Flag Management in Avetta'),('Other','Other')]

class ClaimForm(forms.ModelForm):
    claim_type = forms.ChoiceField(choices=CLAIM_TYPE)
    nature = forms.ChoiceField(choices=NATURE)
    initiated_by = forms.ChoiceField(choices=BINARY, label='Was this claim initiated by Suncor?')
    projects = forms.ChoiceField(choices=BINARY, label='Was this claim in Projects?')
    status = forms.ChoiceField(choices=OPEN_CLOSE)
    bus_unit = forms.ChoiceField(choices=BU, label='Business Unit')
    original_value = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'$'}))
    estimated_value = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'$'}))
    resolution = forms.ChoiceField(choices=RESOLUTION, label='Resolution', required=False)

    class Meta:
        model = Claim
        fields = '__all__'
        widgets = {'open_date': DatePickerInput(),'close_date':DatePickerInput(),}

    def clean(self):
        cleaned_data = super().clean()
        open_date = cleaned_data.get("open_date")
        status = cleaned_data.get("status")
        close_date = cleaned_data.get("close_date")
        resolution = cleaned_data.get("resolution")
        if status == "Closed":
            if resolution == '':
                msg1 = "Choose Claim Resolution!"
                self.add_error('resolution', msg1)
            elif close_date == None:
                msg2 = "Choose Close Date!"
                self.add_error('close_date', msg2)
            elif close_date < open_date:
                msg3 = "Open Date must be before the Close Date"
                self.add_error('open_date', msg3)
                self.add_error('close_date', msg3)
        return cleaned_data

# This form is not inherited from the model because primary key from the Claim record is saved first
# as a foreign key in Vendor db table. Then vendor data will be added from the form
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_number', 'vendor_name']
    #vendor_number = forms.IntegerField(min_value=0, required=False)
    #vendor_name = forms.CharField(max_length=100)

mult_vendor = formset_factory(VendorForm, min_num=1, validate_min=1, max_num=5, extra=4)
