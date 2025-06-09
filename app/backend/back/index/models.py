# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comment(models.Model):
    task = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)
    comment_content = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Comment'


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    group_password = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    task = models.ForeignKey('Task', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Group'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    task_status = models.CharField(max_length=50, blank=True, null=True)
    assigned_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Task'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    user_groups = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Usernotifications(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    invitation_description = models.TextField()
    creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UserNotifications'
