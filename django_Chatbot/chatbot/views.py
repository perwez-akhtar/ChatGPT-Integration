from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key='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'
openai.api_key=openai_api_key

def askgpt(message):
    response=openai.Completion.create(
        model="gpt-3.5-turbo-0125",
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    # print(response)
    answer=response.choices[0].text.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response =askgpt(message)
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chatbot.html')