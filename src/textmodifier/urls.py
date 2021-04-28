from django.urls import path, include
from .views import result,capital,removePunc,wordCount,about,makePDF,lower,wordStartsWith,textToSpeech,firstWordCapital,invisibleText,textCheckup,secRetCode,revealCode,passGen


app_name = "textmodifier"


urlpatterns = [
    
    
    path("",result,name='result'),
    path("capital/",capital,name='capital'),
    path("removepunc/",removePunc,name='remove-punc'),
    path("wordcount/",wordCount,name='word-count'),
    path("about/",about,name='about'),
    path("makepdf/",makePDF,name='make-pdf'),
    path("lower/",lower,name='lower'),
    path("wordstartswith/",wordStartsWith,name='word-s-w'),
    path("texttospeech/",textToSpeech,name='text-to-speech'),
    path("firstwordcapital/",firstWordCapital,name='first-word-capital'),
    path("textinformations/",textCheckup,name='text-informations'),
    path("invisible/",invisibleText,name='invisible'),
    path("secrettext/",secRetCode,name='secrettext'),    
    path("revealtext/",revealCode,name='revealtext'),
    path("passgen/",passGen,name='pass-gen'),



]
