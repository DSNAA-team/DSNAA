from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.db.models.fields import NullBooleanField
from tinymce.models import HTMLField


'''Class category'''


class Category(models.Model):
    theme = models.TextField(max_length=50)

    def __str__(self):
        return self.theme


'''Class Blog , relation FK avec class Categorie'''


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)
    autheur = models.ForeignKey(User, on_delete=CASCADE, null=True)
    titre = models.CharField(max_length=255, null=True)
    slug = models.SlugField(null=True)
    content =  HTMLField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
    image = models.ImageField(null=True,upload_to = "images/")
    blog_views = models.IntegerField(default=0)
    def __str__(self) :
        return self.titre


'''Class Documents , relation manytomany avec class library'''
pays = (
    ("1", "Afghanistan"),
    ("2", "Afrique du sud"),
    ("3", "Åland, îles"),
    ("4", "Albanie"),
    ("5", "Algérie"),
    ("6", "Allemagne"),
    ("7", "Andorre"),
    ("8", "Angola"),
    ("9", "Anguilla"),
    ("10", "Antarctique"),
    ("11", "Antigua et barbuda"),
    ("12", "Arabie saoudite"),
    ("13", "Argentine"),
    ("14", "Arménie"),
    ("15", "Aruba"),
    ("16", "Australie"),
    ("17", "Autriche"),
    ("18", "Azerbaïdjan"),
    ("19", "Bahamas"),
    ("20", "Bahreïn"),
    ("21", "Barbade"),
    ("22", "Bélarus"),
    ("23", "Belgique"),
    ("24", "Bangladesh"),
    ("25", "Belize"),
    ("26", "Bénin"),
    ("27", "Bermudes"),
    ("28", "Bhoutan"),
    ("29", "Bolivie, l'état plurinational de"),
    ("30", "Bonaire, saint eustache et saba"),
    ("31", "Bosnie herzégovine"),
    ("32", "Botswana"),
    ("33", "Bouvet, île"),
    ("34", "Brésil"),
    ("35", "Brunei darussalam"),
    ("36", "Bulgarie"),
    ("37", "Burkina faso"),
    ("38", "Burundi"),
    ("39", "Caïmans, îles"),
    ("40", "Cambodge"),
    ("41", "Cameroun"),
    ("42", "Canada"),
    ("43", "Cap vert"),
    ("44", "Centrafricaine, république"),
    ("45", "Chili"),
    ("46", "Chine"),
    ("47", "Christmas, île"),
    ("48", "Chypre"),
    ("49", "Cocos (keeling), îles"),
    ("50", "Colombie"),
    ("51", "Comores"),
    ("52", "Congo"),
    ("53", "Congo, la république démocratique du"),
    ("54", "Cook, îles"),
    ("55", "Corée, république de"),
    ("56", "Corée, république populaire démocratique de"),
    ("57", "Costa rica"),
    ("58", "Côte d'ivoire"),
    ("59", "Croatie"),
    ("60", "Cuba"),
    ("61", "Curaçao"),
    ("62", "Danemark"),
    ("63", "Djibouti"),
    ("64", "Dominicaine, république"),
    ("65", "Dominique"),
    ("66", "Égypte"),
    ("67", "El salvador"),
    ("68", "Émirats arabes unis"),
    ("69", "Équateur"),
    ("70", "Érythrée"),
    ("71", "Espagne"),
    ("72", "Estonie"),
    ("73", "États unis"),
    ("74", "Éthiopie"),
    ("75", "Falkland, îles (malvinas)"),
    ("76", "Féroé, îles"),
    ("77", "Fidji"),
    ("78", "Finlande"),
    ("79", "France"),
    ("80", "Gabon"),
    ("81", "Gambie"),
    ("82", "Géorgie"),
    ("83", "Géorgie du sud et les îles sandwich du sud"),
    ("84", "Ghana"),
    ("85", "Gibraltar"),
    ("86", "Grèce"),
    ("87", "Grenade"),
    ("88", "Groenland"),
    ("89", "Guadeloupe"),
    ("90", "Guam"),
    ("91", "Guatemala"),
    ("92", "Guernesey"),
    ("93", "Guinée"),
    ("94", "Guinée bissau"),
    ("95", "Guinée équatoriale"),
    ("96", "Guyana"),
    ("97", "Guyane française"),
    ("98", "Haïti"),
    ("99", "Heard et îles macdonald, île"),
    ("100", "Honduras"),
    ("101", "Hong kong"),
    ("102", "Hongrie"),
    ("103", "Île de man"),
    ("104", "Îles mineures éloignées des états unis"),
    ("105", "Îles vierges britanniques"),
    ("106", "Îles vierges des états unis"),
    ("107", "Inde"),
    ("108", "Indonésie"),
    ("109", "Iran, république islamique d'"),
    ("110", "Iraq"),
    ("111", "Irlande"),
    ("112", "Islande"),
    ("113", "Israël"),
    ("114", "Italie"),
    ("115", "Jamaïque"),
    ("116", "Japon"),
    ("117", "Jersey"),
    ("118", "Jordanie"),
    ("119", "Kazakhstan"),
    ("120", "Kenya"),
    ("121", "Kirghizistan"),
    ("122", "Kiribati"),
    ("123", "Koweït"),
    ("124", "Lao, république démocratique populaire"),
    ("125", "Lesotho"),
    ("126", "Lettonie"),
    ("127", "Liban"),
    ("128", "Libéria"),
    ("129", "Libye"),
    ("130", "Liechtenstein"),
    ("131", "Lituanie"),
    ("132", "Luxembourg"),
    ("133", "Macao"),
    ("134", "Macédoine, l'ex république yougoslave de"),
    ("135", "Madagascar"),
    ("136", "Malaisie"),
    ("137", "Malawi"),
    ("138", "Maldives"),
    ("139", "Mali"),
    ("140", "Malte"),
    ("141", "Mariannes du nord, îles"),
    ("142", "Maroc"),
    ("143", "Marshall, îles"),
    ("144", "Martinique"),
    ("145", "Maurice"),
    ("146", "Mauritanie"),
    ("147", "Mayotte"),
    ("148", "Mexique"),
    ("149", "Micronésie, états fédérés de"),
    ("150", "Moldova, république de"),
    ("151", "Monaco"),
    ("152", "Mongolie"),
    ("153", "Monténégro"),
    ("154", "Montserrat"),
    ("155", "Mozambique"),
    ("156", "Myanmar"),
    ("157", "Namibie"),
    ("158", "Nauru"),
    ("159", "Népal"),
    ("160", "Nicaragua"),
    ("161", "Niger"),
    ("162", "Nigéria"),
    ("163", "Niué"),
    ("164", "Norfolk, île"),
    ("165", "Norvège"),
    ("166", "Nouvelle calédonie"),
    ("167", "Nouvelle zélande"),
    ("168", "Océan indien, territoire britannique de l'"),
    ("169", "Oman"),
    ("170", "Ouganda"),
    ("171", "Ouzbékistan"),
    ("172", "Pakistan"),
    ("173", "Palaos"),
    ("174", "Palestinien occupé, territoire"),
    ("175", "Panama"),
    ("176", "Papouasie nouvelle guinée"),
    ("177", "Paraguay"),
    ("178", "Pays bas"),
    ("179", "Pérou"),
    ("180", "Philippines"),
    ("181", "Pitcairn"),
    ("182", "Pologne"),
    ("183", "Polynésie française"),
    ("184", "Porto rico"),
    ("185", "Portugal"),
    ("186", "Qatar"),
    ("187", "Réunion"),
    ("188", "Roumanie"),
    ("189", "Royaume uni"),
    ("190", "Russie, fédération de"),
    ("191", "Rwanda"),
    ("192", "Sahara occidental"),
    ("193", "Saint barthélemy"),
    ("194", "Sainte hélène, ascension et tristan da cunha"),
    ("195", "Sainte lucie"),
    ("196", "Saint kitts et nevis"),
    ("197", "Saint marin"),
    ("198", "Saint martin(partie française)"),
    ("199", "Saint martin (partie néerlandaise)"),
    ("200", "Saint pierre et miquelon"),
    ("201", "Saint siège (état de la cité du vatican)"),
    ("202", "Saint vincent et les grenadines"),
    ("203", "Salomon, îles"),
    ("204", "Samoa"),
    ("205", "Samoa américaines"),
    ("206", "Sao tomé et principe"),
    ("207", "Sénégal"),
    ("208", "Serbie"),
    ("209", "Seychelles"),
    ("210", "Sierra leone"),
    ("211", "Singapour"),
    ("212", "Slovaquie"),
    ("213", "Slovénie"),
    ("214", "Somalie"),
    ("215", "Soudan"),
    ("216", "Soudan du sud"),
    ("217", "Sri lanka"),
    ("218", "Suède"),
    ("219", "Suisse"),
    ("220", "Suriname"),
    ("221", "Svalbard et île jan mayen"),
    ("222", "Swaziland"),
    ("223", "Syrienne, république arabe"),
    ("224", "Tadjikistan"),
    ("225", "Taïwan, province de chine"),
    ("226", "Tanzanie, république unie de"),
    ("227", "Tchad"),
    ("228", "Tchèque, république"),
    ("229", "Terres australes françaises"),
    ("230", "Thaïlande"),
    ("231", "Timor leste"),
    ("232", "Togo"),
    ("233", "Tokelau"),
    ("234", "Tonga"),
    ("235", "Trinité et tobago"),
    ("236", "Tunisia"),
    ("237", "Turkménistan"),
    ("238", "Turks et caïcos, îles"),
    ("239", "Turquie"),
    ("240", "Tuvalu"),
    ("241", "Ukraine"),
    ("242", "Uruguay"),
    ("243", "Vanuatu"),
    ("244", "Venezuela, république bolivarienne du"),
    ("245", "Viet nam"),
    ("246", "Wallis et futuna"),
    ("247", "Yémen"),
    ("248", "Zambie")
)
types = (
    ("1", "PDF"),
    ("2", "TXT")
)

