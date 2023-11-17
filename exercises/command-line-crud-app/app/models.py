from django.db import models

# Create your models here.
class Computer(models.Model):
    name = models.TextField()
    mac = models.TextField()
    model_num = models.IntegerField()
    location = models.TextField()

def create_computer(name, mac, model_num, location):
    new_computer = Computer(name=name, mac=mac, model_num=model_num, location=location)
    new_computer.save()
    return new_computer
    
def all_computers():
    return Computer.objects.all()
    
def find_computer_by_mac(mac):
    try:
        return Computer.objects.get(mac=mac)
    except Computer.DoesNotExist:
        return None

def computers_in_location(enter_location):
    computers_in = Computer.objects.filter(location=enter_location)
    return computers_in

def update_computer_location(mac, new_location):
    computers_to_update = Computer.objects.filter(mac=mac)
    if computers_to_update.exists():
        computers_to_update.update(location=new_location)
        updated_computers = Computer.objects.filter(mac=mac)
        return updated_computers
    else:
        return None
    
def delete_computer(mac):
    computers_to_delete = Computer.objects.filter(mac=mac)
    if computers_to_delete.exists():
        deleted_computer = computers_to_delete.first()
        computers_to_delete.delete()
        return deleted_computer
    else:
        return None
