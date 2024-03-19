import openai

openai.api_key = ''
openai.api_version = '2023-03-15-preview'
openai.api_type = 'azure'
openai.api_base = 'https://api.openai.com/v1'
openai.api_base = 'https://lge-chatgpt-001.openai.azure.com/' #'openai/deployments/TextEmbedding/embeddings

response = openai.ChatCompletion.create(
  engine="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
