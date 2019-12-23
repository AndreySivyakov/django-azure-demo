from django.db import models

class Claim(models.Model):
    open_date = models.DateTimeField(null=True)
    claim_type = models.CharField(max_length=100, null=True)
    contract = models.BigIntegerField(null=True, blank=True, default=None)
    po = models.BigIntegerField(null=True, blank=True, default=None)
    original_value = models.BigIntegerField(null=True)
    estimated_value = models.BigIntegerField(null=True)
    nature = models.CharField(max_length=100, null=True)
    initiated_by = models.CharField(max_length=20, null=True)
    responsible_rep = models.CharField(max_length=100, null=True)
    projects = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
    bus_unit = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    resolution = models.CharField(max_length=100, blank=True, default=None, null=True)
    close_date = models.DateTimeField(null=True, blank=True, default=None)

    def __unicode__(self):
       return self.name

class Vendor(models.Model):
    vendor_claim_ref = models.ForeignKey(Claim, on_delete=models.CASCADE, blank=True, null=True)
    vendor_number = models.BigIntegerField(null=True, default=None)
    vendor_name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
       return self.name

#class Comment(models.Model):
    #comment_claim_ref = models.ForeignKey(Claim, on_delete=models.CASCADE, blank=True, null=True)
    #comment_date = models.DateTimeField(null=True)
    #content = models.TextField(null=True)

    #def __unicode__(self):
       #return self.name
