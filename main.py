import openai

api_key = 'API_KEY'
openai.api_key = api_key

def ask_openai(question, model="gpt-3.5-turbo-1106", max_tokens=50):
    response = openai.Completion.create(
        engine=model,
        prompt=question,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def chat():
    print("Welcome to the OpenAI Chatbot! You can start chatting. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ") 
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = ask_openai(user_input)
        print("OpenAI Bot:", response)

if __name__ == "__main__":
    chat()

