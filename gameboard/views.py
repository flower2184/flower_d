from django.shortcuts import render, get_object_or_404, redirect
from .models import Games, Answer
from django.utils import timezone
from .forms import GamesForm, AnswerForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
import random


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    games_list = Games.objects.order_by('-create_date')

    paginator = Paginator(games_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'games_list': page_obj}  
    return render(request, 'gameboard/games_list.html', context)


def detail(request, games_id):
    games = get_object_or_404(Games, pk=games_id)
    context = {'games': games}
    return render(request, 'gameboard/games_detail.html', context)


@login_required(login_url='common:login')
def answer_create(request, games_id):
    games = get_object_or_404(Games, pk=games_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.nickname = request.user.first_name
            if form.cleaned_data.get('content').startswith('/주사위'):
                tmp = form.cleaned_data.get('content')
                try: 
                    num = int(tmp[4:])
                    dice = random.randint(1,num)
                    answer.content = '* 최대 주사위값: ' + str(num) + '\n* 게임 참가자의 주사위값: ' + str(dice)
                except ValueError:
                    answer.content = "[명령어 오류] 정확한 주사위 명령어를 입력하세요."

            elif form.cleaned_data.get('content').startswith('/배틀'):
                tmp = form.cleaned_data.get('content')
                try: 
                    me = request.user.first_name
                    conterpart = tmp[3:]
                    dice1 = random.randint(1,10)
                    dice2 = random.randint(1,10)
                    answer.content = str(me) + '의 주사위값: ' + str(dice1) + '\n' + str(conterpart) + '의 주사위값: ' + str(dice2)
                    if dice1 > dice2:
                        answer.content += '\n*** 승리: ' + str(me) + ' | 패배: ' + str(conterpart) + ' ***'
                    elif dice1 < dice2:
                        answer.content += '\n*** 승리: ' + str(conterpart) + ' | 패배: ' + str(me) + ' ***'
                    else:
                        answer.content += '\n*** 무승부 ***'

                except ValueError:
                    answer.content = "[명령어 오류] 정확한 배틀 명령어를 입력하세요."

            elif form.cleaned_data.get('content').startswith('/천하제일무술대회'):
                tmp = form.cleaned_data.get('content')
                try: 
                    dice = random.randint(1,10)
                    answer.content = '[EVENT] 천하제일 무술대회' + '\n* 획득 점수: +' + str(dice)
                except ValueError:
                    answer.content = "[명령어 오류] 정확한 이벤트 명령어를 입력하세요."
                
            else:
                answer.content = form.cleaned_data.get('content')
            answer.create_date = timezone.now()
            answer.create_date_str = timezone.localtime(timezone.now()).strftime('%m/%d %H:%M')
            answer.games = games
            answer.save()
            return redirect('gameboard:detail', games_id=games.id)
    else:
        form = AnswerForm()
    context = {'games': games, 'form': form}
    return render(request, 'gameboard/games_detail.html', context)


@login_required(login_url='common:login')
def games_create(request):
#    id = request.user.username # 현재 로그인된 유저의 아이디 불러오기
    if request.method == 'GET':
        forms = GamesForm()
        context = {'forms':forms}
        return render(request, 'gameboard/games_form.html',context)
    elif request.method == 'POST':
        forms = GamesForm(request.POST)
        if forms.is_valid():
            games = Games()
            games.author = request.user
            games.subject = forms.cleaned_data.get('subject')
            games.content = forms.cleaned_data.get('content')
            games.create_date = timezone.now()
            games.create_date_str = timezone.localtime(timezone.now()).strftime('%m/%d %H:%M')
            games.save()
            return redirect('gameboard:index')
        else:
            context = {'forms':forms}
            return render(request, 'gameboard/games_form.html',context)


@login_required(login_url='common:login')
def games_delete(request, games_id):
    games = get_object_or_404(Games, pk=games_id)
    if request.user != games.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('gameboard:detail', games_id=games.id)
    games.delete()
    return redirect('gameboard:index')


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('gameboard:detail', games_id=answer.games.id)