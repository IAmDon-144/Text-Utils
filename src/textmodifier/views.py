from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,FileResponse
from django.core.files import File
from PIL import Image,ImageDraw
from reportlab.pdfgen import canvas
from gtts import gTTS
import time
import reportlab
import io
import os
import qrcode
import png
from pyqrcode import QRCode
import string




def result(request):



    return render(request,'result.html')


def capital(request):
    f_time = time.time()
    text = request.GET.get('text','default')
    is_empty =False
    if len(text)==0:is_empty=True
    textc = text.upper()
    upper = False
    if text.isupper():
        upper = True
    textlen = len(textc)
    l_time = time.time()
    final_time = l_time - f_time
    context  = {
        'text':textc,
        'is_empty':is_empty,
        'upper':upper,
        'textlen':textlen,
        'final_time':final_time,
    }
    # print(text)

    return render(request,'capital.html',context)


def removePunc(request):
    f_time = time.time()
    if request.method == 'GET':

        text = request.GET.get('text','default')
        is_empty =False
        if len(text)==0:is_empty=True
        


        punc = string.punctuation


        for i in text:
            if i in punc:
                text = text.replace(i,'')
        textlen = len(text)
        l_time = time.time()
        final_time = l_time - f_time


        context  = {
            'text':text,
            'is_empty':is_empty,
            'textlen':textlen,
            'final_time':final_time,
        }
        # return JsonResponse(context,safe=False)
    return render(request,'removepunc.html',context)
    # return redirect('textmodifier:result')



def wordCount(request):

    f_time = time.time()
    text = request.GET.get('text','default')
    char =len(text)
    text = text.strip()

    count = 1
    for i in range(0,len(text)):
        if (text[i] ==" " and text[i+1]!=" "):
            count+=1
    sen_count = 0
    for j in text:
        if j == '.':
            sen_count+=1

    text = text.lower()    
    text = " "+text+" "    

    preposition_list = [" with "," at "," form "," into ", " during "," including "," until ", " against ", " among "," throughout" , " of "," to ", " in "," for "," on "," by "," despite "," towards "," upon "," concerning "," about "," like "," through "," over "," before "," between "," after "," since "," without "," under ",' within ',' along ', ' following ',' acorss '," behind "," beyond "," plus "," except "," but ", ' up ',' out ',' arround ', ' down ',' off ',' above ' ,' near ', ' in spite of ','  regarding', ' with regard to '," because of " ]

    pre_count  = 0 
    instance_count = 0
    instance_prepositions = []

    for i in preposition_list:
        instance_count = text.count(i)
        if instance_count>=1:
            instance_prepositions.append(i)

        pre_count+=instance_count
        instance_count = 0
    # print("PreCount ",pre_count)




    l_time = time.time()
    final_time = l_time - f_time

    context ={
        'count':count,
        'final_time':final_time,

        'sen_count':sen_count,
        'pre_count':pre_count,
        'instance_prepositions':instance_prepositions,
        'Char':char
    }
    return render(request,'wordcount.html',context)





def about(request):
    return render(request,'about.html')




def makePDF(request):

    textcontent = request.GET.get('text','default')
    textcontent.strip()
    pdf_word_list = textcontent.split(' ')
    list_for_pdf = []

    j = 12
    for i in range(0,len(pdf_word_list),12):
        string = ' '.join(pdf_word_list[i:j])
        list_for_pdf.append(string)
        j+=12


    buffer = io.BytesIO()


    file_name = f'{list_for_pdf[0][0:10]}.pdf'



    pdf = canvas.Canvas(buffer)
    pdf.setTitle(f'{file_name}')

    text =pdf.beginText(40,800)
    text.setFont('Courier',10)

    for line in list_for_pdf:
        text.textLine(line)
    pdf.drawText(text)
    pdf.showPage()

    pdf.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=file_name)





