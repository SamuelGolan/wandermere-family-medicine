from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(
                              attrs={'class': "form-control", 'placeholder':'Your Email'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(
                              attrs={'class': "form-control", 'placeholder': 'Subject'}))
    name = forms.CharField(required=True, widget=forms.TextInput(
                              attrs={'class': "form-control", 'placeholder': 'Your Name'}))
    message = forms.CharField(widget=forms.Textarea(
                              attrs={'class': "form-control", 'placeholder': 'Message', 'rows':'5'}), required=True)
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['name']['placeholder'] = 'Your Name'
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'