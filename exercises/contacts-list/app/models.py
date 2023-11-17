from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()

def create_contact(name, email, phone, is_favorite):
    new_contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    new_contact.save()
    return new_contact
    
def all_contacts():
    return Contact.objects.all()
    
def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except Contact.DoesNotExist:
        return None

def favorite_contacts():
    favorite_contacts_ = Contact.objects.filter(is_favorite=True)
    return favorite_contacts_

def update_contact_email(name, new_email):
    contacts_to_update = Contact.objects.filter(name=name)
    if contacts_to_update.exists():
        contacts_to_update.update(email=new_email)
        updated_contacts = Contact.objects.filter(name=name)
        return updated_contacts
    else:
        return None
    
def delete_contact(name):
    contacts_to_delete = Contact.objects.filter(name=name)
    if contacts_to_delete.exists():
        deleted_contact = contacts_to_delete.first()
        contacts_to_delete.delete()
        return deleted_contact
    else:
        return None
