from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentForm(forms.Form):

	comments = forms.CharField( widget = forms.Textarea )

class LoginForms(forms.Form):
	username=forms.CharField()
	password = forms.CharField(widget= forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		if not User.objects.filter(username=username).exists():
			raise forms.ValidationError('User does not  exists.')
		user =User.objects.get(username=username)
		if not user.check_password(password):
			raise forms.ValidationError('Incorect password.')
class RegistrationForms(forms.ModelForm):
	password_check = forms.CharField(widget=forms.PasswordInput)
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'password',
		]

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		password_check = self.cleaned_data['password_check']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('User exists.')

		if password != password_check:
			raise forms.ValidationError('Password don\'t match.')