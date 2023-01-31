import openai

conversation_context = {}

def askGPT(text, context):
    openai.api_key = ""
    context_str = ''
    for key, value in context.items():
        context_str += key + ' ' + value + '\n'
    prompt = text + '\n' + context_str
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

def main():
    print('GPT: Hello! How can I assist you today?\n')
    while True:
        myQn = input('You: ')
        if myQn.lower() == 'bye':
            print('GPT: Goodbye! Have a great day!')
            break
        else:
            response = askGPT(myQn, conversation_context)
            conversation_context.update({myQn:response})
            print('GPT: ' + response + '\n')

main()