def lower(request):
    f_time = time.time()
    text = request.GET.get('text','default')
    is_empty =False
    if len(text)==0:is_empty=True
    textc = text.lower()
    lower = False
    if text.islower():
        lower = True
    textlen = len(textc)
    l_time = time.time()
    final_time = l_time - f_time
    context  = {
        'text':textc,
        'is_empty':is_empty,
        'lower':lower,
        'textlen':textlen,
        'final_time':final_time,
    }
    # print(text)

    return render(request,'lower.html',context)


def wordStartsWith(request):
    f_time = time.time()
    

    textc = request.GET.get('text','default')
    text = textc.strip(' ')
    text = ' ' + text
    text = text.lower()
    is_empty = False

    if len(text) == 1:
        is_empty = True
        
 




        
    a,b,c,d,e,f,g,h,i_,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z =0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0


    for i in range(0,len(text)):
        if text[i] == " " and is_empty ==False:
            if text[i+1] == 'a':a+=1
            if text[i+1] == 'b':b+=1
            if text[i+1] == 'c':c+=1
            if text[i+1] == 'd':d+=1
            if text[i+1] == 'e':e+=1
            if text[i+1] == 'f':f+=1
            if text[i+1] == 'g':g+=1
            if text[i+1] == 'h':h+=1
            if text[i+1] == 'i':i_+=1
            if text[i+1] == 'j':j+=1
            if text[i+1] == 'k':k+=1
            if text[i+1] == 'l':l+=1
            if text[i+1] == 'm':m+=1
            if text[i+1] == 'n':n+=1
            if text[i+1] == 'o':o+=1
            if text[i+1] == 'p':p+=1
            if text[i+1] == 'q':q+=1
            if text[i+1] == 'r':r+=1
            if text[i+1] == 's':s+=1
            if text[i+1] == 't':t+=1
            if text[i+1] == 'u':u+=1
            if text[i+1] == 'v':v+=1
            if text[i+1] == 'w':w+=1
            if text[i+1] == 'x':x+=1
            if text[i+1] == 'y':y+=1
            if text[i+1] == 'z':z+=1
    

    count_list =[a,b,c,d,e,f,g,h,i_,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


    a_words = []
    b_words = []
    c_words = []
    d_words = []
    e_words = []
    f_words = []
    g_words = []
    h_words = []
    i_words = []
    j_words = []
    k_words = []
    l_words = []
    m_words = []
    n_words = []
    o_words = []
    p_words = []
    q_words = []
    r_words = []
    s_words = []
    t_words = []
    u_words = []
    v_words = []
    w_words = []
    x_words = []
    y_words = []
    z_words = []


    textforwords = request.GET.get('text','default')
    textforwords =textforwords.strip(' ')

    if len(textforwords)>0:

        initial_list = textforwords.split(' ')
        initial_list =set(initial_list)

        final_list = list(initial_list)
        if '' in final_list:
            final_list.remove('')


        for _ in final_list:

            if _[0] =='a' or _[0] =='A':
                a_words.append(_)
            if _[0] =='b' or _[0] =='B':
                b_words.append(_)
            if _[0] =='c' or _[0] =='C':
                c_words.append(_)
            if _[0] =='d' or _[0] =='D':
                d_words.append(_)
            if _[0] =='e' or _[0] =='E':
                e_words.append(_)
            if _[0] =='f' or _[0] =='F':
                f_words.append(_)
            if _[0] =='g' or _[0] =='G':
                g_words.append(_)
            if _[0] =='h' or _[0] =='H':
                h_words.append(_)
            if _[0] =='i' or _[0] =='I':
                i_words.append(_)
            if _[0] =='j' or _[0] =='J':
                j_words.append(_)
            if _[0] =='k' or _[0] =='K':
                k_words.append(_)
            if _[0] =='l' or _[0] =='L':
                l_words.append(_)
            if _[0] =='m' or _[0] =='M':
                m_words.append(_)
            if _[0] =='n' or _[0] =='N':
                n_words.append(_)
            if _[0] =='o' or _[0] =='O':
                o_words.append(_)
            if _[0] =='p' or _[0] =='P':
                p_words.append(_)
            if _[0] =='q' or _[0] =='Q':
                q_words.append(_)
            if _[0] =='r' or _[0] =='R':
                r_words.append(_)
            if _[0] =='s' or _[0] =='S':
                s_words.append(_)
            if _[0] =='t' or _[0] =='T':
                t_words.append(_)
            if _[0] =='u' or _[0] =='U':
                u_words.append(_)
            if _[0] =='v' or _[0] =='V':
                v_words.append(_)
            if _[0] =='w' or _[0] =='W':
                w_words.append(_)
            if _[0] =='x' or _[0] =='X':
                x_words.append(_)
            if _[0] =='y' or _[0] =='Y':
                y_words.append(_)
            if _[0] =='z' or _[0] =='Z':
                z_words.append(_)
            else:
                pass


    letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    words_list = [
                    a_words,
                    b_words,
                    c_words,
                    d_words,
                    e_words,
                    f_words,
                    g_words,
                    h_words,
                    i_words,
                    j_words,
                    k_words,
                    l_words,
                    m_words,
                    n_words,
                    o_words,
                    p_words,
                    q_words,
                    r_words,
                    s_words,
                    t_words,
                    u_words,
                    v_words,
                    w_words,
                    x_words,
                    y_words,
                    z_words
    ]
    myzip = zip(letter_list,words_list,count_list)



    l_time = time.time()
    final_time = l_time - f_time

    context = {


        'final_time':final_time,
        'myzip':myzip,
        'is_empty':is_empty
    }
    return render(request,'textStartsWith.html',context)







def textToSpeech(request):

    if request.method =="GET":
        text = request.GET.get('text','default')
        title = text[0:text.find(' ')]
        is_empty = False
        if len(text) == 0:
            is_empty = True
        else:

            lang = detect(text)
            TTS = gTTS(text = text , lang=lang,slow=False)
            # TTS.save(f'static_project/audio/{title}.mp3')            
            # os.system(f'start static_project/audio/{title}.mp3')
            # p =  FileResponse(as_attachment=True,filename=(f'{title}.mp3'))

        context={
            'audio':f'{title}.mp3',
            # 'p':p,
            # 'is_empty':is_empty
            'text':text
        }
    return render(request,'texttospeech.html',context)


def firstWordCapital(request):


    f_time = time.time()

    text = request.GET.get('text','default')
    text = text.strip()
    is_empty =False
    if len(text) == 0:
        is_empty = True
    initial_list = text.split(' ')
    final_list  = []
    for word in initial_list:
        word = word.capitalize()
        final_list.append(word)
    final_text = ' '.join(final_list)


    l_time = time.time()

    final_time = l_time-f_time


    context ={
        'final_text':final_text,
        'final_time':final_time,
        'is_empty':is_empty

    }
    return render(request,'firstwordcapitaal.html',context)



def invisibleText(request):
    text = request.GET.get('text','default')

    context ={

        'text':text

    }

    return render(request,'invisible.html',context)


def textCheckup(request):
    text = request.GET.get('text','default')
    punctuation = 0
    alphabet =0
    spaces = 0
    upper_case = 0
    lower_case = 0
    digit = 0
    ascii_ = 0

    for letter in text:
        if letter.isalpha():alphabet+=1
        if letter.isspace():spaces+=1
        if letter.islower():lower_case+=1
        if letter.isupper():upper_case+=1
        if letter.isnumeric():digit+=1
        if letter.isascii():ascii_+=1
        if letter in string.punctuation:punctuation+=1

    listKey = ['Alphabet','Digit','UPPER CASE','lower case','Punctuation','Spaces','Ascii Letter']
    listValue = [alphabet,digit,upper_case,lower_case,punctuation,spaces,ascii_]
    final_list = zip(listKey,listValue)

    context = {
        'final_list':final_list,

    }
    return render(request,'info.html',context)