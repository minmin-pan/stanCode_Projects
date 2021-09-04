"""
File: my_drawing
Name: Tzu-MIn, Pan
----------------------
The program is used to draw Rilakkuma.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLabel
from campy.graphics.gwindow import GWindow

# global variable
window = GWindow(title='My Draw')


def main():
    """
    The program is used to draw Rilakkuma.
    """
    # background
    background = background_maker()

    # face
    face = face_maker()

    # eye
    eye_l = eye_maker()
    eye_r = eye_maker()

    # mouth
    mouth = mouth_maker()
    mouth_1 = GArc(60, 60, 290, 60)
    mouth_2 = GArc(60, 60, 190, 60)

    # nose
    nose = GOval(10, 10)
    nose.filled = True

    # ear
    ear_l = ear_maker()
    ear_r = ear_maker()
    ear_ll = ear2_maker()
    ear_rr = ear2_maker()

    # body
    body = body_maker()
    body2 = body2_maker()
    body3 = body3_maker()

    # label
    label = label_maker('Rilakkuma', 70)
    label2 = label_maker('Min', 10, font='Dialog')

    # arm
    arm_l = arm1_maker()
    arm_r = arm2_maker()

    # leg
    leg = leg_maker()
    leg2 = leg_maker()

    # show my draw
    window.add(background)
    window.add(leg, (window.width - leg.width) / 2 - body.width/3.7, (window.height - leg.height) / 2 + body.height*1.1)
    window.add(leg2, (window.width - leg2.width) / 2 + body.width / 3.7,
               (window.height - leg2.height) / 2 + body.height * 1.1)
    window.add(body, (window.width - body.width) / 2, (window.height - body.height) / 2 + face.height/1.4)
    window.add(body2, (window.width - body2.width) / 2,
               (window.height - body2.height) / 2 + face.height/1.4 + body.height/3.3)
    window.add(body3, (window.width - body3.width) / 2, (window.height - body3.height) / 2 + face.height/1.2)
    window.add(arm_l, (window.width - arm_l.width) / 2 - body.width / 2.9,
               (window.height - arm_l.height) / 2 + face.height / 1.5)
    window.add(arm_r, (window.width - arm_r.width) / 2 + body.width / 2.9,
               (window.height - arm_r.height) / 2 + face.height / 1.5)
    window.add(label, (window.width-label.width)/2, window.height/4)
    window.add(ear_l, (window.width - ear_l.width) / 2 - face.width / 2.25,
               (window.height - ear_l.height) / 2 - face.height / 3)
    window.add(ear_ll, (window.width - ear_ll.width) / 2 - face.width / 2.25,
               (window.height - ear_ll.height) / 2 - face.height / 3.5)
    window.add(ear_r, (window.width - ear_r.width) / 2 + face.width / 2.25,
               (window.height - ear_r.height) / 2 - face.height / 3)
    window.add(ear_rr, (window.width - ear_rr.width) / 2 + face.width / 2.25,
               (window.height - ear_rr.height) / 2 - face.height / 3.5)
    window.add(face, (window.width - face.width) / 2, (window.height - face.height) / 2)
    window.add(eye_l, (window.width - eye_l.width) / 2 - face.width / 5, (window.height - eye_l.height) / 2)
    window.add(eye_r, (window.width - eye_r.width) / 2 + face.width / 5, (window.height - eye_r.height) / 2)
    window.add(mouth, (window.width - mouth.width) / 2, (window.height - mouth.height) / 2 + face.height / 8)
    window.add(nose, (window.width - nose.width) / 2, (window.height - nose.height) / 2 + face.height / 12)
    window.add(mouth_1, (window.width - mouth_1.width) / 2 - face.width / 20,
               (window.height - mouth_1.height) / 2 + face.height / 11)
    window.add(mouth_2, (window.width - mouth_2.width) / 2 + face.width / 20,
               (window.height - mouth_2.height) / 2 + face.height / 11)
    window.add(label2, window.width-label2.width, window.height)

    # kuma2
    kuma2_color = '0xFFEEDD'
    face2 = face_maker(140, color=kuma2_color)

    eye2_l = eye_maker(size=15)
    eye2_r = eye_maker(size=15)

    mouth2 = mouth_maker(size=40)
    mouth2_1 = GArc(60, 60, 290, 60)
    mouth2_2 = GArc(60, 60, 190, 60)

    nose2 = GOval(8, 8)
    nose2.filled = True

    ear2_l = ear_maker(size=50, color=kuma2_color)
    ear2_r = ear_maker(size=50, color=kuma2_color)
    ear2_ll = ear2_maker(size=30, color='0xFFC1E0')
    ear2_rr = ear2_maker(size=30, color='0xFFC1E0')

    body_2 = body_maker(size=100, color=kuma2_color)
    body2_2 = body2_maker(size=85, color=kuma2_color)
    body3_2 = body3_maker(size=60)

    arm2_l = arm1_maker(size=40, color=kuma2_color)
    arm2_r = arm2_maker(size=40, color=kuma2_color)

    leg_2 = leg_maker(size=25, color=kuma2_color)
    leg2_2 = leg_maker(size=25, color=kuma2_color)

    buttons = GOval(15, 15)
    buttons.filled = True
    buttons.fill_color = 'red'

    window.add(leg_2, (window.width - leg_2.width) / 2 - face.width / 1.05 - body_2.width/3.3,
               (window.height - leg_2.height) / 2 + face.height / 1.4 + body2.height * 0.82)
    window.add(leg2_2, (window.width - leg2_2.width) / 2 - face.width / 1.05 + body_2.width/3.3,
               (window.height - leg2_2.height) / 2 + face.height / 1.4 + body2.height * 0.82)
    window.add(body_2, (window.width - body_2.width) / 2 - face.width/1.05,
               (window.height - body_2.height) / 2 + face.height / 1.4)
    window.add(body2_2, (window.width - body2_2.width) / 2 - face.width/1.05,
               (window.height - body2_2.height) / 2 + face.height / 1.4 + body_2.height / 3.3)
    window.add(body3_2, (window.width - body3_2.width) / 2 - face.width/1.05,
               (window.height - body3_2.height) / 2 + face.height / 1.2)
    window.add(arm2_l, (window.width - arm2_l.width) / 2 - face.width / 1.05 - body_2.width/2.9,
               (window.height - arm2_l.height) / 2 + face2.height / 1.06)
    window.add(arm2_r, (window.width - arm2_r.width) / 2 - face.width / 1.05 + body_2.width/2.9,
               (window.height - arm2_r.height) / 2 + face2.height / 1.06)
    window.add(ear2_l, (window.width - ear2_l.width) / 2 - face.width / 0.8,
               (window.height - ear2_l.height) / 2 - face2.height / 9)
    window.add(ear2_ll, (window.width - ear2_ll.width) / 2 - face.width / 0.8,
               (window.height - ear2_ll.height) / 2 - face2.height / 15)
    window.add(ear2_r, (window.width - ear2_r.width) / 2 - face.width / 1.5,
               (window.height - ear2_r.height) / 2 - face2.height / 9)
    window.add(ear2_rr, (window.width - ear2_rr.width) / 2 - face.width / 1.52,
               (window.height - ear2_rr.height) / 2 - face2.height / 15)
    window.add(face2, (window.width-face2.width)/2 - face.width/1.05, (window.height-face2.height)/2 + face2.height/4)
    window.add(eye2_l, (window.width - eye2_l.width) / 2 - face.width / 0.9,
               (window.height - eye2_l.height) / 2 + face2.height/4)
    window.add(eye2_r, (window.width - eye2_r.width) / 2 - face.width / 1.25,
               (window.height - eye2_r.height) / 2 + face2.height/4)
    window.add(mouth2, (window.width - mouth2.width) / 2 - face.width/1.05,
               (window.height - mouth2.height) / 2 + face2.height / 2.4)
    window.add(nose2, (window.width - nose2.width) / 2 - face.width/1.05,
               (window.height - nose2.height) / 2 + face2.height / 2.5)
    window.add(mouth2_1, (window.width - mouth2_1.width) / 2 - face.width / 1,
               (window.height - mouth2_1.height) / 2 + face2.height / 2.5)
    window.add(mouth2_2, (window.width - mouth2_2.width) / 2 - face.width / 1.1,
               (window.height - mouth2_2.height) / 2 + face2.height / 2.5)
    window.add(buttons, (window.width-buttons.width)/2 - face.width/1.05,
               (window.height-buttons.height)/2 + face.height/1.62)


def face_maker(size=180, color='0x9C661F'):
    """
    The function produce kuma's face
    :param size: int, face size
    :param color: str, color number
    :return: GOval, kuma's face
    """
    face = GOval(size, size-20)
    face.filled = True
    face.fill_color = color
    return face


def eye_maker(size=20):
    """
    The function produce kuma's eye
    :param size: int, eye size
    :return: GOval, kuma's eye
    """
    eye = GOval(size, size)
    eye.filled = True
    return eye


def mouth_maker(size=50, color='white'):
    """
    The function produce kuma's mouth
    :param size: int, mouth size
    :param color: str, color number
    :return: GOval, kuma's mouth
    """
    mouth = GOval(size, size-10)
    mouth.filled = True
    mouth.color = color
    mouth.fill_color = color
    return mouth


def ear_maker(size=60, color='0x9C661F'):
    """
    The function produce kuma's ear
    :param size: int, ear size
    :param color: str, color number
    :return: GOval, kuma's ear
    """
    ear = GOval(size, size)
    ear.filled = True
    ear.fill_color = color
    return ear


def ear2_maker(size=40, color='yellow'):
    """
    The function produce kuma's inner_ear
    :param size: int, inner_ear size
    :param color: str, color number
    :return: GOval, kuma's inner_ear
    """
    ear2 = GOval(size, size)
    ear2.filled = True
    ear2.fill_color = color
    return ear2


def background_maker():
    """
    The function produce window background
    :return: GRect, background
    """
    background = GRect(window.width, window.height)
    background.filled = True
    background.fill_color = '0xFFFCEC'
    background.color = '0xFFFCEC'
    return background


def label_maker(string, size, font='Courier'):
    """
    The function produce any label
    :param string: str, what you want text
    :param size: int, text size
    :param font: str, font
    :return: GLabel, label
    """
    label = GLabel(string)
    label.font = str(font) + '-' + str(size)
    return label


def body_maker(size=130, color='0x9C661F'):
    """
    The function produce kuma's body
    :param size: int, body size
    :param color: str, color number
    :return: GOval, kuma's body
    """
    body = GOval(size, size+30)
    body.filled = True
    body.fill_color = color
    body.color = color
    return body


def body2_maker(size=105, color='0x9C661F'):
    """
    The function produce kuma's body
    :param size: int, body size
    :param color: str, color number
    :return: GOval, kuma's body
    """
    body2 = GOval(size, size-45)
    body2.filled = True
    body2.fill_color = color
    body2.color = color
    return body2


def body3_maker(size=80, color='white'):
    """
    The function produce kuma's body
    :param size: int, body size
    :param color: str, color number
    :return: GOval, kuma's body
    """
    body3 = GOval(size, size+20)
    body3.filled = True
    body3.fill_color = color
    body3.color = color
    return body3


def arm1_maker(size=60, color='0x9C661F'):
    """
    The function produce kuma's arm
    :param size: int, arm size
    :param color: str, color number
    :return: GArc, kuma's arm
    """
    arm = GArc(size, size+30, 100, 200)
    arm.filled = True
    arm.fill_color = color
    return arm


def arm2_maker(size=60, color='0x9C661F'):
    """
    The function produce kuma's arm
    :param size: int, arm size
    :param color: str, color number
    :return: GArc, kuma's arm
    """
    arm = GArc(size, size+30, 245, 200)
    arm.filled = True
    arm.fill_color = color
    return arm


def leg_maker(size=40, color='0x9C661F'):
    """
    The function produce kuma's leg
    :param size: int, leg size
    :param color: str, color number
    :return: GOval, kuma's leg
    """
    leg = GOval(size, size+30)
    leg.filled = True
    leg.fill_color = color
    leg.color = color
    return leg


if __name__ == '__main__':
    main()
