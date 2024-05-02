from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password

from .models import User

from companies.models import Enterprise, Employee


class Authentication:
    def signin(self, email=None, password=None) -> User:

        EXCEPTION_AUTH = AuthenticationFailed('Email or password is invalid')

        user_exists = User.objects.filter(email=email).exists()

        if not user_exists:
            return EXCEPTION_AUTH
        
        user = User.objects.filter(email=email).first()

        if check_password(password, user.password):

            raise EXCEPTION_AUTH

        return user
    

    def signup(self, name, email, password, type_account='owner', company_id=False):

        if not name or name == '':
            raise APIException('Name cannot be null')
        
        if not email or email == '':
            raise APIException('Email cannot be null')
        
        if not password:
            raise APIException('Password cannot be null')
        
        if type_account == 'employee' and not company_id:
            raise APIException('The field company_id cannot be null')

        user = User

        if user.objects.filter(email=email).exists():
            raise APIException('This email alredy used')
        
        password_hashed = make_password(password=password)

        user_created = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )

        if type_account == 'owner':
            enterprise_created = Enterprise.objects.create(
                name='Enterprise name',
                user_id=user_created.id
            )

        if type_account == 'employee':
            Employee.objects.create(
                enterprise_id=company_id or enterprise_created.id,
                user_id = user_created
            )

        return user_created