# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Checkin(models.Model):
    sid = models.IntegerField(db_column='SID')  # Field name made lowercase.
    classid = models.TextField(db_column='CLASSID', blank=True, null=True)  # Field name made lowercase.
    checkin = models.TextField(db_column='CHECKIN', blank=True, null=True)  # Field name made lowercase.
    checkout = models.TextField(db_column='CHECKOUT', blank=True, null=True)  # Field name made lowercase.
    attendance = models.IntegerField(db_column='ATTENDANCE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHECKIN'


class Classdesc(models.Model):
    classid = models.TextField(db_column='CLASSID', primary_key=True)  # Field name made lowercase.
    starttime = models.TextField(db_column='STARTTIME')  # Field name made lowercase.
    endtime = models.TextField(db_column='ENDTIME')  # Field name made lowercase.
    day = models.IntegerField(db_column='DAY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLASSDESC'


class Register(models.Model):
    name = models.TextField(db_column='NAME')  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    password = models.TextField(db_column='PASSWORD', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    maddress = models.TextField(db_column='MADDRESS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REGISTER'
        unique_together = (('email', 'sid'),)


class Studentclass(models.Model):
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    classid = models.TextField(db_column='CLASSID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENTCLASS'
        unique_together = (('sid', 'classid'),)


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
