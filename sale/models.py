from django.db import models

PREFERRED_CONTACT_METHOD = (
    ('phone', 'Phone Number'),
    ('email', 'Email Address'),
    ('both', 'Both')
)

CONDITIONS = (
    ("FN", "Factory New"),
    ("NE", "New Material"),
    ("NS", "New Surplus"),
    ("OH", "Overhauled"),
    ("SV", "Servicable"),
    ("RP", "Repariable"),
    ("AR", "As Removed")
)

PRIORITIES = (
    ("AOG", "Aircraft On Ground"),
    ("Immediate", "Within 1-2 Weeks"),
    ("Flexible", "No Specific Time")
)
# Create your models here.
class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=150)
    message = models.TextField()

class Quote(models.Model):
    class Meta:
        db_table = 'quote'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=12) # example: 321-555-5555
    email_address = models.EmailField(max_length=100)
    preferred_contact_method = models.CharField(choices= PREFERRED_CONTACT_METHOD, max_length=50)
    quantity = models.IntegerField()
    condition = models.CharField(choices=CONDITIONS, max_length=50)
    priority = models.CharField(choices=PRIORITIES, max_length=50)
    accepted_terms = models.BooleanField()