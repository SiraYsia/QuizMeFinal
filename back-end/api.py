import openai
import os
openai.api_key = os.environ['OPENAI_API_KEY']

text = input("What text you like to generate a flashcarrd for")
num_flashcards = input("How many flashcards do you want to generate? ")


conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': f'create {num_flashcards} concise flashcards to demonstrate my understanding of the following text: {text}. Name the flashcards Front and Back and number them. The front should always be the question and the back should be the answer. The front should always be in question format.'}
]

try:
    # Make the API request to ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=500
    )

    assistant_response = response.choices[0].message['content']

    print("Assistant:", assistant_response)

except Exception as e:
    print("An error occurred:", str(e))
