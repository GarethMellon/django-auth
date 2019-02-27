from django.contrib.auth.models import UserLogin

class EmailAuth:
    """Authenticate a user by an excat match on the email and password"""
    
    def authenticate(self, username=None, password=None):
        """Get instance of user based off the email and verify the password"""
        
        try:
            user = User.object.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """used by the django authentication system to retrieve a user instance"""
        
        try:
            user = User.object.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
            