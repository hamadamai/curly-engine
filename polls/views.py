from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice
from django.template import loader
from django.shortcuts import render
import sqlite3

que = []
cho1 = []
cho2 = []
conect = []
conect1 =[]
conect2 =[]
answer = []
answer2 = []
# データベース開く
db = sqlite3.connect('MyDatabase')
con = db.cursor()



sql1 = 'SELECT question_text FROM polls_question;'
for q in con.execute(sql1):
    #print(q)
    q1 = "".join(map(str, q))
    que.append(q1)

j=1
sql2 = 'SELECT choice_text FROM polls_choice;'
for c in con.execute(sql2):
    c1 = "".join(map(str, c))
    #print(c)
    if j%2 == 1:
        cho1.append(c1)
    else:
        cho2.append(c1)
    j+=1
sql10='select * from polls_member'
datum =db.execute(sql10)
nagasa = len(datum.fetchall())
answer.append(nagasa)
answer2.append(nagasa)
db.close()

def detailfirst(request):
    return render(request, 'myapp/index_first.html')

def detail0(request):
    if (request.method == 'POST'):
        answer.append(int(request.POST['years']))
    conect ={
        'question_0': que[0], 'choice1_0': cho1[0], 'choice2_0': cho2[0],
        'question_1': que[1], 'choice1_1': cho1[1], 'choice2_1': cho2[1],
        'question_2': que[2], 'choice1_2': cho1[2], 'choice2_2': cho2[2],
        'question_3': que[3], 'choice1_3': cho1[3], 'choice2_3': cho2[3],
        'question_4': que[4], 'choice1_4': cho1[4], 'choice2_4': cho2[4],
        'question_5': que[5], 'choice1_5': cho1[5], 'choice2_5': cho2[5],
        'question_6': que[6], 'choice1_6': cho1[6], 'choice2_6': cho2[6],
        'question_7': que[7], 'choice1_7': cho1[7], 'choice2_7': cho2[7],
        'question_8': que[8], 'choice1_8': cho1[8], 'choice2_8': cho2[8],
        'question_9': que[9], 'choice1_9': cho1[9], 'choice2_9': cho2[9],
        }
    return render(request, 'myapp/index.html', conect)




def detail1(request):
    if (request.method == 'POST'):
        answer.append(request.POST['example0'])
        answer.append(request.POST['example1'])
        answer.append(request.POST['example2'])
        answer.append(request.POST['example3'])
        answer.append(request.POST['example4'])
        answer.append(request.POST['example5'])
        answer.append(request.POST['example6'])
        answer.append(request.POST['example7'])
        answer.append(request.POST['example8'])
        answer.append(request.POST['example9'])

    conect1 ={
        'question_0': que[10], 'choice1_0': cho1[10], 'choice2_0': cho2[10],
        'question_1': que[11], 'choice1_1': cho1[11], 'choice2_1': cho2[11],
        'question_2': que[12], 'choice1_2': cho1[12], 'choice2_2': cho2[12],
        'question_3': que[13], 'choice1_3': cho1[13], 'choice2_3': cho2[13],
        'question_4': que[14], 'choice1_4': cho1[14], 'choice2_4': cho2[14],
        'question_5': que[15], 'choice1_5': cho1[15], 'choice2_5': cho2[15],
        'question_6': que[16], 'choice1_6': cho1[16], 'choice2_6': cho2[16],
        'question_7': que[17], 'choice1_7': cho1[17], 'choice2_7': cho2[17],
        'question_8': que[18], 'choice1_8': cho1[18], 'choice2_8': cho2[18],
        'question_9': que[19], 'choice1_9': cho1[19], 'choice2_9': cho2[19],
    }
    return render(request, 'myapp/index1.html', conect1)

def detail2(request):
    if (request.method == 'POST'):
        answer.append(request.POST['example0'])
        answer.append(request.POST['example1'])
        answer.append(request.POST['example2'])
        answer.append(request.POST['example3'])
        answer.append(request.POST['example4'])
        answer.append(request.POST['example5'])
        answer.append(request.POST['example6'])
        answer.append(request.POST['example7'])
        answer.append(request.POST['example8'])
        answer.append(request.POST['example9'])


    conect2 ={
        'question_0': que[20], 'choice1_0': cho1[20], 'choice2_0': cho2[20],
        'question_1': que[21], 'choice1_1': cho1[21], 'choice2_1': cho2[21],
        'question_2': que[22], 'choice1_2': cho1[22], 'choice2_2': cho2[22],
        'question_3': que[23], 'choice1_3': cho1[23], 'choice2_3': cho2[23],
        'question_4': que[24], 'choice1_4': cho1[24], 'choice2_4': cho2[24],
        'question_5': que[25], 'choice1_5': cho1[25], 'choice2_5': cho2[25],
        'question_6': que[26], 'choice1_6': cho1[26], 'choice2_6': cho2[26],
        'question_7': que[27], 'choice1_7': cho1[27], 'choice2_7': cho2[27],
        'question_8': que[28], 'choice1_8': cho1[28], 'choice2_8': cho2[28],
        'question_9': que[29], 'choice1_9': cho1[29], 'choice2_9': cho2[29],
    }
    return render(request, 'myapp/index2.html', conect2)

