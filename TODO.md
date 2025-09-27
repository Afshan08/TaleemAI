# TODO: Add Roles to User Auth in Datamanager App

- [x] Add UserProfile model to models.py with OneToOneField to User and role field (choices: teacher, student)
- [x] Update SignupForm in forms.py to include role selection field
- [x] Modify signup_view in views.py to create and save UserProfile with selected role
- [x] Register UserProfile in admin.py
- [ ] Run python manage.py makemigrations datamanager
- [ ] Run python manage.py migrate
