import openai
openai.api_key='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'
def get_completion(prompt,model='gpt-3.5-turbo'):
    messages=[{'role':'user','content':prompt}]
    response=openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        )
    return response.choices[0].message['content']
while True:
    prompt=input('sua pergunta: ')
    response=get_completion(prompt)
    print(response)
    