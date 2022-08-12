from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class MatchRequest(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="match_request_user",
    )
    match_request_for = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="match_requested_for_user",
    )
    is_accepted = models.BooleanField(
        default="False",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class ProfileConfig(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="profile_configs",
    )
    show_me_on_search = models.BooleanField(
        default="True",
    )
    show_profile_image = models.BooleanField(
        default="True",
    )
    show_cover_image = models.BooleanField(
        default="True",
    )
    show_country = models.BooleanField(
        default="True",
    )
    show_city = models.BooleanField(
        default="True",
    )
    show_phone_number = models.BooleanField(
        default="True",
    )
    show_interests = models.BooleanField(
        default="True",
    )
    show_skills = models.BooleanField(
        default="True",
    )
    radius_of_interest = models.IntegerField(
        default="100",
        help_text="_",
    )
    interest_gender = models.CharField(
        null=True,
        blank=True,
        max_length=128,
    )

    def __str__(self):
        return self.user.username


class Interest(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name


class MatchDenied(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="match_denied_user",
    )
    match_denied_with = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="match_denied_with_user",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class UserProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="profile_info",
    )
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile_photos",
    )
    cover_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="cover_photos",
    )
    bio = models.TextField(
        null=True,
        blank=True,
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
    )
    country = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    city = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    phone_number = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    interests = models.ManyToManyField(
        "users.Interest",
        blank=True,
        related_name="user_interests",
    )
    skills = models.ManyToManyField(
        "users.Skill",
        blank=True,
        related_name="user_skills",
    )
    gender = models.CharField(
        null=True,
        blank=True,
        max_length=128,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username


class Match(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="match_user",
    )
    match_with = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="match_with_user",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Skill(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name
