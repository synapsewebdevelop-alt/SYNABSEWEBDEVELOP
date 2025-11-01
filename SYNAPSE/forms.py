from django.forms import ModelForm
from . models import USERS_DATA
class USERS_INFO(ModelForm):
    class META:
        model=USERS_DATA
        fields="_all_"
        