from django.shortcuts import render
from chat.models import Messages
from django.db.models.query_utils import Q
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSerializer
from django.contrib.auth.models import User
from accounts.models import extUser
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
def getUserId(username):
    """
    Get the user id by the username
    :param username:
    :return: int
    """
    use = User.objects.get(username=username)
    id = use.id
    return id
    
@login_required(login_url='login')
def chat(request,username):
    """
    Get the chat between two users.
    :param request:
    :param username:
    :return:
    """    
    nuser=extUser.objects.exclude(user__id=request.user.id)
    muser=extUser.objects.get(user__id=request.user.id)
    friend = User.objects.get(username=username)
    id = getUserId(request.user.username)
    fuser=extUser.objects.get(user__id=friend.id)
    curr_user = User.objects.get(id=id)
    flag=1
    # print(curr_user,friend)
    messages = Messages.objects.filter(sender_name=id, receiver_name=friend.id) | Messages.objects.filter(sender_name=friend.id, receiver_name=id)
    # messages=zip(message,euser)

    if request.method == "GET":
        return render(request, "chats/chat.html",
                      {'messages': messages,
                       'curr_user': curr_user, 'friend': friend,'flag':flag ,'euser':muser,'fuser':fuser,'eusers':nuser})

@csrf_exempt 
@login_required(login_url='login')
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Messages.objects.filter(sender_name=sender, receiver_name=receiver, seen=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.seen = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@login_required(login_url='login')
def chathome(request):
    flag=0
    euser=extUser.objects.exclude(user__id=request.user.id)
    params={'flag':flag,'eusers':euser}
    return render(request,'chats/chat.html',params)

@login_required(login_url='login')
def chatsearch(request):
    if request.method=="GET":
        flag=0
        search=request.GET['search']
        s=search.split(' ')
        if len(s)>1:
            s1,s2=s[0],s[1]
        else:
            s1,s2=search,search
        print(s1,s2)
        users=extUser.objects.filter(Q(user__first_name__icontains=search) | Q(user__last_name__icontains=search) | Q(user__first_name__icontains=s1) | Q(user__last_name__icontains=s2) | Q(user__first_name__icontains=s2) | Q(user__last_name__icontains=s1)).exclude(user__id=request.user.id)
        params={'flag':flag,'eusers':users}
        return render(request,'chats/chat.html',params)