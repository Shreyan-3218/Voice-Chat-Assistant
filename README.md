# Voice_Chat-assistant
This is a simple voice assistant using Python libraries which takes commands through microphone and executes them 
Available Voice Commands :

Basic Commands
"Hello"
The assistant will greet you with a "Hello, How can I assist you today?" message.

"Play music"
The assistant will play a random song from a predefined list of YouTube links.

"Tell time"
The assistant will tell you the current time.

"Tell date"
The assistant will tell you the current date.

Task Management
"Add task [task description]"
Adds a task to the todo.txt file. For example, "Add task Buy groceries" will add "Buy groceries" to your task list.

"What are today's tasks"
The assistant will read out the tasks listed in the todo.txt file.

"Show me today's tasks"
The assistant will display a notification with the tasks listed in the todo.txt file.

Web Browsing
"Open [application name]"
Opens the specified application on your computer. For example, "Open Chrome" will open the Chrome browser.

"Search Google [query]"
Searches Google for the specified query. For example, "Search Google Python programming" will open a Google search for "Python programming".

"Search Wikipedia [query]"
Searches Wikipedia for the specified query and reads out a summary. For example, "Search Wikipedia Python programming" will provide a summary of Python programming from Wikipedia.

Screenshot
"Take screenshot"
Takes a screenshot and saves it with a timestamped filename.
WhatsApp Messaging

"Send WhatsApp"
Sends a predefined WhatsApp message to a specified number. (Note: This is a basic implementation and requires manual setup.)
AI Interaction

"Ask AI [your question]"
Sends your question to the OpenAI API and reads out the response. For example, "Ask AI What is the capital of France?" will return "The capital of France is Paris."

Multi-turn Conversation
If the assistant does not recognize a specific command, it will treat the input as a conversational query and respond using the OpenAI API. This allows for multi-turn conversations.
Configuration

Voice Settings:
You can change the voice and speech rate in the main.py file by modifying the engine.setProperty lines.

API Keys:
Ensure that your API keys are correctly set in the user_config.py file.

Contributing
Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions, please open an issue.
