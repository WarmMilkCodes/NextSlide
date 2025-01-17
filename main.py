import json
import speech_recognition as sr
import pyautogui
from googletrans import Translator

# Load configuration from JSON file
def load_config(config_file="config.json"):
    try:
        with open(config_file, "r") as file:
            config = json.load(file)
        print("Configuration loaded successfully.")
        return config
    except FileNotFoundError:
        print("Configuration file not found. Using default settings.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}

# Listen for voice commands
def listen_for_command(sensitivity):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=sensitivity)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower().strip()  # Normalize command
            print(f"Recognized command: '{command}'")
            return command
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return ""

# Translate voice commands
translator = Translator()

def translate_to_english(command):
    try:
        translated = translator.translate(command, src="auto", dest="en").text.lower()
        print(f"Translated command: '{translated.text}'")
        return translated.text.lower().strip()
    except Exception as e:
        print(f"Translation error: {e}")
        return command.lower().strip()

# Perform actions based on the recognized command and configuration
def perform_action(command, config):
    actions = config.get("commands", {})
    for key, value in actions.items():
        normalized_key = key.lower().strip()  # Normalize JSON keys
        if normalized_key in command and value.get("enabled", False):
            action = value.get("action")
            if action == "key_press":
                key_to_press = value.get("key")
                print(f"Simulating key press: {key_to_press}")
                pyautogui.press(key_to_press)
            elif action == "mouse_click":
                button = value.get("button", "left")
                print(f"Simulating mouse click: {button} button")
                pyautogui.click(button=button)
            return
    print("Command not recognized or disabled. Waiting for a valid command...")

if __name__ == "__main__":
    config = load_config()
    print("Loaded Commands:")
    for cmd, details in config.get("commands", {}).items():
        print(f" - {cmd}: Enabled={details.get('enabled', False)}")

    # Get microphone sensitivity from config
    sensitivity = config.get("microphone_sensitivity", 0.5)

    while True:
        # Listen and process commands
        raw_command = listen_for_command(sensitivity)
        if raw_command:
            # Translate to English
            translated_command = translate_to_english(raw_command)
            # Perform action based on command
            perform_action(translated_command, config)
