import os

from django import template
from django.conf import settings

from clock.renderer import create_clock

register = template.Library()

@register.filter
def clock_url(timestamp, width):
    rel_image_dir = 'managed/clock/%s/%s/' % (
        timestamp.strftime('%Y-%B').lower(),
        timestamp.strftime('%d'),
        )
    image_filename = '%s-w%s.png' % (
        timestamp.strftime('%H-%M'),
        width
        )
    image_dir_on_disk = '%s%s' % (settings.MEDIA_ROOT, rel_image_dir)
    image_path_on_disk = '%s%s' % (image_dir_on_disk, image_filename)
    if not os.path.exists(image_path_on_disk):
        image = create_clock(timestamp, int(width) / 2, 7)
        if not os.path.exists(image_dir_on_disk):
            os.makedirs(image_dir_on_disk)
        image.save(image_path_on_disk)
    return '%s%s%s' % (settings.MEDIA_URL, rel_image_dir, image_filename)