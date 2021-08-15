# -*- coding: utf-8 -*-
"""bourseLibre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog__ import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog__/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.urls import path
from . import views, views_notifications
from django.views.generic import TemplateView
from bourseLibre.views import handler400 as h400, handler403  as h403, handler404  as h404, handler500  as h500
#from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

# On import les vues de Django, avec un nom spécifique
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
# admin.autodiscover()
from django.contrib import admin
from .settings import MEDIA_ROOT
#from jugemaj import models

#from wiki import urls

admin.sites.site_header ="Admin "
admin.sites.site_title ="Admin Permacat"

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^captcha/', include('bourseLibre.captcha_local.urls')),
    url(r'^photolog/', include('photologue.urls', namespace='photologue')),
    #url(r'^chat/', include('chat.urls')),
    path(r'agenda/', include('cal.urls')),
    path(r'carto/', include('carto.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.bienvenue, name='bienvenue'),
    url(r'^bienvenue/$', views.bienvenue, name='bienvenue'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^gallerie/$', views.gallerie, name='gallerie'),
    path(r'admin/<str:asso>', views.admin_asso, name='admin_asso'),
    url(r'^permacat/fichiers/$', views.telechargements_asso, name='telechargements_asso'),
    url(r'^permacat/adhesion_asso/$', views.adhesion_asso, name='adhesion_asso'),
    url(r'^notifications/parType/$', views_notifications.notifications, name='notifications'),
    url(r'^notifications/activite/$', views_notifications.notifications_news_regroup, name='notifications_news'),
    url(r'^notifications/parDate/$', views_notifications.notificationsParDate, name='notificationsParDate'),
    url(r'^notifications/Lues/$', views_notifications.notificationsLues, name='notificationsLues'),
    url(r'^notificatioadherent_assons/changerDateNotif/$', views_notifications.changerDateNotif, name='changerDateNotif'),
    url(r'^notifications/notif_cejour/$', views_notifications.notif_cejour, name='notif_cejour'),
    url(r'^notifications/notif_cettesemaine/$', views_notifications.notif_cettesemaine, name='notif_cettesemaine'),
    url(r'^notifications/notif_cemois/$', views_notifications.notif_cemois, name='notif_cemois'),
    url(r'^notifications/visites/', views_notifications.voirDerniersArticlesVus, name='articles_visites'),
    url(r'^dernieresInfos/$', views_notifications.dernieresInfos, name='dernieresInfos'),
    url(r'^prochaines_rencontres/$', views.prochaines_rencontres, name='prochaines_rencontres'),
    path(r'presentation/<str:asso>/', views.presentation_asso, name='presentation_asso'),
    path(r'groupes/presentation/', views.presentation_groupes, name='presentation_groupes'),
    path(r'permagora/inscription/', views.inscription_permagora, name='inscription_permagora'),
    url(r'^site/presentation/$', views.presentation_site, name='presentation_site'),
    url(r'^permacat/statuts/$', views.statuts, name='statuts'),
    #url(r'^ramenetagraine/statuts/$', views.statuts_rtg, name='statuts_rtg'),


    url(r'^gestion/', admin.site.urls, name='admin',),

    #url(r'^jet/', include('jet.urls')),  # Django JET URLS
    #url(r'^jet/dashboard/', include('jet.dashboard.urls')),  # Django JET dashboard URLS
    #url(r'^admin/', admin.site.urls),


    url(r'^merci/$', views.merci, name='merci'),
    url(r'^forum/', include('blog.urls', namespace='bourseLibre.blog')),
    url(r'^jardins/', include('jardinpartage.urls', namespace='bourseLibre.jardinpartage')),
    url(r'^vote/', include('vote.urls', namespace='bourseLibre.vote')),
    url(r'^kit/', include('fiches.urls', namespace='bourseLibre.fiches')),
    url(r'^ateliers/', include('ateliers.urls', namespace='bourseLibre.ateliers')),
    url(r'^chercher/$', login_required(views.chercher), name='chercher'),
    url(r'^chercher/forum/$', login_required(views.chercher_articles), name='chercher_articles'),
    url(r'^accounts/profil/(?P<user_id>[0-9]+)/$', login_required(views.profil), name='profil',),
    url(r'^accounts/profil/(?P<user_username>[\w.@+-]+)/$', login_required(views.profil_nom), name='profil_nom',),
    url(r'^accounts/profile/$',  login_required(views.profil_courant), name='profil_courant',),
    url(r'^accounts/profil_inconnu/$', views.profil_inconnu, name='profil_inconnu',),
    url(r'^accounts/profil_modifier/$', login_required(views.profil_modifier.as_view()), name='profil_modifier',),
    url(r'^accounts/profil_supprimer/$', login_required(views.profil_supprimer.as_view()), name='profil_supprimer',),
    url(r'^accounts/profil_modifier_adresse/$', login_required(views.profil_modifier_adresse.as_view()), name='profil_modifier_adresse',),
    url(r'^accounts/profil_contact/(?P<user_id>[0-9]+)/$', login_required(views.profil_contact), name='profil_contact',),
    url(r'^accounts/mesSuivis/$', login_required(views.mesSuivis), name='mesSuivis',),
    url(r'^accounts/supprimerAction/(?P<actionid>[0-9]+)/$', login_required(views.supprimerAction), name='supprimerAction',),
    url(r'^accounts/mesActions/$', login_required(views.mesActions), name='mesActions',),
    url(r'^accounts/mctions/$', login_required(views.mesActions), name='mesActions',),
    url(r'^accounts/activite/(?P<pseudo>[\w.@+-]+)/$', login_required(views.activite), name='activite',),
    url(r'^register/$', views.register, name='senregistrer',),
    url(r'^reset-password/$',
        PasswordResetView.as_view(template_name='accounts/reset_password.html',
                                  email_template_name='accounts/reset_password_email.html',
                                  success_url=reverse_lazy('bienvenue')),
        name='reset_password'),
    #url(r'^password/reset/$', views.reset_password, name='reset_password'),
    url(r'^password/change/$', views.change_password, name='change_password'),
    path('auth/', include('django.contrib.auth.urls')),

    url(r'^contact_admins/$', views.contact_admins, name='contact_admins',),
    url(r'^charte/$', views.charte, name='charte',),
    url(r'^cgu/$', views.cgu, name='cgu',),
    url(r'^liens/$', views.liens, name='liens',),
    url(r'^fairedon/$', views.fairedon, name='fairedon',),
    #url(r'^agenda/$', views.agenda, name='agenda',),
    path(r'annuaire/<str:asso>', login_required(views.annuaire), name='annuaire',),
    path(r'cooperateurs/listeContacts/<str:asso>', login_required(views.listeContacts), name='listeContacts',),
    url(r'^cooperateurs/listeFollowers/$', login_required(views.listeFollowers), name='listeFollowers',),
    path(r'cooperateurs/carte/<str:asso>', login_required(views.carte), name='carte',),

    url(r'^cooperateurs/contacter_newsletter/$', login_required(views.contacter_newsletter), name='contacter_newsletter',),
    url(r'^cooperateurs/contacter_adherents/$', login_required(views.contacter_adherents), name='contacter_adherents',),

    url(r'^marche/proposer/(?P<type_produit>[-A-Za-z]+)/$', login_required(views.produit_proposer), name='produit_proposer', ),
    url(r'^marche/proposer/', login_required(views.proposerProduit_entree), name='produit_proposer_entree',),

    # url(r'^list$', views.product_list),
    #     url(r'^list2/$', FilterView.as_view(model=Produit, filterset_class=ProductFilter,)),
    url(r'^marche/$', login_required(views.ListeProduit.as_view()),  name="marche"),
    url(r'^marche/lister/$', login_required(views.ListeProduit.as_view()),  name="marche"),
    url(r'^marche/supprimerProduits_expires_confirmation/$', views.supprimerProduits_expires_confirmation,  name="supprimerProduits_expires_confirmation"),
    url(r'^marche/supprimerProduits_expires/$', views.supprimerProduits_expires,  name="supprimerProduits_expires"),
    url(r'^marche/lister_offres/', login_required(views.ListeProduit_offres.as_view()),
        name="marche_offres"),
    url(r'^marche/lister_recherches/', login_required(views.ListeProduit_recherches.as_view()),
        name="marche_recherches"),

    url(r'^marche/detail/(?P<produit_id>[0-9]+)/$', login_required(views.detailProduit), name='produit_detail',),

    url(r'^marche/modifier/(?P<pk>[0-9]+)/$',
        login_required(views.ProduitModifier.as_view()), name='produit_modifier', ),
    url(r'^marche/contacterProducteur/(?P<producteur_id>[0-9]+)/$',
        login_required(views.produitContacterProducteur), name='produit_contacterProducteur', ),
    url(r'^marche/supprimer/(?P<pk>[0-9]+)/$',
        login_required(views.ProduitSupprimer.as_view()), name='produit_supprimer', ),

    url(r'^panier/afficher/$', login_required(views.afficher_panier), name='panier_afficher', ),
    url(r'^panier/ajouter/(?P<produit_id>[0-9]+)/(?P<quantite>[0-9]{1,3}([.]{0,1}[0-9]{0,3}))/$',
        login_required(views.ajouterAuPanier), name='produit_ajouterAuPanier', ),
    url(r'^panier/supprimerItem/(?P<item_id>[0-9]+)',
        login_required(views.enlever_du_panier), name='supprimerDuPanier', ),

    url(r'^requetes/afficher/$',
        login_required(views.afficher_requetes), name='afficher_requetes', ),

    url(r'^conversations/(?P<destinataire>[\w.@+-]+)$', login_required(views.lireConversation), name='agora_conversation'),
    url(r'^conversations/(?P<destinataire1>[\w.@+-]+)/(?P<destinataire2>[\w.@+-]+)$', login_required(views.lireConversation_2noms), name='lireConversation_2noms'),
    url(r'^conversations/$', login_required(views.ListeConversations.as_view()), name='conversations'),
    url(r'^conversations/chercher/$', login_required(views.chercherConversation), name='chercher_conversation'),
    url(r'^suivre_conversation/$', views.suivre_conversations, name='suivre_conversations'),
    url(r'^suivre_produits/$', views.suivre_produits, name='suivre_produits'),
    url(r'^sereabonner/$', views.sereabonner, name='sereabonner'),
    path(r'agora/<str:asso>', login_required(views.agora), name='agora'),
    url(r'^activity/', include('actstream.urls')),

#    path(r'wiki_ecovillage_notifications/', include('django_nyt.urls')),
#    path(r'wiki_ecovillage/', include('wiki.urls')),


    url(r'^inscription_newsletter/$', views.inscription_newsletter, name='inscription_newsletter', ),
    path(r'modifier_message/<int:id>-<str:type_msg>-<str:asso>', views.modifier_message, name='modifierMessage'),
    url(r'^voirEmails/$', views_notifications.voirEmails,  name="voirEmails"),
    url(r'^nettoyerActions/$', views_notifications.nettoyerActions,  name="nettoyerActions"),
    url(r'^nettoyerHistoriqueAdmin/$', views_notifications.nettoyerHistoriqueAdmin,  name="nettoyerHistoriqueAdmin"),
    url(r'^envoyerEmailsRequete/$', views_notifications.envoyerEmailsRequete,  name="envoyerEmailsRequete"),
    url(r'^voir_articles_a_archiver/$', views_notifications.voir_articles_a_archiver,  name="voir_articles_a_archiver"),
    url(r'^archiverArticles/$', views_notifications.archiverArticles,  name="archiverArticles"),
]
urlpatterns += [
    url(r'^robots\.txt$', TemplateView.as_view(template_name="bourseLibre/robots.txt", content_type='text/plain')),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = h404
handler500 = h500
handler400 = h400
handler403 = h403

if settings.LOCALL:
    import debug_toolbar
    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)),] + urlpatterns
    #urlpatterns += url('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

