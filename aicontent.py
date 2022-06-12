import os
import openai 
import config 
openai.api_key = config.OPENAI_API_KEY

def productDescription(query):
    response = openai.Completion.create(
        model="davinci-instruct-beta-v3",
        prompt="Generate a detailed Product Description for: {}".format(query),
        temperature=0.5,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'You beat the AI!'
    else:
        answer = 'You beat the AI!'
    
    return answer
    
#     print()

# query = 'Mango'
# productDescription(query)