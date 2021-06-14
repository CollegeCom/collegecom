from django.shortcuts import render, HttpResponse, redirect
from chat.models import  Friends, Messages
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSerializer
from django.contrib.auth.models import User

def getUserId(username):
    """
    Get the user id by the username
    :param username:
    :return: int
    """
    use = User.objects.get(username=username)
    id = use.id
    return id

def chat(request,username):
    """
    Get the chat between two users.
    :param request:
    :param username:
    :return:
    """
    users=User.objects.all()
    friend = User.objects.get(username=username)
    id = getUserId(request.user.username)
    curr_user = User.objects.get(id=id)
    # print(curr_user,friend)
    messages = Messages.objects.filter(sender_name=id, receiver_name=friend.id) | Messages.objects.filter(sender_name=friend.id, receiver_name=id)
    for i in messages:
        print(i.sender_name,i.receiver_name)
    if request.method == "GET":
        return render(request, "chats/chat.html",
                      {'messages': messages,
                       'curr_user': curr_user, 'friend': friend,'users':users})

@csrf_exempt
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

def chathome(request):
    users=User.objects.all()
    params={'users':users}
    return render(request,'chats/chat.html',params)