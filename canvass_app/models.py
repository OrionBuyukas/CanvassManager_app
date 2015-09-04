from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Canvasser(models.Model):
    user = models.OneToOneField(User)

    # Todo add location field
    # location = models.LocationField()

    #if user is logged in is working = true Store record somewhere?
    is_working = models.BooleanField(default=False)



# total leads
# can be parsed in the application javascript
#     confirmed_leads_today =
#     confirmed_total_leads =
#     number_of_leads =
#     total_leads =
#
# confirmed leads = sort leads by canvasser, sort by date today and leads by lead confirmed true false

class Manager(models.Model):
    user = models.ForeignKey(User)
    # location = models.LocationField()


class SalesPerson(models.Model):
    user = models.ForeignKey(User)


class Address(models.Model):

    street = models.CharField(max_length=120)
    city = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)
    state = models.CharField(max_length=2)


class HomeOwner(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.ForeignKey(Address)
    phone_number = models.ForeignKey(PhoneNumber)
    email = models.ForeignKey(Email)

    def __str__(self):
        return self.first_name + " " + self.last_name



class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=11)

class Email(models.Model):
    email = models.EmailField()

class Lead(models.Model):

    home_owner = models.ForeignKey(HomeOwner)

    address = models.ForeignKey(Address)




    sales_person = models.ForeignKey(SalesPerson, default=None)
    canvasser = models.ForeignKey(Canvasser)
    canvasser_comment = models.TextField(blank=True)
    sales_comment = models.TextField(blank=True)

    bid = models.ForeignKey(Bids)

    has_bid = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    sale_date = models.DateTimeField()
    add_date = models.DateTimeField(auto_now_add=True)
    estimate_date = models.DateTimeField()

    def __str__(self):
        return self.home_owner.first_name + " " + self.home_owner.last_name + " " + self.status

class LeadStatus(models.Model):
    #todo make dropdown on lead
    lead_text = models.CharField(max_length=220)

class Bids(models.Model):
    bid_amount = models.DecimalField()
    bid_content = models.TextField()





class Pitch(models.Model):
    title = models.CharField(max_length=150)
    pitch = models.TextField()
    canvasser = models.ForeignKey(Canvasser) #for when users want to edit their personal pitches

class Objection(models.Model):

    # author = models.ForeignKey(User)

    title = models.CharField(max_length=120)
    text = models.TextField()

    add_date = models.DateTimeField(auto_now_add=True)



class Rebuttal(models.Model):

    objection = models.ForeignKey(Objection)