def detail3(request):
    if (request.method == 'POST'):
        answer.append(request.POST['example0'])
        answer.append(request.POST['example1'])
        answer.append(request.POST['example2'])
        answer.append(request.POST['example3'])
        answer.append(request.POST['example4'])
        answer.append(request.POST['example5'])
        answer.append(request.POST['example6'])
        answer.append(request.POST['example7'])
        answer.append(request.POST['example8'])
        answer.append(request.POST['example9'])


    conect3 ={
        'question_0': que[30], 'choice1_0': cho1[30], 'choice2_0': cho2[30],
        'question_1': que[31], 'choice1_1': cho1[31], 'choice2_1': cho2[31],
        'question_2': que[32], 'choice1_2': cho1[32], 'choice2_2': cho2[32],
        'question_3': que[33], 'choice1_3': cho1[33], 'choice2_3': cho2[33],
        'question_4': que[34], 'choice1_4': cho1[34], 'choice2_4': cho2[34],
        'question_5': que[35], 'choice1_5': cho1[35], 'choice2_5': cho2[35],
    }
    return render(request, 'myapp/index3.html', conect3)

def detail4(request):
    if (request.method == 'POST'):
        answer.append(request.POST['example0'])
        answer.append(request.POST['example1'])
        answer.append(request.POST['example2'])
        answer.append(request.POST['example3'])
        answer.append(request.POST['example4'])
        answer.append(request.POST['example5'])

    return render(request, 'myapp/index4.html')

def detail20(request):
    if (request.method == 'POST'):
        answer.append(request.POST['text'])
    conect20 = {
        'question_0': que[36], 'choice1_0': cho1[36], 'choice2_0': cho2[36],
        'question_1': que[37], 'choice1_1': cho1[37], 'choice2_1': cho2[37],
    }
    return render(request, 'myapp/index20.html', conect20)

def detail30(request):
    if (request.method == 'POST'):
        answer.append(request.POST['example0'])
        answer.append(request.POST['example1'])
    conect30 = {
        'question_0': que[38], 'choice1_0': cho1[38], 'choice2_0': cho2[38],
        'question_1': que[39], 'choice1_1': cho1[39], 'choice2_1': cho2[39],
        'question_2': que[40], 'choice1_2': cho1[40], 'choice2_2': cho2[40],
        'question_3': que[41], 'choice1_3': cho1[41], 'choice2_3': cho2[41],
    }
    return render(request, 'myapp/index30.html', conect30)



def detaillast(request):
    if (request.method == 'POST'):
        answer.append(request.POST['example0'])
        answer.append(request.POST['example1'])
        answer.append(request.POST['example2'])
        answer.append(request.POST['example3'])
        answer.append(request.POST['text'])
        print(answer)

        db100 = sqlite3.connect('MyDatabase')
        con100 = db100.cursor()
        con100.execute('INSERT INTO polls_member VALUES (?,?,?,?,?,?,?,?,?,?\
                       ,?,?,?,?,?,?,?,?,?,?\
                        ,?,?,?,?,?,?,?,?,?,?\
                        ,?,?,?,?,?,?,?,?,?,?\
                        ,?,?,?,?,?,?'')', answer)
        #con100.execute('INSERT INTO Member2 VALUES (?,?,?,?,?,?,?,?,?,?,?\
        #                      ,?,?,?,?,?\
        #                        '')', answer2)
        '''
        if (request.method == 'POST'):
        answer.append(int(request.POST['example0']))
        answer.append(int(request.POST['example1']))
        answer.append(int(request.POST['example2']))
        answer.append(int(request.POST['example3']))
        answer.append(int(request.POST['example4']))
        answer.append(int(request.POST['example5']))
        answer.append(int(request.POST['example6']))
        answer.append(int(request.POST['example7']))
        answer.append(int(request.POST['example8']))
        answer.append(int(request.POST['example9']))
        print(answer)
        '''


        db100.commit()
        db100.close()


    conectlast100 = {
        'msg': 'ご協力ありがとうございました！',
    }
    return render(request, 'myapp/index_last.html', conectlast100)

