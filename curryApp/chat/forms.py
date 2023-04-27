from django import forms
from django.utils.translation import gettext_lazy
from . import models

User = models.User

# チャットルーム検索用のフォーム
class SearchForm(forms.Form):
    keywords = forms.CharField(
        label=gettext_lazy('keywords (split space)'),
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': gettext_lazy('Enter the room name.'),
            'class': 'form-control',
        }),
    )

    def get_keywords(self):
        init_keywords = ''
        keywords = init_keywords

        if self.is_valid():
            keywords = self.cleaned_data.get('keywords', init_keywords)

        return keywords

# チャットルーム作成/更新用のフォーム
class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        # 修正部分：participantsを追加
        fields = ('name', 'description', 'participants')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': gettext_lazy('Enter the room name.'),
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 10,
                'style': 'resize: none',
                'placeholder': gettext_lazy('Enter the description.'),
                'class': 'form-control',
            }),
            # 修正部分：participantsを追加、複数選択を可能とするためにSelectMultipleを指定
            'participants': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
        }


    # 修正部分：participantsの候補を定義
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participants'].queryset = User.objects.filter(is_staff=False)