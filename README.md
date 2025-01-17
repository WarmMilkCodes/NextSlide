# Next Slide Automation App

A Python-based voice command application that listens for specific phrases such as "Next Slide", "Previous Slide", "Click Mouse" and performs predefined actions. Users can customize and enable/disable commands using the JSON configuration file.

## Features

- Voice recognition powered by the ```speech_recognition``` library
- Simulate mouse clicks or keyboard actions with ```pyautogui```
- Fully customizable commands via ```config.json```
- Activate or deactivate commands using a simple ```enabled``` flag in the configuration file
- Adjustable microphone sensitivity

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/WarmMilkCodes/NextSlide.git
    cd NextSlide

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Ensure you have a working microphone connected to your computer.

## Configuration
Customize the ```config.json``` file to define and manage commands.
Example:
```
    {
    "commands": {
        "next slide": {
            "enabled": true,
            "action": "key_press",
            "key": "right"
        },
        "previous slide": {
            "enabled": false,
            "action": "key_press",
            "key": "left"
        },
        "click mouse": {
            "enabled": true,
            "action": "mouse_click",
            "button": "left"
        }
    },
    "microphone_sensitivity": 0.5
    }
```

- ```enabled```: Toggle the command on/off (```true``` or ```false```)
- ```action```: Specify the type of action (```key_press``` or ```mouse_click```)
- ```key```: Key to simulate for ```key_press``` actions
- ```button```: Button to simulate for ```mouse_click``` actions (```left```, ```right```, or ```middle```)
- ```microphone_sensitivity```: Adjust for ambient noise (in seconds)

## Usage
1. Run the application:
    ```bash
    python main.py

2. Speak your commands into the microphone

3. Actions will be performed based on the configuration in ```config.json```

**Example Commands**
- **"Next Slide"**: Simulates pressing the right arrow key
- **"Previous Slide"**: Simulates pressing the left arrow key
- **"Mouse Click"**: Simulates a *left* mouse click

## Requirements
- Python 3.7+
- Libraries:
    - ```speech_recognition```
    - ```pyautogui```
    - ```pyaudio```

- Install dependencies with:
    ```bash
    pip install -r requirements.txt

## Troubleshooting
- **Command not recognized or disabled**:
    - Check that the command exists in ```config.json``` and is ```enabled: true```
    - Ensure proper formatting and case matching in ```config.json```
- **Microphone not working**:
    - Test your microphone with another application
    - Adjust ```microphone_sensitivity``` in ```config.json```

## Contributing
Contributions are welcome. Feel free to submit a pull request or open an issue for bugs or feature requests.