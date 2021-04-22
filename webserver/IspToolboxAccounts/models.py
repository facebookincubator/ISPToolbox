# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, first & last name and
        password
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    class Meta:
        db_table = 'auth_user'


class IspToolboxUserSignUpInfo(models.Model):
    SUBSCRIBER_SIZE_CHOICES = (
        ("", _("Choose subscriber size")),
        ("aspiring", _("I don\'t service anyone right now")),
        ("small", _("1 - 100")),
        ("medium", _("101 - 500")),
        ("large", _("501 - 2,000")),
        ("xlarge", _("2,001 - 5,000")),
        ("xxlarge", _("5,000+")),
    )
    ROLE_CHOICES = (
       ("bus_fin", _("Business & Finance")),
       ("tech_install", _("Tech & Installation")),
       ("mar_sales", _("Marketing & Sales")),
    )
    GOAL_CHOICES = (
       ("start_business", _("Start an ISP Business")),
       ("customer_acquistion", _("Acquire more customers")),
       ("expansion", _("Expand service to new areas")),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_website = models.CharField(max_length=100, null=True)
    subscriber_size = models.CharField(
        null=True,
        max_length=50,
    )
    individual_role = models.CharField(
        null=True,
        max_length=200,
    )
    company_goal = models.CharField(
        null=True,
        max_length=500,
    )

    # ip_prefix = models.GenericIPAddressField()
    # ip_prefix_length = models.IntegerField()

    # asn = models.CharField(max_length=30)
