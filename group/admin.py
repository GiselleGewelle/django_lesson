from django.contrib import admin

from group.models import Student, Teacher, Group

# Register your models here.
# admin.site.register(Student)
admin.site.register(Teacher)


# admin.site.register(Group)

@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('student_name', 'list_groups')

    def student_name(self, obj):
        print(self)
        return obj

    def list_groups(self, obj):
        # print(obj.id, obj.name, obj.last_name, obj.age, obj.contacts)
        # print(obj.groups.all(),'!!!!!!!!!!!!!!!!!!!!!!!')
        return [x for x in obj.groups.all()]


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'count_of_studetns', 'list_of_students')

    def count_of_studetns(self, obj):
        print(self)
        # print(obj,'!!!!!!!!!!!!!!!!!!!!!!!!!')
        qt = obj.students.count()
        # print(qt, '!!!!!!!!!!!!!!!!!!!!')
        return qt

    def list_of_students(self, obj):
        print(self)
        ls = [x for x in obj.students.all()]
        return ls
