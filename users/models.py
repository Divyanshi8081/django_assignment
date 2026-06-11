from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=255)
    username   = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    # Foreign key relationship at MODEL level only — NOT at database level
    # Using IntegerField instead of ForeignKey so no DB constraint is created
    user       = models.IntegerField(help_text="Stores the User ID (model-level FK only)")
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_user(self):
        """Manually resolve the related User (no DB-level FK)."""
        try:
            return User.objects.get(id=self.user)
        except User.DoesNotExist:
            return None

    def __str__(self):
        return f"Post #{self.id} by user_id={self.user}"
