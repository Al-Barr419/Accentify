from transformers import pipeline

# Load the Whisper model
model_name = "openai/whisper-base"
pipe = pipeline(model=model_name, task="automatic-speech-recognition")

result = pipe("archive (4)/recordings/recordings/yoruba1.mp3")
print(result["text"])

