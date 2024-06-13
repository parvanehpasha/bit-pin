from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    # create user method
    def create_user(self, username, mobile, password):
        if not mobile:
            raise ValueError('User must have a phone number')

        user = self.model(
                    username=username,
                    mobile=mobile)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # super user admin
    def create_superuser(self, username, mobile, password):
        user = self.create_user(username, mobile, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
