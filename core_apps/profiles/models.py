from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimestampModel


User = get_user_model()


# Create your models here.
class Profile(TimestampModel):
    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        OTHER = "O", _("Other")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    phone_number = PhoneNumberField(
        verbose_name=_("phone number"),
        null=True,
        blank=True,
        max_length=30,
        default="0000000000",
    )

    about_me = models.TextField(
        verbose_name=_("about me"),
        default="say something about yourself",
    )

    gender = models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=30,
    )

    country = CountryField(verbose_name=_("country"), default="IN")

    city = models.CharField(verbose_name=_("city"), max_length=180, default="Bengaluru")

    profile_photo = models.ImageField(
        verbose_name=_("profile photo"), null=True, blank=True
    )

    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

    def follow(self, profile):
        if not self.is_following(profile):
            self.followers.add(profile)

    def unfollow(self, profile):
        if self.is_following(profile):
            self.followers.remove(profile)

    def is_following(self, profile):
        return self.followers.filter(pk=profile.pk).exists()
