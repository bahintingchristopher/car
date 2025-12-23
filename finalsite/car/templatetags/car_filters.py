from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

@register.filter
def smart_image_url(image_field):
    """
    Handles ImageField (new uploads) and string paths (old static files).
    """
    default_image = static('car/images/no-image.webp')

    # Case 1: The ImageField is completely empty/null
    if not image_field:
        return default_image

    # Case 2: The field is a string (must be an old path)
    if isinstance(image_field, str):
        # Check if the string actually has content
        if image_field.strip():
            # Assume old paths are relative to the static folder, e.g., 'car/images/mustang.jpg'
            # The static() function prepends the STATIC_URL (/static/)
            return static(image_field)
        return default_image

    # Case 3: The field is a valid ImageFieldFile object (new upload)
    try:
        # Check if the ImageField object has a file path attached (i.e., not a blank file object)
        if hasattr(image_field, 'name') and image_field.name:
            return image_field.url
    except Exception:
        # Fallback for any error during file object access
        pass

    # Final fallback
    return default_image