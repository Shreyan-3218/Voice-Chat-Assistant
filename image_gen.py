from openai import OpenAI
import user_config
client = OpenAI(api_key=user_config.api_key)

response = client.images.generate(
    model="dall-e-2",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)         #this is the code to generate the image but it requires u to have balance in your open ai account

print(response.data[0].url)