# -*- coding: utf-8 -*-
import openai

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import secrets

openai.api_key = secrets.OPENAI_API_KEY

# Create your views here.
@api_view(['POST',])
def question(request):
    data = request.data
    job = data['job']
    essay = data['essay']

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": ("너는 {0}면접관이야. 자기소개서를 입력하면 예상질문을 5개 작성해줘"
                            .format(job + " 직무 분야의 " if job else ""))
            },
            { 
                "role": "user",
                "content": essay
            }
        ]
    )

    result = completion.choices[0].message.content

    return Response(result, status=status.HTTP_200_OK)