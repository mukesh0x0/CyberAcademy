from django.contrib import admin

from academy_app.models import CourseLectures, Courses, Enroll, Payment, PaymentDetail, Curriculum



# custom Admin text
admin.site.site_header = "CyberAcademy Admin"
admin.site.site_title = "CyberAcademy Admin Panel"
admin.site.index_title = "Welcome to CyberAcademy"



# course curriculum
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'description']
    class meta:
        model  = Curriculum


# course videos
class CourseLectureAdmin(admin.TabularInline):
    model = CourseLectures

    
# courses 
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseLectureAdmin]
    list_display = ['course_title', 'duration', 'level', 'fee', 'description', 'prerequisites', 'thumbnail', 'created']
    
    class Meta:
        model = Courses



# payment model
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'payment_status', 'total_amount', 'payment_date', 'payment_detail']
    class Meta:
        model = Payment



# payment detail
class PaymentDetailAdmin(admin.ModelAdmin):
    list_display = ['bank', 'card_number', 'expiry', 'holder_name']
    class Meta:
        model = PaymentDetail
        

# enroll model
class EnrollAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'payment_id', 'first_name', 'last_name', 'email', 'phone', 'address']
    class Meta:
        model = Enroll

# registering models
admin.site.register(Courses, CourseAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentDetail, PaymentDetailAdmin)
admin.site.register(Enroll, EnrollAdmin)
admin.site.register(Curriculum, CurriculumAdmin)