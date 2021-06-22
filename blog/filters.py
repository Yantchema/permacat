from django import forms
from bourseLibre.models import Asso, Profil
from .models import Article, Choix
#from django_filters.views import FilterView
import django_filters
#from django.db import models
#from django_summernote.widgets import SummernoteWidget
#from photologue.models import Album
#from bourseLibre.constantes import Choix as Choix_global
from datetime import datetime, timedelta, timezone

class ArticleFilter(django_filters.FilterSet):
    asso = django_filters.ModelMultipleChoiceFilter(field_name='asso', queryset=Asso.objects.all().exclude(abreviation="jp"),
        widget=forms.CheckboxSelectMultiple)
    titre = django_filters.CharFilter(lookup_expr='icontains',)
    contenu = django_filters.CharFilter(lookup_expr='icontains', )
    auteur = django_filters.ModelChoiceFilter(field_name='auteur', queryset=Profil.objects.all().extra(\
    select={'lower_name':'lower(username)'}).order_by('lower_name'),
        )
    #date_creation = django_filters.DateFromToRangeFilter(label="Date de création de l'article", widget=forms.DateInput(attrs={'class':"date", }))
    #start_time = django_filters.DateFromToRangeFilter(label="Date de l'evenement associé à l'article", widget=forms.DateInput(attrs={'class':"date", }))
    date_creation = django_filters.NumberFilter(
        field_name='date_creation', method='get_past_n_days', label="Articles créés depuis X jours")

    def get_past_n_days(self, queryset, field_name, value):
        time_threshold = datetime.now() - timedelta(days=int(value))
        return queryset.filter(date_creation__gte=time_threshold)

    class Meta:
        model = Article
        fields = {
            'categorie': ['exact', ],
            'titre': ['icontains', ],
            'contenu': ['icontains', ],
            'auteur': ['exact', ],
            "asso": ['exact', ],
            #"start_time": ['range', ],
        }
    #
    # @property
    # def qs(self):
    #     parent = super().qs
    #     user = getattr(self.request, 'user', None)
    #
    #     for nomAsso in Choix_global.abreviationsAsso:
    #         if not getattr(user, "adherent_" + nomAsso):
    #             parent = parent.exclude(asso__abreviation=nomAsso)
    #     return parent
