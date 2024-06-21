
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.core.management.base import BaseCommand

# custom command to create new user with Arguments Without Prompt
class Command(BaseCommand):
    # to define what this commands will exaclty do/perform certain action
    help = 'This commands will create a normal user using commands line'

    # take different arguments which is required to perform certain task
    def add_arguments(self, parser):

        # taking some arguments
        parser.add_argument('username', type=str, help='The username for user')
        parser.add_argument('email', type=str, help='Email of user account')
        parser.add_argument('password', type=str, help='Password of user account ')

    
    # to perform that certain task using handle method
    def handle(self, *args, **kwargs):
        """This handle will perform the actual actual operation that you want to perform like data insertion, testing etc """

        # get/fetch all required arguments to perform the some task
        email    = kwargs.get('email') 
        username = kwargs.get('username')
        password = kwargs.get('password')

        print(f'\nInput Credential are: username: {username} email: {email}  password: {password} \n')

        # create new user logic 

        try:
            user = User.objects.create(username = username, email = email, password = password)
        
        # if validation failed 
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'\nError: {e.message} \n {e.message_dict}\n'))


        # any other exception is raise
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\nError: {str(e)} \n'))

        else:
            # set user password
            user.set_password(raw_password=password)
            user.save()

            # success message
            self.stdout.write(self.style.SUCCESS(F'\n Congrats!  new user is created successfully username is: {username}\n'))


      

