from django.db import models
from django.contrib.auth.models import User





# course detail
class Courses(models.Model):
    course_title = models.CharField("title", max_length=50)
    duration = models.CharField("duration", max_length=50)
    LEVELS = [
        ('1', 'beginner'),
        ('2', 'intermediate'),
        ('3', 'advanced'),
    ]
    level = models.CharField("level", max_length=1, choices=LEVELS)
    fee = models.IntegerField("fee", default=None)
    description = models.TextField("description", default=None)
    prerequisites = models.TextField("Prerequisites", default=None)
    thumbnail = models.ImageField("thumbnail", upload_to="course/thumbnail/", height_field=None, width_field=None, max_length=None, default=None, blank=True)
    video_thumbnail = models.FileField("video thumbnail", upload_to="course/thumbnail/", default=None, blank=True)
    created = models.DateTimeField("created", auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.course_title
    
    class Meta:
        ordering = ['-created']


# course curriculum
class Curriculum(models.Model):
    course = models.ForeignKey(Courses, verbose_name=("course_name"), on_delete=models.CASCADE, default=None)
    title = models.CharField("title", max_length=50)
    description = models.CharField("Description", max_length=50, default=None)
    def __str__(self):
        return self.title
        


    

# course lectures
class CourseLectures(models.Model):
    course = models.ForeignKey(Courses, verbose_name=("course_name"), on_delete=models.CASCADE, default=None)
    video_title = models.CharField("title", max_length=50, default=None)
    video = models.FileField("video", upload_to="course/videos", default=None)

    def __str__(self):
        return self.video_title


# account detail for payment
class PaymentDetail(models.Model):
    bank = models.CharField("Bank", max_length=50)
    card_number = models.CharField('ATM no.', max_length=50)
    expiry = models.DateField("Expiry", auto_now=False, auto_now_add=False)
    holder_name = models.CharField("Holder Name", max_length=50)

    def __str__(self):
        return self.holder_name

    
# payment model
class Payment(models.Model):
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name=("course"), on_delete=models.CASCADE, null=True) 
    payment_status = models.BooleanField("payment status")
    total_amount = models.IntegerField("amount")
    payment_date = models.DateTimeField("date", auto_now_add=True)
    payment_detail = models.ForeignKey(PaymentDetail, verbose_name=("payment detail"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
   

# enroll
class Enroll(models.Model):
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name=("course"), on_delete=models.CASCADE)
    payment_id = models.IntegerField("payment id", default=None, null=True)
    first_name = models.CharField("first", max_length=50, default=None, null=True)
    last_name = models.CharField("last", max_length=50, default=None, null=True)
    email = models.CharField("email", max_length=254, default=None, null=True)
    phone = models.CharField("phone", max_length=50, default=None, null=True)
    address = models.TextField("Address", default=None, null=True)

    def __str__(self):
        return self.course.course_title


