from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()

router.register('category', views.CategoryAPI, basename='category')
router.register('', views.RecipeAPI, basename='recipe')

urlpatterns = router.urls
