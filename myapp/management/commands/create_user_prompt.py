import getpass
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.management import BaseCommand
from django.core.validators import validate_email


# custom commands with prompt No Arguments

class Command(BaseCommand):
    
    help = 'Create new user using prompt'

    def handle(self, *args, **kwargs):

        username = input('Enter username:  ')
        email    = input('Enter email:  ')
        password = getpass.getpass('Password: ')
        confirm_password = getpass.getpass('Confirm Password(same password again): ')

        # password  validation

        if not password:
            self.stdout.write(self.style.ERROR(f'Password is required'))


        if(password != confirm_password):
            self.stdout.write(self.style.ERROR(f'\nPassword and Confirm password mis-matched. Please enter same password'))
        
        else:

            # email validator
            try:
                
                # email format validator
                validate_email(value=email)
            
            except ValidationError:
                self.stdout.write(self.style.ERROR(f'Please enter valid email address'))
            
            else:
                # now check wether some user already exists with this email-id
                email_exists = User.objects.filter(email = email).exists()

                if(email_exists):
                    # user found  this email raise error
                    self.stdout.write(self.style.ERROR(f'\nUser already register with this email address. Please user different/unique email address'))
                
                else:

                # user name validator
                    username_exists = User.objects.filter(username = username).exists()

                    if(username_exists):
                        self.stdout.write(self.style.ERROR(F'\nUsername already register with this username. Please user differnt/unique username'))
                    
                    else:
                        # if user does not exists
                        try:
                            user = User.objects.create(username=username, email=email, password=password)

                        except ValidationError as e:
                            self.stdout.write(self.style.ERROR(f'\n Validation Errors: {e.message_dict}\n{e.messages}'))
                        
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f'\n Exception raise: During user creation\n {e}\n'))

                        else:
                            # set password and save user password
                            user.set_password(raw_password=password)
                            user.save()

                            # success message
                            self.stdout.write(self.style.SUCCESS(f'\nCongrats! dear {username} your account successfully created'))









    