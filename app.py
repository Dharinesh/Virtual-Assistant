import speech_recognition as sr
import pyttsx3
import os
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Initialize the speech recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Ensure the model path and name are correct
llm = CTransformers(
    model='models/llama-2-7b-chat.Q8_0.gguf',
    model_type='llama',
    config={'max_new_tokens': 512}
)

template = """You are a helpful assistant. Answer the following question in a clear and concise manner.

Question: {question} Assistant: """

# Create a prompt template instance
prompt = PromptTemplate(
    input_variables=["question"],
    template=template
)

# Function to capture voice input and convert it to text
def get_voice_input():
    with sr.Microphone() as source:
        print("Speak your question:")
        audio = r.listen(source)
    try:
        question = r.recognize_google(audio)
        print(f"You asked: {question}")
        return question
    except sr.UnknownValueError:
        print("Sorry, I could not understand your question.")
    except sr.RequestError as e:
        print("Could not request results from the speech recognition service; {0}".format(e))
    return None

# Function to convert text to speech and save the audio
def save_response_audio(text, output_path):
    wav_file = output_path + ".wav"
    engine.save_to_file(text, wav_file)
    engine.runAndWait()

# Function to speak the response
def speak_response(text):
    engine.say(text)
    engine.runAndWait()

# Create the "responses" directory if it doesn't exist
responses_dir = "responses"
if not os.path.exists(responses_dir):
    os.makedirs(responses_dir)

# Get voice input for the question
question = get_voice_input()

if question:
    # Format the prompt with the question
    formatted_prompt = prompt.format(question=question)

    # Generate a response using the Llama-2 model
    response = llm.invoke(formatted_prompt)

    print(f"Assistant: {response}")

    # Save the response as an audio file in the "responses" folder
    output_path = os.path.join(responses_dir, f"input_audio")
    save_response_audio(response, output_path)
    print(f"Response audio saved to {output_path}.wav")

    # Speak the response using text-to-speech
    speak_response(response)