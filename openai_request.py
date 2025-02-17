from openai import OpenAI
import user_config #this is the main code for the open ai chat gpt functionality

client = OpenAI(api_key=user_config.api_key)

# For single-turn interactions
def send_request(query): 
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": query    
            }
        ]
    )
    return completion.choices[0].message.content

# For multi-turn interactions (chat history)
def send_request2(query):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=query
    )
    return completion.choices[0].message.content