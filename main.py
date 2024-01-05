### Notes ###
# Using Ollama local endpoint and performing experiments

import asyncio
import requests
import json

api_endpoint = "http://localhost:11434/api/generate" 

headers = {
    "Content-Type" : "application/json"
}

# data = {
#     "model" : "tinyllama",
#     "prompt" : "What is the meaning of life?"
# }

# response = requests.post(api_endpoint, headers= headers, data= json.dumps(data))

# Getting text output from the API request
def get_str_response(response):
    """
    Generates a string response from the given HTTP response object.

    Parameters:
        response (HttpResponse): The HTTP response object.

    Returns:
        str: The generated string response.
    """
    response_str = response.content.decode('utf-8')
    json_strs = response_str.split("\n")
    message = ""
    for json_str in json_strs:
        if json_str:
            json_obj = json.loads(json_str)
            message += json_obj['response']
    return message

# text_output = get_str_response(response)
# print(text_output)

# Running a prompt on the API
def run_prompt(prompt, model = "dolphin-phi", json_mode = False):

    if not json_mode:
        data = {
            "model" : model,
            "prompt" : prompt
        }
        response = requests.post(api_endpoint, headers= headers, data= json.dumps(data))
        output = get_str_response(response)
    else:
        data = {
            "model" : model,
            "prompt" : prompt,
            "format" : "json"
        }
        response = requests.post(api_endpoint, headers= headers, data= json.dumps(data))
        output = json.loads(get_str_response(response))
    return output

# text_output = run_prompt("How old is too old?")
# text_output = run_prompt("What is the meaning of life?")
# print(text_output)

# Creating a class for PromptTemplate
class PromptTemplate:
    def __init__(self, input_variables, template):
        self.input_variables = input_variables
        self.template = template

    def format(self, **kwargs):
        return self.template.format(**kwargs)

new_template = PromptTemplate(input_variables=['question'], template = "You are Rick from Rick and Morty. Please answer the following {question}")

# Create a story using a PromptTemplate
def generate_story(topic, model = "dolphin-phi"):
    story_template = PromptTemplate(input_variables=['topic'], template = "You are Rick from Rick and Morty. Create a story on the following topic: {topic}")
    prompt = story_template.format(topic=topic)
    print(prompt)
    data = {
        "model" : model,
        "prompt" : prompt
    }

    response = requests.post(api_endpoint, headers= headers, data= json.dumps(data))
    message = get_str_response(response)
    return message

# text_output = generate_story(topic = "Mount Everest")
# print(text_output)


# Generate a history lesson
def tell_history(topic, model = "dolphin-phi"):
    template = """
    You are Yuval Noah Harari, a historian famous for his storytelling. 
    Create a brief history overview on the following topic: 
    {topic}
    """
    history_template = PromptTemplate(input_variables=['topic'], template = template)
    prompt = history_template.format(topic=topic)
    print(prompt)
    data = {
        "model" : model,
        "prompt" : prompt
    }

    response = requests.post(api_endpoint, headers= headers, data= json.dumps(data))
    message = get_str_response(response)
    return message

# text_output = tell_history(topic = "Why wars happen?")
# print(text_output)


# Word-Building game
def build_word(myword):
    last_letter = myword[-1]
    build_word_template = """
    Give me a word that starts with '{last_letter}'. 
    Just give the word and nothing else.
    """
    build_word_template = PromptTemplate(input_variables=['last_letter'], template = build_word_template)
    build_word_prompt = build_word_template.format(last_letter=last_letter)
    output = run_prompt(prompt = build_word_prompt, json_mode= True)
    return output['word']

# print(build_word("Lattice"))

# def word_building_game():
#     print("Welcome to the Word Building Game!")
#     print("You will be given a word. Your task is to come up with a new word that starts with the last letter of the given word.")
#     print("Let's start!")

#     while True:
#         word = input("Enter a word: ")
#         last_letter = word[-1]
#         print(f"The last letter is: {last_letter}")

#         user_word = input("Your turn. Enter a word that starts with the last letter: ")
#         if user_word[0].lower() != last_letter.lower():
#             print("Your word does not start with the last letter. You lose!")
#             break

#         computer_word = build_word(word)
#         print(f"Computer's turn. Computer's word is: {computer_word}")
#         if computer_word[0].lower() != last_letter.lower():
#             print("Computer's word does not start with the last letter. You win!")
#             break

#         print("Next round!")


# async def word_building_game(num_rounds):
#     word= "lattice"
#     for i in range(num_rounds):
#         new_word = input(f"Add a word starting with {word[-1]}: ")
#         word = await build_word(new_word)
#         print(f"Computer's turn: {word}")
        
#         new_word = await build_word(word) 
#         print(f"Your turn: {new_word}")
        
#     print("Game over!")

# async def main():
#     await word_building_game(5)

# asyncio.run(main())


def word_building_game():
    recent_word = ""
    word_list = []
    while True:
        user_word = input("Enter a word: ")
        recent_word = user_word
        word_list.append({"user": "recent_word"})
        


# Creating classes for ChatMessage and ChatHistory
class ChatMessage:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def __str__(self):
        return f"{self.role}: {self.content}"
    

class ChatHistory:
    def __init__(self):
        self.messages = []

    def add_ai_message(self, content):
        message = ChatMessage(role = "assistant", content = content)
        self.messages.append(message)

    def add_user_message(self, content):
        message = ChatMessage(role = "user", content = content)
        self.messages.append(message)


# message = ChatMessage(role = "system", content = "You are Rick from Rick and Morty.")
# print(message)
