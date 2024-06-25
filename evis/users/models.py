from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, EmailField, ImageField, Model, PositiveBigIntegerField, URLField
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from evis.users.managers import UserManager

REGISTER_TYPE = (
    ("speaker", "Speaker"),
    ("conference", "Conference"),
    ("exhibitor", "Exhibitor"),
    ("visitor", "Visitor"),
    ("sponsor", "Sponsor"),
    ("partner", "Partner"),
    ("media", "Media"),
)


class User(AbstractUser):
    """
    Default custom user model for evis.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore
    picture = ImageField(upload_to="profile_pictures/", default="profile_pictures/default.jpg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class RegisterLink(Model):
    link = URLField(unique=True)
    type = CharField(max_length=20, choices=REGISTER_TYPE, unique=True)
    created_at = DateTimeField(auto_now_add=timezone.now)
    rank = PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.link

    class Meta:
        unique_together = ("type", "link")
