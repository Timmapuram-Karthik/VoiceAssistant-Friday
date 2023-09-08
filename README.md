# Voice Assistant - Friday

## Overview
Voice Assistant - Friday is a Python-based voice-activated virtual assistant capable of performing various tasks. It can answer questions, provide weather information, open websites, and much more, all through voice commands.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up API Keys](#setting-up-api-keys)
- [Usage](#usage)
- [Voice Commands](#voice-commands)
- [Features](#features)

## Getting Started

### Prerequisites
Before you get started, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- An internet connection for certain features.

### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/VoiceAssistant-Friday.git
   ```

2. Navigate to the project directory:
   ```bash
   cd VoiceAssistant-Friday
   ```

3. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Setting Up API Keys
Some features of Voice Assistant require API keys. You can obtain these keys from the following sources:

- **Weather API Key:** You need an API key from [WeatherAPI](https://www.weatherapi.com/) to access weather information. Once you have the key, add it to the `key.py` file.

- **News API Key:** To fetch the latest news, you'll need an API key from [NewsAPI](https://newsapi.org/). Insert this key into the `key.py` file as well.
  
- **Jokes API Key:** To fetch jokes, you'll need an API key from [JokesAPI](https://api-ninjas.com/api/jokes) Insert this key into the `key.py` file as well.

- **OpenAI API Key:** To fecth chatgpt queries, you'll need an API key from [OpenAIAPI](https://platform.openai.com/) Insert this key into the `key.py` file as well.

### Usage

#### Voice Commands
To use Voice Assistant - Friday, follow these steps:

1. Run the voice assistant script:
   ```bash
   python Friday.py
   ```

2. Greet Friday with "Hello, Friday."

3. Issue voice commands, e.g., "What's the weather like today?" or "Open Wikipedia."

4. Friday will respond to your commands and carry out tasks accordingly.

## Features
- Ask questions and get answers.
- Check the current weather conditions.
- Read out the latest news headlines.
- Perform web searches.
- Open websites and applications.
- Engage in general chat with Friday.
- Write documents using OpenAI's GPT-3.

```

This README provides instructions for setting up and using your Voice Assistant project, including information about obtaining API keys and how to run the assistant.
