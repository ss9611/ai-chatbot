import os
import openai

# Retrieve the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to interact with the chatbot
def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Main loop for chat interaction
if __name__ == "__main__":
    print("Welcome to the AI Chatbot. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        bot_response = chatbot(user_input)
        print(f"Bot: {bot_response}")
