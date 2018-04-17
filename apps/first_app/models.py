from __future__ import unicode_literals
from django.db import models
import bcrypt
from datetime import datetime

class UserManager(models.Manager):
    def val_reg(self, postData):
        print postData
        errors = []
        name = postData['name']
        username = postData['username']
        password = postData['password']
        c_password = postData['c_password']

        if len(name) is 0:
            errors.append('Name is required')
        elif len(name) < 3:
            errors.append('Name must be at least 3 characters')
        if len(username) is 0:
            errors.append('Username is required')
        elif len(username) < 3:
            errors.append('Username must be at least 3 characters')
        if len(password) is 0:
            errors.append('Password is required')
        elif len(password) < 8:
            errors.append('Password must be at least 8 letters')
        elif not password.isalpha():
            errors.append('Password must only be letters')
        elif password != c_password:
            errors.append('Passwords must match')

        if len(errors) > 0:
            return (False, errors)
        else: 
            result = User.objects.filter(username=username)
            if len(result) > 0:
                errors.append('Username already exists')
                return (False, errors)
            else: 
                new_user = self.create(
                    name = name,
                    username = username,
                    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                )
            return (True, new_user)

    def val_log(self, postData):
        username = postData['username']
        password = postData['password']
        if len(username) is 0:
            errors.append('Username is required')
        elif len(username) < 3:
            errors.append('Username must be at least 3 characters')
        if len(password) is 0:
            errors.append('Password is required')
        elif len(password) < 8:
            errors.append('Password must be at least 8 letters')
        elif not password.isalpha():
            errors.append('Password must only be letters')
        if len(errors) > 0:
            return (False, errors)
        else:
            result = self.filter(username=username)
            if len(result) > 0:
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    return (True, user)
                else: errors.append('Username/Password combo')
                return (False, errors)
            else:
                errors.append('Username/Password combo')
                return (False, errors)

class TripManager(models.Model):
    def trip_val(self, postDate, id):
        print postData
        errors = []
        destination = postData['destination']
        description = postData['description']
        start = postData['start']
        end = postData['end']

        if len(destination) is 0:
            errors.append('No empty entries for destination field')
        if len(description) is 0:
            errors.append('No empty entries for description field')
        if datetime.date > datetime.date(year=2018, month=4, day=17)postData['start']): # need help on setting datetime
            errors.append('Travel Date From should be future-dated')
        if datetime.date > datetime.date(year=2018, month=4, day=17)postData['end']:
            errors.append('Travel Date To should not be before the Travel Date From')

    def join(self, id, trip_id):
        if len(Trip.objects.filter(id=trip_id).filter(join_id=id)) > 0:
            return { 'errors':'You already joined this trip' }
        else:
            users = User.objects.get(id=id)
            book = self.get(id=trip_id)
            book.join.add(users)
        return {}

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    added_by = models.ForeignKey(User, related_name="users")
    join = models.ManyToManyField(User, related_name="joiner")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()