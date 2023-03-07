from .models import Session
from django.contrib.auth.models import User
from users.models import Profile
from django import forms
from datetime import datetime

FOCUS_CHOICES = [
    ("listening", "Listening"),
    ("scales", "Scales and Arpeggios"),
    ("technique", "Technique"),
    ("sightreading", "Sightreading"),
    ("rhythm", "Rhythm"),
    ("memorising", "Memorising"),
    ("performing", "Performing"),
    ("musicality", "Musicality"),
]

MOOD_CHOICES = [
    ("confident", "Confident"),
    ("anxious", "Anxious"),
    ("hopeful", "Hopeful"),
    ("pessimistic", "Pessimistic"),
    ("motivated", "Motivated"),
    ("discouraged", "Discouraged"),
    ("determined", "Determined"),
    ("overwhelmed", "Overwhelmed"),
    ("ambitious", "Ambitious"),
    ("doubtful", "Doubtful"),
    ("focused", "Focused"),
    ("distracted", "Distracted"),
    ("excited", "Excited"),
    ("bored", "Bored"),
    ("engaged", "Engaged"),
    ("disinterested", "Disinterested"),
    ("inspired", "Inspired"),
    ("uninspired", "Uninspired"),
    ("enthusiastic", "Enthusiastic"),
    ("disheartened", "Disheartened"),
    ("empowered", "Empowered"),
    ("defeated", "Defeated"),
    ("encouraged", "Encouraged"),
    ("despondent", "Despondent"),
    ("curious", "Curious"),
    ("frustrated", "Frustrated"),
    ("accomplished", "Accomplished"),
    ("disappointed", "Disappointed"),
    ("productive", "Productive"),
    ("procrastinating", "Procrastinating"),
]


class CreateSessionForm(forms.ModelForm):

    # focus = forms.MultipleChoiceField()

    class Meta:
        model = Session
        fields = ["headline", "date", "duration", "focus", "summary", "moods"]

    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields["headline"].widget = forms.TextInput(
            attrs={
                "placeholder": "One sentence that describes your practice...",
                "label": "Add a headline",
                "class": "input-field py-1",
            }
        )
        # https://stackoverflow.com/questions/61076688/django-form-dateinput-with-widget-in-update-loosing-the-initial-value
        self.fields["date"].widget = forms.DateTimeInput(
            attrs={
                "class": "form-control input-field py-1",
                "placeholder": "",
                "type": "date",
                "max": datetime.now().date(),
            }
        )

        self.fields["duration"].widget = forms.NumberInput(
            attrs={
                "placeholder": "",
                "label": "",
                "class": "form-control input-field py-1",
                "type": "number",
            }
        )

        self.fields["focus"] = forms.MultipleChoiceField(
            choices=FOCUS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False
        )

        self.fields["moods"] = forms.MultipleChoiceField(
            choices=MOOD_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False
        )

        self.fields["summary"].widget = forms.Textarea(
            attrs={
                "placeholder": "Reflect on your practice. What went well? What will you work on next time?"
            }
        )


        # Edited from ChatGPT
    def moods_as_columns(self):
            """
            Render the moods field as two columns of checkboxes.
            """
            choices = self.fields['moods'].choices
            num_per_column = len(choices) // 2
            col1 = choices[:num_per_column]
            col2 = choices[num_per_column:]
            col1_html = ''.join(f'<label"><input class="mx-1" type="checkbox" name="moods" value={choice[0]}>{choice[1]}</label><br>' for choice in col1)
            col2_html = ''.join(f'<label"><input class="mx-1" type="checkbox" name="moods" value={choice[0]}>{choice[1]}</label><br>' for choice in col2)
            return f'<div class="row"><div class="col-sm-6">{col1_html}</div><div class="col-sm-6">{col2_html}</div></div>'
