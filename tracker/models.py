from django.db import models

# For uploading images (optional)
def gun_part_upload_path(instance, filename):
    return f"gun_parts/{instance.order.id}/{filename}"

def design_upload_path(instance, filename):
    return f"designs/{instance.name}/{filename}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_in = models.DateField(auto_now_add=True)
    date_out = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    wants_engraving = models.BooleanField(default=False)
    wants_electroplating = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"

class Finish(models.Model):
    name = models.CharField(max_length=100)
    finish_type = models.CharField(max_length=100, help_text="e.g. Electroplating, Anodizing")
    color = models.CharField(max_length=100)
    pattern = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.color})"

class Design(models.Model):
    name = models.CharField(max_length=100)
    design_type = models.CharField(max_length=100, help_text="e.g. Engraving, Laser Etch")
    description = models.TextField()
    image = models.ImageField(upload_to=design_upload_path, blank=True, null=True)

    def __str__(self):
        return self.name

class GunPart(models.Model):
    PART_TYPES = [
        ('slide', 'Slide'),
        ('frame', 'Frame'),
        ('barrel', 'Barrel'),
        ('grip', 'Grip'),
        ('trigger', 'Trigger'),
        ('other', 'Other'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='parts')
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, blank=True)
    part_type = models.CharField(max_length=50, choices=PART_TYPES)
    finish = models.ForeignKey(Finish, on_delete=models.SET_NULL, null=True)
    design = models.ForeignKey(Design, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=gun_part_upload_path, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.part_type}"
    
class Customization(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='customizations')
    part_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    finish_type = models.CharField(max_length=100)
    design = models.ForeignKey(Design, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='customizations/', blank=True, null=True)

    def __str__(self):
        return f"Customization for {self.part_name} in Order #{self.order.id}"

