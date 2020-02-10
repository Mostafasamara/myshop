from django.db import models
from django.conf import settings
from orders.models import Order


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    # info = models.OneToOneField(Order)
    # user_info = models.get_object_or_404(Order,OrderCreateForm)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
