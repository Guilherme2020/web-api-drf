from django.db import models

# Create your models here.
class Game(models.Model):
	created = models.DateTimeField(auto_now_add=True,null=True)
	name = models.CharField(max_length=200, null=True, default='')
	release_date = models.DateTimeField(null=True)
	game_category = models.CharField(max_length=200, null=True, default='')
	played = models.BooleanField(default=False)

	class Meta:
		ordering = ('name',)
