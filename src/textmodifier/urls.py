from django.urls import path, include
from .views import result,capital,removePunc,wordCount,about,makePDF,lower,wordStartsWith,textToSpeech,firstWordCapital,invisibleText


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
    path("invisible/",invisibleText,name='invisible'),


]
