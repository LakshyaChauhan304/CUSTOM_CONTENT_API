from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeadingBlock(blocks.StructBlock):
    heading_text = blocks.CharBlock(classname="title")
    size = blocks.ChoiceBlock(choices=[
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "CONTENT_APP/blocks/heading_block.html"

class ParagraphBlock(blocks.StructBlock):
    text = blocks.RichTextBlock()

    class Meta:
        icon = "pilcrow"
        template = "CONTENT_APP/blocks/paragraph_block.html"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "CONTENT_APP/blocks/image_block.html"

class CtaBlock(blocks.StructBlock):
    text = blocks.CharBlock()
    button_text = blocks.CharBlock()
    button_link = blocks.URLBlock()

    class Meta:
        icon = "plus"
        template = "CONTENT_APP/blocks/cta_block.html"
