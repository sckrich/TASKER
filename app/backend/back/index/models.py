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
    class Meta:
        managed = False
        db_table = 'Group'


class Task(models.Model):
    task_group = models.ForeignKey( 
        Group, 
        on_delete=models.CASCADE,
        related_name='tasks' 
    )
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    task_status = models.CharField(max_length=50, blank=True, null=True)
    assigned_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Task'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length = 255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    user_groups = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
  
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_email']
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_active(self):
        return True  
    
    @property
    def is_staff(self):
        return False 
    
    @property
    def is_superuser(self):
        return False 
    
    def has_perm(self, perm, obj=None):
        return False 
    
    def has_module_perms(self, app_label):
        return False 
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