strat_natio = (
    ("1", "TRUE"),
    ("2", "FALSE")
)
lan = (
    ("1", "Fr"),
    ("2", "En"),
    ("3", "Ar"),

)


class Documents(models.Model):

    titre = models.CharField('Titre de document', max_length=20, unique=True)
    autheur = models.CharField(max_length=20)
    organization = models.CharField(max_length=20)
    date_publication = models.DateField()
    fichier = models.FileField(null=True, upload_to='uploads/')
    lien = models.CharField(max_length=30)
    mot_cle = models.CharField(null=True, max_length=30)
    type_de_doc = models.CharField(null=True, max_length=50, choices=types)
    pays = models.CharField(null=True, max_length=50, choices=pays)
    strategie_national = models.CharField(null=True, max_length=10)
    language = models.CharField(null=True, max_length=30, choices=lan)

    thumbnail = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.titre


'''Class library'''


class Library(models.Model):
    titre = models.CharField(max_length=255)
    date_creation = models.DateField()
    image = models.ImageField(null=True, upload_to='images/')
    document = models.ManyToManyField(
        Documents)

    def document_names(self):
        return "\n".join([p.titre for p in self.document.all()])

    def document_autheur(self):
        return "\n".join([p.autheur for p in self.document.all()])

    def document_thum(self):
        return "\n".join([p.thumbnail.path for p in self.document.all()])

    def document_org(self):
        return "\n".join([p.organization for p in self.document.all()])

    def document_Date(self):
        return "\n".join([p.date_publication.__str__() for p in self.document.all()])

    def document_Country(self):
        return "\n".join([p.get_pays_display.__str__() for p in self.document.all()])

    def document_lang(self):
        return "\n".join([p.get_language_display.__str__() for p in self.document.all()])

    def document_fich(self):
        return "\n".join([p.fichier.__str__() for p in self.document.all()])

    def __str__(self):
        return self.titre


