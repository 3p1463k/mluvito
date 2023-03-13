import os

from google.cloud import texttospeech

from core.config import settings


def syntesize_userinput(userinput: str):

    # GOOGLE_APPLICATION_CREDENTIALS=settings.GOOGLE_APPLICATION_CREDENTIALS
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "static/mluvijo-0ad4cf2ab5c4.json"

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=userinput)

    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="cs-CZ",
        name="cs-CZ-Standard-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("static/mp3/output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    #
    # raise exceptions.DefaultCredentialsError(
    # google.auth.exceptions.DefaultCredentialsError: File djdcklLHLKUGDKJ;l4vd5f4 was not found.
