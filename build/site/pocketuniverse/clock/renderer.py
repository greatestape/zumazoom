import math

from PIL import Image, ImageDraw

from clock.clockwork import get_amount_of_sun

NIGHT_SUN_COLOUR = (35, 79, 153)
DAY_SUN_COLOUR = (255, 255, 0)
TWILIGHT_SUN_COLOUR = (255, 0, 0)

def create_clock(timestamp, radius, thickness):
    double_radius = radius * 2
    image = Image.new("RGBA", (double_radius * 2, double_radius * 2), color="#FFFFFF")
    draw = ImageDraw.Draw(image)
    draw_clock_image(image, draw, timestamp, double_radius, thickness)
    draw_sun_image(image, draw, timestamp, double_radius, thickness)
    del draw
    return image.resize((radius * 2, radius * 2), Image.ANTIALIAS)


def draw_clock_image(draw, timestamp, radius, hand_width):
    hour_hand_length = radius * 0.5
    minute_hand_length = radius * 0.75

    minute_angle = -2 * math.pi * (timestamp.minute / 60.0) + (math.pi / 2.0)
    hour_angle = -2 * math.pi * (timestamp.hour % 12 / 12.0) - (timestamp.minute / 720.0) + (math.pi / 2.0)

    hour_hand = translate_polygon(rotate_polygon(make_clock_hand(hand_width, hour_hand_length, (radius, radius)), -hour_angle), radius, radius)
    minute_hand = translate_polygon(rotate_polygon(make_clock_hand(hand_width, minute_hand_length, (radius, radius)), -minute_angle), radius, radius)

    draw.polygon(hour_hand, fill="#4C4C4C")
    draw.polygon(minute_hand, fill="#4C4C4C")


def draw_sun_image(draw, timestamp, arc_radius, sun_radius):
    sun_angle = -2 * math.pi * (timestamp.hour / 24.0) - (math.pi / 2.0)

    sun_x = arc_radius + math.cos(sun_angle) * (arc_radius - sun_radius)
    sun_y = arc_radius - math.sin(sun_angle) * (arc_radius - sun_radius)
    bounding_box = [(sun_x - sun_radius, sun_y - sun_radius), (sun_x + sun_radius, sun_y + sun_radius)]
    sun_colour = get_sun_colour(timestamp)
    draw.ellipse(bounding_box, fill='rgb(%s,%s,%s)' % sun_colour)


def get_sun_colour(timestamp):
    sunnyness = get_amount_of_sun(timestamp)
    if sunnyness == 0.0:
        return NIGHT_SUN_COLOUR
    else:
        return blend_colours(DAY_SUN_COLOUR, TWILIGHT_SUN_COLOUR, sunnyness)


def blend_colours(c1, c2, mix):
    c3 = []
    mix = float(mix)
    for x in range(3):
        if c1[x] < c2[x]:
            diff = c2[x] - c1[x]
            c3.append(c1[x] + diff * mix)
        else:
            diff = c1[x] - c2[x]
            c3.append(int(c2[x] + diff * mix))
    return tuple(c3)


def rotate_polygon(poly, angle):
    cos = math.cos(angle)
    sin = math.sin(angle)
    rotated_poly = []
    for i in range(len(poly)):
        rotated_poly.append((poly[i][0] * cos - poly[i][1] * sin,
                             poly[i][0] * sin + poly[i][1] * cos))
    return rotated_poly


def translate_polygon(poly, x, y):
    translated_poly = []
    for i in range(len(poly)):
        translated_poly.append((poly[i][0] + x, poly[i][1] + y))
    return translated_poly


def make_clock_hand(width, length, centre):
    return [((-width / 2.0), (width / 2.0)),
            ((-width / 2.0), (-width / 2.0)),
            (length, -(width / 2.0)),
            (length, (width / 2.0))]