'''Class Galery '''


class MediaCategory(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    thumbnail = models.ImageField(null=True)

    def __str__(self):
        return self.title




class Album(models.Model):

    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(null=True)
    Category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

   


'''Class Image '''


class Image(models.Model) : 

    titre = models.TextField(max_length=255)

    description = models.TextField(max_length=500)

    date_publication = models.DateTimeField(auto_now_add=True)

    lieu = models.TextField(max_length=40)

    image = models.ImageField()

    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=True)

    def __str__(self) :

        return self.titre


'''Class VideoLibrary '''


class VideoLibrary(models.Model):
    titre = models.TextField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.TextField(max_length=25)

    def __str__(self):
        return self.titre


'''Class Video '''


class Video(models.Model):
    titre = models.TextField(max_length=255)
    date_publication = models.DateTimeField(auto_now_add=True)
    organisation = models.TextField(max_length=40)
    longueur = models.FloatField()
    description = models.TextField(max_length=255)
    lien = models.TextField(max_length=100)
    videoLibrary = models.ManyToManyField(VideoLibrary)

    def __str__(self):
        return self.titre


'''Class Task'''


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


'''Class evenement'''


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    date_event = models.DateField()
    organizer = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    place = models.CharField(null=True, max_length=50)
    image = models.ImageField(null=True, upload_to="images/")

    def __str__(self):
        return self.title


'''Class fomrulaire contact'''


class ContactForm(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


# Create your models here.


class ContactForm(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
