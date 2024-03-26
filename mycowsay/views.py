import cowsay
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET


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

@require_GET
@cache_control(max_age=60 * 60 * 24, immutable=True, public=True)  # one day
def favicon(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + '<text y=".9em" font-size="90">🐮</text>'
            + "</svg>"
        ),
        content_type="image/svg+xml",
    )