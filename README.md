# Virtual Humanoid Assistant

This project is a Virtual Humanoid Assistant that can understand voice inputs, generate text responses using the Llama-2 language model, convert the text responses to speech, and generate a video with lip-sync animation using the Wav2Lip repository.

## Sample Output:

https://github.com/Dharinesh/Virtual-Assistant/assets/108059896/0639e96e-d718-48ee-baa5-197de74d3d4e

### Disclaimer: This Picture of the Personality is used only for Educational Purposes and not intended for misuse

## Features

- Voice input recognition
- Text-to-speech conversion
- Response generation using the Llama-2 language model
- Video generation with lip-sync animation using Wav2Lip

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python 3.x
- Required Python packages (specified in the `requirements.txt` file)
- Llama-2 model (download and place it in the `models` directory)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Dharinesh/virtual-humanoid-assistant.git
```

2. Navigate to the project directory:

```bash
cd virtual-humanoid-assistant
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Download the Llama-2 model and place it in the models directory.

## Usage

1. Run the app.py script to start the Virtual Humanoid Assistant:

```bash
python app.py
```

2. Speak your question when prompted.

3. The assistant will generate a text response using the Llama-2 model, convert it to speech, and save the audio as a WAV file in the responses directory.

4.  The virtual_assistant.ipynb file will use the Wav2Lip repository to generate a video with lip-sync animation based on the audio response and a custom image.

5.  The final video will be saved, and a preview will be displayed.

## License 

This project is licensed under the GNU License.

## Acknowledgments

-> Llama-2 - The language model used for generating text responses.

-> Wav2Lip - The repository used for generating lip-sync animation videos.
