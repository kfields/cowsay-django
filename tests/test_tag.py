from django.template import Context, Template


def test_cowsayer_tag() -> None:
    context = Context({"char": "cow", "text": "Hello from Cowsay!"})
    template_to_render = Template("{% load cowsay_tags %}" "{% cowsays char text %}")
    rendered: str = template_to_render.render(context)

    # Check if the output is what you expect
    assert "Hello" in rendered
