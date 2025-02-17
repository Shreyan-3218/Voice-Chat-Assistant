import pyttsx3       # This is the TTS library used for Python
import speech_recognition as sr  # This is the STT library used for Python
import random #this is for rand function
import webbrowser #this is for opening the webbrowser
import datetime #this is for date and time
from plyer import notification # this is for the notification function
import pyautogui
from datetime import datetime
import wikipedia # this is for wiki
import pywhatkit #this is for whatsapp
import user_config # this is the file which contains the api key
import openai_request as ai # this is the openai file 
import time
import mtranslate

engine = pyttsx3.init()
voices = engine.getProperty('voices')       # Getting details of current voice
#engine.setProperty('voice', voices[0].id)  # Changing index, changes voices. 0 for male
#engine.setProperty('voice', voices[4].id)  # Changing index, changes voices. 4 for female hindi
engine.setProperty('voice', voices[2].id)   # Changing index, changes voices. 1 for female
engine.setProperty('rate', 170)   # This will control the speed of the text to speech

def speak(command):       # This is a function for the TTS with parameters command this command will be spoken
    
    engine.say(command)
    engine.runAndWait()

def command():    # This is a function for the STT with parameters command this command will be listened
    content = ""  # This is done so if nothing is said then the loop will keep on running without error
    while content == "":
        r = sr.Recognizer()  # Obtain audio from the microphone
        with sr.Microphone() as source:
            print("What is your Command")
            audio = r.listen(source)

            # Recognize speech using Google Speech Recognition
            try:
                content = r.recognize_google(audio, language='en-IN')
                print("Thinking ...." )
                print("Your Command is: " + content)
              #  content = mtranslate.translate(content,to_language ="en-in")  #uncomment for translation
               # print("Thinking ....")
               # print("Your Command is: " + content)
                return content.lower()  # Ensure the command is in lowercase
            except Exception as e:
                print("Can you please repeat that sir...")
                print(f"Error: {e}")  # Print the error for debugging

def read_tasks():  # This function reads tasks from the todo.txt file
    try:
        with open("todo.txt", "r") as file:
            tasks = file.read()
            return tasks if tasks else "No tasks found."  # Return tasks or a default message
    except FileNotFoundError:
        return "No tasks found."  # Handle case where the file doesn't exist

def main():
    chat_assistant = [] 
    while True:
        request = command()
        print(f"Recognized Command: '{request}'")  # Print the recognized command with quotes for clarity

        # Initialize a flag to check if any command was matched
        command_matched = False

        if request == "hello":
            speak("Hello, How can I assist you today?")
            command_matched = True
        
        
        elif request == "play music": 
            speak("Playing music")
            song = random.randint(1, 5) #this is the random function
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=pRpeEdMmmQ0")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=PBwAxmrE194")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=AiwvPmRTv6M")
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=CSvFpBOe8eY") 
            elif song == 5:
                webbrowser.open("https://www.youtube.com/watch?v=XFkzRNyygfk")        
            command_matched = True
      
      
        elif request == "tell time":
            now_time = datetime.now().strftime("%H:%M") #this is the time function
            speak("The current time is " + str(now_time))
            command_matched = True
       
        elif request == "tell date":
            now_time = datetime.now().strftime("%d:%m") #this is the date function
            speak("The current date is " + str(now_time))    
            command_matched = True
       
       
       
        elif request.startswith("add task"):
            task = request.replace("add task", "").strip() #here we will replace add task with the task that is said in the todo.txt file
            if task != "":
                speak("Task added: " + task)
                try:
                    with open("todo.txt", "a") as file:
                        file.write(task + "\n")  # Append the task to the file
                except Exception as e:
                    speak("Failed to add task.")  # Handle file access errors
                    print(f"Error: {e}")
            command_matched = True
       
        elif "what are today's task" in request or "what are today's tasks" in request:
            tasks = read_tasks()  # Read tasks from the file
            speak("Today's objectives are: " + tasks)
            command_matched = True
       
        elif "show me today's task" in request or "show today's tasks" in request:
            tasks = read_tasks()  # Read tasks from the file
            if tasks != "No tasks found.":
                notification.notify(
                    title="Today's work",
                    message=tasks
                )
            else:
                speak("No tasks found.")
            command_matched = True
       
        elif "open" in request:
            query = request.replace("open", "")  # The command open will be replaced by your command
            pyautogui.press("super")  # This command will press the window key
            pyautogui.typewrite(query)  # This will type the query that is said in the windows menu
            pyautogui.sleep(2)  # This is the time it will pause for before closing the window
            pyautogui.press("enter")  # This will press enter after typing the name
            command_matched = True
       
       
        elif "take screenshot" in request:
            timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")  # This will create a timestamp which is imported from datetime library.
            filename = f'my_screenshot_{timestamp}.png'  # This will create a filename with the timestamp
            im1 = pyautogui.screenshot()  # This is the main screenshot function
            im1.save(filename)  # This will save the file 
            command_matched = True
       
       
        elif "search wikipedia" in request:
            query = request.replace("search wikipedia", "") #this is will replace the command with search wiki
            print(query)
            result = wikipedia.summary(query, sentences=2)
            print(result)   
            speak(result)
            command_matched = True
        
        
        
        elif "search google" in request:
            query = request.replace("search google", "")
            speak("Searching Google for " + query)  # This is the query that we will ask
            webbrowser.open("https://www.google.com/search?q=" + query)  # This is the URL for any Google search; we will add our query to it
            command_matched = True
        
        
        elif "send whatsapp" in request:
            pywhatkit.sendwhatmsg("+918218270158", "Hello, how are you?", 16, 53, 30)  # This is the number, message, and time (hours, minutes, seconds)
          #this is a very barebones version of sending whatsapp msg because in order to make it dynamic where it searches your contact list we would need whatsapp api which is not publicly available
            command_matched = True
        
        
        elif "ask ai" in request:
             request = request.replace("ask ai", "").strip()  # Clean up the request
             response = ai.send_request(request)  # Get the AI's response
             print(response)  # Print the response
             speak(response)  # Speak the response
             command_matched = True

        # Check if no command was matched
        if not command_matched:
            # Add the user's request to the chat history
            chat_assistant.append({"role": "user", "content": request})
            print(chat_assistant)
            # Send the chat history to the AI
            response = ai.send_request2(chat_assistant)  # Call the multi-turn function
            print(response)
            speak(response)
            # Append the AI's response to the chat history
            chat_assistant.append({"role": "assistant", "content": response})
        
if __name__ == "__main__":
    main()  # Call the main function