from django.db import models


class Category(models.Model):
    # Category model
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    # Recipe model
    category = models.ForeignKey(Category, related_name="recipes", on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    recipe_description = models.TextField()
    image = models.ImageField(upload_to='recipe_img/')
    composition = models.TextField(null=True, blank=True, default="Will be added soon")

    class Meta:
        ordering = ('recipe_title',)
        verbose_name_plural = "recipes"

    def __str__(self):
        return self.recipe_title
