from django.db import models

class User(models.Model):
    # Facebook ID of user
    uid = models.CharField(max_length=100, primary_key=True)
    # Year that the user is in
    year = models.CharField(max_length=50)
    majorId = models.IntegerField(max_length=2, blank=True, null=True, default=None)
    def __unicode__(self):
        return self.uid
    
class Course(models.Model):
    # Course ID, incremented naturally
    uid = models.AutoField(primary_key=True)
    # Semester - Fall, Spring or Summer
    semester = models.CharField(max_length=10)
    # Year that the course is offered
    year = models.IntegerField(max_length=4)
    professor = models.CharField(max_length=100)
    # Rating - Average rating for the course
    rating = models.DoubleField()
    size = models.IntegerField(max_length=4)
    time = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    deptId = models.ForeignKey(Dept)
    


class Rating(models.Model):
    # Facebook ID of user
    uid = models.ForeignKey(User)
    cid = models.ForeignKey(Course)
    rating = models.IntegerField(max_length=2)
    comments = models.CharField(max_length=5000)
    
class Major(models.Model):
    # Major ID
    majorId = models.AutoField(primary_key=True)
    deptId = models.ForeignKey(Dept)
    majorName = models.CharField(max_length=100)
    
#class Enroll(models.Model):
#    uid = models.For
    
    
    

    
