from django.core.exceptions import ValidationError

def validate_png(img):
    if not img.name.lower().endswith('.png'):
        raise ValidationError('Imagem precisa ser PNG')