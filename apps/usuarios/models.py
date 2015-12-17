from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from datetime import datetime,date

class UserProfile(models.Model):
	user = models.OneToOneField(User,related_name='profile')
	mes_nac = models.IntegerField(null=True)
	dia_nac = models.IntegerField(null=True)
	anio_nac = models.IntegerField(null=True)
	activation_key = models.CharField(max_length=40, blank=True)
	key_expires = models.DateTimeField(default=datetime.today())

	class Meta:
		db_table = 'UserProfile'

	def user_profile(sender, instance, signal, *args, **kwargs):
		profile, new = UserProfile.objects.get_or_create(user=instance)

	signals.post_save.connect(user_profile, sender=User)