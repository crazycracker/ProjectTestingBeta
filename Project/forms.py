from django import forms

from Project.models import requestTable


class SignupForm(forms.Form):
    username = forms.CharField(max_length=10,label='ID')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    type = forms.ChoiceField(choices=(('student','STUDENT') , ('faculty','FACULTY')), label='CHOICE')
    mobile_number = forms.CharField(max_length=10,label='MOBILE NUMBER')


    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.type = self.cleaned_data['type']
        user.mobile_number = self.cleaned_data['mobile_number']
        user.save()



class EventForm(forms.ModelForm):
    block = forms.CharField(label='BLOCK NAME', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'block_name'}))
    room_number = forms.CharField(label='ROOM NUMBER', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'room_number'}))
    startDateTime = forms.CharField(label='START DATE', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'startDateTime'}))
    endDateTime = forms.CharField(label='END DATE', widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'endDateTime'}))
    description = forms.CharField(label='DESCRIPTION', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter the description for the event'}))
    granter = forms.CharField(label='GRANTER', max_length=30,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'granter'}))
    sender = forms.CharField(widget=forms.HiddenInput(
        attrs={'class': 'form-control', 'id': 'sender'}))
    class Meta:
        model = requestTable
        fields = ("description", "granter","startDateTime","endDateTime","room_number")

    def save(self, commit=True):
        form = super(EventForm, self).save(commit=False)
        if commit:
            form.save()
        return form

