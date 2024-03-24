from django.shortcuts import render

import cowsay


def index(request):
    text = "Hello from cowsay!"
    character = "cow"
    if request.method == "POST":
        character = request.POST.get(
            "character", "cow"
        )  # Default to 'cow' if not specified
        # Extract the text input from the form
        text = request.POST.get("text", "")

    # Pass the message to the template, whether it's the default or from a POST request
    return render(
        request,
        "index.html",
        {
            "characters": cowsay.char_names,
            "character": character,
            "message": text,
            "selected_character": character,
            # Include the original text if you want to remember it as well
            "original_text": text,
        },
    )
