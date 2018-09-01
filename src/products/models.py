import random
import os
from django.db import models

def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name, ext=os.path.splitext(base_name)
	return name, ext

def upload_image_path(instance, filename):
	#print(instance)
	#print(filename)
	new_filename=random.randint(1,39868478)
	name, ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "products/{new_filename}/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)

class Product(models.Model): #Product_Category
	title 		=	models.CharField(max_length=120)
	description	=	models.TextField()
	price 		=	models.DecimalField(decimal_places=2,max_digits=20, default=39.99)
	image		=	models.ImageField(upload_to=upload_image_path, null=True, blank=False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title
