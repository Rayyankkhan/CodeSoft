# List of responses and their corresponding input from the user
responses = {
    'hello': 'Hello! How can I help you today?',
    'bye': 'Goodbye! Have a great day!',
    'how are you?': 'I\'m a bot, so I\'m doing great!',
    'I am having trouble with my account.': 'I\'m sorry to hear that. I\'ll do my best to help. Could you please provide more details about the issue?',
    'I have a Problem': 'I\'m sorry to hear that. I\'ll do my best to help. Could you please provide more details about the issue?',
    
    'What\'s the best framework for responsive websites?': 'Depends on needs. Options: [list]. Project specifics?',

'How can I optimize my website for SEO?': 'Focus on [best practices]. Need help in a specific area?',

'Connect web app to database?': 'Use [connector]. Securely handle credentials. Need more guidance?',

'My website is slow. How to optimize?': 'Optimize images, use caching, minimize HTTP requests. More specifics?',

'Secure web app from threats?': 'Input validation, HTTPS, updates. Specifics?'

}

# Get the user's message
user_message = input("You: ").lower()

# Check if the user's input matches any of the responses
for response, chatbot_response in responses.items():
    if user_message == response:
        print("Chatbot:", chatbot_response)
        break
else:
    print("Chatbot: Sorry, I didn't understand that. Can you please provide more information?")