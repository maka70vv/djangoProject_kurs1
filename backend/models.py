from django.db import models


# Create your models here.
class Home(models.Model):
    main_image = models.ImageField()
    text_welcome = models.TextField()
    text_call = models.TextField(null=True)
    text_repair = models.TextField()
    text_services = models.TextField()
    client1 = models.CharField(max_length=100)
    client1_info = models.TextField()
    client2 = models.CharField(max_length=100)
    client2_info = models.TextField()
    client3 = models.CharField(max_length=100)
    client3_info = models.TextField()
    repair_image = models.ImageField()
    service_image = models.ImageField()
    image_down1 = models.ImageField(upload_to="")
    image_down2 = models.ImageField(upload_to="")
    image_down3 = models.ImageField(upload_to="")


class Service_content(models.Model):
    repair1 = models.CharField(max_length=100, null=True)
    repair2 = models.CharField(max_length=100, null=True)
    repair3 = models.CharField(max_length=100, null=True)
    repair4 = models.CharField(max_length=100, null=True)
    repair5 = models.CharField(max_length=100, null=True)
    repair6 = models.CharField(max_length=100, null=True)
    repair7 = models.CharField(max_length=100, null=True)
    repair8 = models.CharField(max_length=100, null=True)
    repair9 = models.CharField(max_length=100, null=True)
    price1 = models.CharField(max_length=20, null=True)
    price2 = models.CharField(max_length=20, null=True)
    price3 = models.CharField(max_length=20, null=True)
    price4 = models.CharField(max_length=20, null=True)
    price5 = models.CharField(max_length=20, null=True)
    price6 = models.CharField(max_length=20, null=True)
    price7 = models.CharField(max_length=20, null=True)
    price8 = models.CharField(max_length=20, null=True)
    price9 = models.CharField(max_length=20, null=True)
    image1 = models.ImageField(null=True, upload_to="")
    image2 = models.ImageField(null=True, upload_to="")
    text_content = models.TextField(null=True)
    image_down1 = models.ImageField(null=True, upload_to="")
    image_down2 = models.ImageField(null=True, upload_to="")
    image_down3 = models.ImageField(null=True, upload_to="")


class Form(models.Model):
    BROKEN = (
        ("TV", "TV"),
        ("Refrigerator", "Refrigerator"),
        ("Microwave ovens", "Microwave ovens"),
        ("Washing machine", "Washing machine"),
        ("Electric cooker", "Electric cooker"),
        ("Gas cooker", "Gas cooker"),
        ("Vacuum cleaners", "Vacuum cleaners"),
        ("Irons", "Irons"),
        ("Electric kettle", "Electric kettle"),
    )
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    broken = models.CharField(max_length=60, choices=BROKEN)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class About_us(models.Model):
    image1 = models.ImageField(upload_to="")
    image2 = models.ImageField(upload_to="")
    image3 = models.ImageField(upload_to="")
    text1_1 = models.TextField()
    text1_2 = models.TextField()
    text2_1 = models.TextField()
    text2_2 = models.TextField()
    image_down1 = models.ImageField(upload_to="")
    image_down2 = models.ImageField(upload_to="")
    image_down3 = models.ImageField(upload_to="")


class Contact(models.Model):
    name1 = models.CharField(max_length=50, null=True)
    name2 = models.CharField(max_length=50, null=True)
    name3 = models.CharField(max_length=50, null=True)
    insta = models.CharField(max_length=40, null=True)
    link_inst = models.URLField(null=True)
    phone_number1 = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15)
    phone_number3 = models.CharField(max_length=15)
    address = models.CharField(max_length=100, null=True)
    link_address = models.URLField(null=True)
    image_mem = models.ImageField(upload_to="")
    image_down1 = models.ImageField(upload_to="")
    image_down2 = models.ImageField(upload_to="")
    image_down3 = models.ImageField(upload_to="")


class Guides(models.Model):
    text = models.TextField(null=True)
    video1 = models.URLField()
    video2 = models.URLField()
    video3 = models.URLField()
    video4 = models.URLField()
    image_down1 = models.ImageField(upload_to="")
    image_down2 = models.ImageField(upload_to="")
    image_down3 = models.ImageField(upload_to="")
