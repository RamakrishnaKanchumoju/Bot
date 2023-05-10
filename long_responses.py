import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_FONT = "Type of fontr you need in your script!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?",
                "I have a suggestion to work on it"][
        random.randrange(4)]
    return response