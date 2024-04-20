from django.contrib.auth.models import UserManager


def normalize_mobile_number(mobile_number):
    if len(str(mobile_number)) < 10:
        raise ValueError("Invalid mobile number format")
    return mobile_number


class MainUserManager(UserManager):

    def create_user(self, email=None, role_id=None, password=None, **extra_fields):
        if not email:
            raise ValueError("email is required")
        # if not phone_number:
        #     raise ValueError("mobile number is required")
        role = None
        if not role_id:
            from user.models import Role
            role = Role.objects.get(name="User")
        else:
            from user.models import Role
            role = Role.objects.get(id=role_id)
        if not role:
            raise ValueError(f"No no role found with name {'User' if not role_id else 'Super Admin'}")

        email = self.normalize_email(email)
        # phone_number = normalize_mobile_number(mobile_number=phone_number)
        user = self.model(email=email, role_id=role.id, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_stuff", True)
        extra_fields.setdefault("is_active", True)
        # print(email)
        return self.create_user(email, 1, password, **extra_fields)
