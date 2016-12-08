from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    artist_name = models.CharField(max_length=45)
    artist_people = models.CharField(max_length=45)
    artist_contact = models.CharField(max_length=45)
    artist_vk = models.CharField(max_length=45)
    class Meta:
        db_table = 'artist'
