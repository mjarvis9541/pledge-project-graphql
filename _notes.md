python -m pip install --upgrade pip
pip install django django-filter django-graphql-jwt graphene-django

# IMPORTANT: tokenAuth issue with PyJWT 2.0.1 -- revert to 1.7.0

pip install --upgrade PyJWT==1.7.0
