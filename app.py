import openai

openai.api_key = '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'


text = input("What text you like to generate a flashcarrd for")
num_flashcards = input("How many flashcards do you want to generate? ")


conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': f'create {num_flashcards} concise flashcards to demonstrate my understanding of the following text: {text}. Name the flashcards Front and Back and number them.'}
]

try:
    # Make the API request to ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=200
    )

    assistant_response = response.choices[0].message['content']

    print("Assistant:", assistant_response)

except Exception as e:
    print("An error occurred:", str(e))
