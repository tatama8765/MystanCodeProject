"""
File: 
Name:
楊庭瑄
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect,GPolygon,GArc,GLine,GLabel
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage



def main():
    """
    Title: Cute Rilakkuma
    This  is my friend Rilakkuma, because they are so cute,so I want to draw them.
    """
    # to generate a window width 850 and height 465
    window = GWindow(width=850,height=465,title='Rilakkuma')
    # the center background
    background = GOval(316, 285, x=263, y=52)
    background.filled = True
    background.fill_color = 'lightpink'
    window.add(background)
    # candy left background
    background2 = GPolygon()
    background2.add_vertex((262, 118))
    background2.add_vertex((260,116))
    background2.add_vertex((258,114))
    background2.add_vertex((251,111))
    background2.add_vertex((251, 109))
    background2.add_vertex((247, 107))
    background2.add_vertex((244, 104))
    background2.add_vertex((237, 102))
    background2.add_vertex((235,101))
    background2.add_vertex((230,99))
    background2.add_vertex((228,97))
    background2.add_vertex((224, 97))
    background2.add_vertex((218, 95))
    background2.add_vertex((215, 95))
    background2.add_vertex((211, 97))
    background2.add_vertex((209, 96))
    background2.add_vertex((204, 97))
    background2.add_vertex((200, 96))
    background2.add_vertex((199, 96))
    background2.add_vertex((194, 98))
    background2.add_vertex((192, 96))
    background2.add_vertex((188, 98))
    background2.add_vertex((184, 99))
    background2.add_vertex((180, 100))
    background2.add_vertex((172, 106))
    background2.add_vertex((168, 110))
    background2.add_vertex((167, 109))
    background2.add_vertex((164, 111))
    background2.add_vertex((161, 113))
    background2.add_vertex((158, 115))
    background2.add_vertex((153, 119))
    background2.add_vertex((152, 122))
    background2.add_vertex((149, 127))
    background2.add_vertex((147, 130))
    background2.add_vertex((146, 134))
    background2.add_vertex((145, 138))
    background2.add_vertex((143, 142))
    background2.add_vertex((142, 144))
    background2.add_vertex((140, 149))
    background2.add_vertex((138, 154))
    background2.add_vertex((139, 158))
    background2.add_vertex((139, 160))
    background2.add_vertex((139, 167))
    background2.add_vertex((140, 169))
    background2.add_vertex((141, 173))
    background2.add_vertex((142, 176))
    background2.add_vertex((143, 180))
    background2.add_vertex((146, 183))
    background2.add_vertex((145, 185))
    background2.add_vertex((141, 188))
    background2.add_vertex((140, 190))
    background2.add_vertex((139, 190))
    background2.add_vertex((138, 194))
    background2.add_vertex((136, 197))
    background2.add_vertex((135, 199))
    background2.add_vertex((133, 202))
    background2.add_vertex((130, 205))
    background2.add_vertex((129, 210))
    background2.add_vertex((128, 213))
    background2.add_vertex((129, 217))
    background2.add_vertex((126, 224))
    background2.add_vertex((127, 228))
    background2.add_vertex((126, 233))
    background2.add_vertex((127, 237))
    background2.add_vertex((128, 242))
    background2.add_vertex((131, 250))
    background2.add_vertex((133, 254))
    background2.add_vertex((136, 259))
    background2.add_vertex((143, 268))
    background2.add_vertex((147, 275))
    background2.add_vertex((155, 294))
    background2.add_vertex((159, 298))
    background2.add_vertex((168, 307))
    background2.add_vertex((172, 317))
    background2.add_vertex((176, 318))
    background2.add_vertex((180, 326))
    background2.add_vertex((184, 324))
    background2.add_vertex((190, 328))
    background2.add_vertex((195, 331))
    background2.add_vertex((200, 333))
    background2.add_vertex((204, 332))
    background2.add_vertex((211, 336))
    background2.add_vertex((218, 337))
    background2.add_vertex((224, 337))
    background2.add_vertex((239, 338))
    background2.add_vertex((250, 343))
    background2.add_vertex((255, 341))
    background2.add_vertex((258, 341))
    background2.add_vertex((265, 339))
    background2.add_vertex((266, 338))
    background2.add_vertex((273, 335))
    background2.add_vertex((277, 333))
    background2.add_vertex((279, 331))
    background2.add_vertex((281, 329))
    background2.add_vertex((283, 327))
    background2.add_vertex((285, 325))
    background2.add_vertex((287, 323))
    background2.add_vertex((289, 321))
    background2.add_vertex((291, 319))
    background2.add_vertex((293, 317))
    background2.add_vertex((295, 315))
    background2.add_vertex((297, 313))
    background2.add_vertex((299, 311))
    background2.add_vertex((301, 309))
    background2.add_vertex((303, 307))
    background2.filled = True
    background2.fill_color = 'lightpink'
    window.add(background2)

    # candy right background
    background3 = GPolygon()
    background3.add_vertex((547, 107))
    background3.add_vertex((627, 56))
    background3.add_vertex((647, 53))
    background3.add_vertex((666, 59))
    background3.add_vertex((673, 64))
    background3.add_vertex((680, 71))
    background3.add_vertex((685, 82))
    background3.add_vertex((688, 93))
    background3.add_vertex((690, 106))
    background3.add_vertex((689, 117))
    background3.add_vertex((686, 127))
    background3.add_vertex((685, 134))
    background3.add_vertex((697, 142))
    background3.add_vertex((705, 157))
    background3.add_vertex((690, 166))
    background3.add_vertex((684, 173))
    background3.add_vertex((653, 162))
    background3.add_vertex((610, 157))
    background3.add_vertex((586, 138))
    background3.add_vertex((563, 130))
    background3.add_vertex((554, 114))
    background3.add_vertex((548, 107))
    background3.filled = True
    background3.fill_color = 'lightpink'
    window.add(background3)

    # to add circle to the candy
    background3circle = GOval(30,30,x=634,y=127)
    background3circle.filled = True
    background3circle.fill_color = 'white'
    window.add(background3circle)

    # to add circle to the candy
    background3circle2 = GArc(50,50,218,180,x=598,y=42)
    background3circle2.filled = True
    background3circle2.fill_color = 'white'
    window.add(background3circle2)

    # to add circle to the candy
    backcircle1 = GOval(30,30,x=328,y=288)
    backcircle1.filled = True
    backcircle1.fill_color = 'white'
    window.add(backcircle1)

    # to add circle to the candy
    backcircle2 = GArc(52,52,-173,180,x=380,y=41)
    backcircle2.filled = True
    backcircle2.fill_color = 'white'
    window.add(backcircle2)

    # to add circle to the candy
    backcircle3 = GArc(32, 32, -195, 180, x=460, y=52)
    backcircle3.filled = True
    backcircle3.fill_color = 'white'
    window.add(backcircle3)

    # to add circle to the candy
    backcircle4 = GOval(30,30,x=128,y=215)
    backcircle4.filled = True
    backcircle4.fill_color = 'white'
    window.add(backcircle4)

    # to add circle to the candy
    backcircle5 = GOval(30, 30, x=210, y=128)
    backcircle5.filled = True
    backcircle5.fill_color = 'white'
    window.add(backcircle5)

    # to add circle to the candy
    backcircle6 = GOval(30, 30, x=212, y=215)
    backcircle6.filled = True
    backcircle6.fill_color = 'white'
    window.add(backcircle6)

    # to add circle to the candy
    backcircle7 = GArc(31, 31, 260, 180, x=133, y=131)
    backcircle7.filled = True
    backcircle7.fill_color = 'white'
    window.add(backcircle7)

    # to add circle to the candy
    backcircle8 = GArc(31, 31, 275, 180, x=224, y=304)
    backcircle8.filled = True
    backcircle8.fill_color = 'white'
    window.add(backcircle8)

   # to draw the background line on the left
    backline1 = GPolygon()
    backline1.add_vertex((1,271))
    backline1.add_vertex((8, 296))
    backline1.add_vertex((17, 325))
    backline1.add_vertex((44, 436))
    backline1.add_vertex((55, 428))
    backline1.add_vertex((28, 313))
    backline1.add_vertex((18, 280))
    backline1.add_vertex((9, 254))
    backline1.add_vertex((1, 230))
    backline1.filled = True
    backline1.fill_color = 'lightgoldenrodyellow'
    window.add(backline1)

    # to draw the background line on the left
    backline2 = GPolygon()
    backline2.add_vertex((1, 158))
    backline2.add_vertex((38, 282))
    backline2.add_vertex((51, 328))
    backline2.add_vertex((76, 404))
    backline2.add_vertex((91, 394))
    backline2.add_vertex((61, 313))
    backline2.add_vertex((31, 218))
    backline2.add_vertex((20, 177))
    backline2.add_vertex((12, 151))
    backline2.filled = True
    backline2.fill_color = 'lightgoldenrodyellow'
    window.add(backline2)

    # to draw the background line on the left
    backline3 = GPolygon()
    backline3.add_vertex((33, 155))
    backline3.add_vertex((50, 216))
    backline3.add_vertex((77, 304))
    backline3.add_vertex((104, 390))
    backline3.add_vertex((115, 387))
    backline3.add_vertex((92, 307))
    backline3.add_vertex((77, 255))
    backline3.add_vertex((61, 199))
    backline3.add_vertex((51, 161))
    backline3.filled = True
    backline3.fill_color = 'lightgoldenrodyellow'
    window.add(backline3)

    # to draw the background line on the left
    backline4 = GPolygon()
    backline4.add_vertex((72, 175))
    backline4.add_vertex((92, 240))
    backline4.add_vertex((110, 303))
    backline4.add_vertex((129, 343))
    backline4.add_vertex((144, 350))
    backline4.add_vertex((118, 273))
    backline4.add_vertex((100, 224))
    backline4.add_vertex((91, 185))
    backline4.filled = True
    backline4.fill_color = 'lightgoldenrodyellow'
    window.add(backline4)

    # to draw the background line on the left
    backline5 = GPolygon()
    backline5.add_vertex((113, 197))
    backline5.add_vertex((122, 229))
    backline5.add_vertex((128, 226))
    backline5.add_vertex((124, 196))
    backline5.filled = True
    backline5.fill_color = 'lightgoldenrodyellow'
    window.add(backline5)

    # to draw the background line on the left
    backline6 = GPolygon()
    backline6.add_vertex((1, 159))
    backline6.add_vertex((14, 150))
    backline6.add_vertex((20, 150))
    backline6.add_vertex((44, 156))
    backline6.add_vertex((66, 168))
    backline6.add_vertex((83, 178))
    backline6.add_vertex((99, 188))
    backline6.add_vertex((108, 194))
    backline6.add_vertex((121, 197))
    backline6.add_vertex((128, 194))
    backline6.add_vertex((121, 197))
    backline6.add_vertex((128, 194))
    backline6.add_vertex((134, 194))
    backline6.add_vertex((142, 186))
    backline6.add_vertex((139, 180))
    backline6.add_vertex((122, 188))
    backline6.add_vertex((95, 176))
    backline6.add_vertex((78, 166))
    backline6.add_vertex((62, 156))
    backline6.add_vertex((40, 146))
    backline6.add_vertex((25, 142))
    backline6.add_vertex((15, 142))
    backline6.add_vertex((2, 148))
    backline6.filled = True
    backline6.fill_color = 'sienna'
    window.add(backline6)

    # to draw the background line on the right
    backline21 = GPolygon()
    backline21.add_vertex((698,342))
    backline21.add_vertex((741,383))
    backline21.add_vertex((785, 424))
    backline21.add_vertex((847, 474))
    backline21.add_vertex((845, 453))
    backline21.add_vertex((791, 409))
    backline21.add_vertex((725, 347))
    backline21.add_vertex((696, 326))
    backline21.filled = True
    backline21.fill_color = 'paleturquoise'
    window.add(backline21)

    # to draw the background line on the right
    backline22 = GPolygon()
    backline22.add_vertex((720, 306))
    backline22.add_vertex((758, 332))
    backline22.add_vertex((811, 364))
    backline22.add_vertex((847, 393))
    backline22.add_vertex((849, 372))
    backline22.add_vertex((825, 352))
    backline22.add_vertex((762, 306))
    backline22.add_vertex((734, 285))
    backline22.filled = True
    backline22.fill_color = 'paleturquoise'
    window.add(backline22)

    # to draw the background line on the right
    backline23 = GPolygon()
    backline23.add_vertex((742, 253))
    backline23.add_vertex((777, 278))
    backline23.add_vertex((846, 326))
    backline23.add_vertex((848, 332))
    backline23.add_vertex((849, 302))
    backline23.add_vertex((839, 293))
    backline23.add_vertex((813, 276))
    backline23.add_vertex((734, 229))
    backline23.filled = True
    backline23.fill_color = 'paleturquoise'
    window.add(backline23)

    # to draw the background line on the right
    backline24 = GPolygon()
    backline24.add_vertex((790, 220))
    backline24.add_vertex((849, 261))
    backline24.add_vertex((849, 232))
    backline24.add_vertex((812, 204))
    backline24.filled = True
    backline24.fill_color = 'paleturquoise'
    window.add(backline24)

    # to draw the background line on the right
    backline25 = GPolygon()
    backline25.add_vertex((841, 186))
    backline25.add_vertex((848, 191))
    backline25.add_vertex((849, 181))
    backline25.filled = True
    backline25.fill_color = 'paleturquoise'
    window.add(backline25)

    # to draw the background line on the right
    backline26 = GPolygon()
    backline26.add_vertex((767,205))
    backline26.add_vertex((788, 211))
    backline26.add_vertex((848, 170))
    backline26.add_vertex((849, 181))
    backline26.add_vertex((786, 219))
    backline26.add_vertex((767, 212))
    backline26.filled = True
    backline26.fill_color = 'saddlebrown'
    window.add(backline26)

    # the left brown bear
    face = GOval(78,57,x=21,y=334)
    face.filled = True
    face.fill_color = 'Peru'
    window.add(face)
    lear = GOval(24,28,x=1,y=337)
    lear.filled = True
    lear.fill_color = 'Peru'
    window.add(lear)
    rear = GOval(24,28,x=66,y=307)
    rear.filled = True
    rear.fill_color = 'Peru'
    window.add(rear)
    leye = GOval(8,8,x=48,y=371)
    leye.filled = True
    leye.fill_color ='saddlebrown'
    window.add(leye)
    reye = GOval(8,8,x=77,y=352)
    reye.filled = True
    reye.fill_color = 'saddlebrown'
    window.add(reye)
    mouth = GOval(22,17,x=60,y=363)
    mouth.filled = True
    mouth.fill_color = 'white'
    window.add(mouth)
    nose = GOval(4,4,x=68,y=368)
    nose.filled = True
    nose.fill_color = 'saddlebrown'
    window.add(nose)
    noselinel = GLine(70,368,70,377)
    noselinel.color='saddlebrown'
    window.add(noselinel)
    noseliner = GLine(70,369,79,370)
    noseliner.color ='saddlebrown'
    window.add(noseliner)
    dudu = GOval(50,50,x=70,y=381)
    dudu.filled = True
    dudu.fill_color = 'Peru'
    window.add(dudu)
    llear = GOval(13,13,x=4,y=347)
    llear.filled = True
    llear.fill_color = 'Gold'
    window.add(llear)
    rrear = GOval(13,13,x=75,y=311)
    rrear.filled = True
    rrear.fill_color = 'Gold'
    window.add(rrear)
    lhand = GArc(25,30,65,180,x=67,y=388)
    lhand.filled = True
    lhand.fill_color = 'Peru'
    window.add(lhand)
    rhand = GArc(25,30,-33,180,x=90,y=376)
    rhand.filled = True
    rhand.fill_color = 'Peru'
    window.add(rhand)
    ddduu = GOval(20,20,x=84,y=393)
    ddduu.filled = True
    ddduu.fill_color = 'white'
    window.add(ddduu)
    lhand2 = GArc(25,25,90,358,x=137,y=349)
    lhand2.filled =True
    lhand2.fill_color = 'Gold'
    window.add(lhand2)

    # to draw yellow chicken on the left side
    face2 = GPolygon()
    face2.add_vertex((125,324))
    face2.add_vertex((125,333))
    face2.add_vertex((127,363))
    face2.add_vertex((128, 367))

    # to draw yellow chicken on the left side
    face2.add_vertex((129,385))
    face2.add_vertex((132,385))
    face2.add_vertex((132,389))
    face2.add_vertex((135,395))
    face2.add_vertex((139,396))
    face2.add_vertex((146,398))
    face2.add_vertex((150,396))
    face2.add_vertex((153,394))
    face2.add_vertex((157,388))
    face2.add_vertex((156,386))
    face2.add_vertex((157,381))

    # to draw yellow chicken on the left side
    face2.add_vertex((168,389))
    face2.add_vertex((179,388))
    face2.add_vertex((193,384))
    face2.add_vertex((202,384))
    face2.add_vertex((214,381))

    # to draw yellow chicken on the left side
    face2.add_vertex((218,377))
    face2.add_vertex((219,381))
    face2.add_vertex((222,382))
    face2.add_vertex((226,384))
    face2.add_vertex((233,382))
    face2.add_vertex((235, 380))
    face2.add_vertex((240, 372))
    face2.add_vertex((240, 367))
    face2.add_vertex((243,353))
    face2.add_vertex((231,310))
    face2.add_vertex((227,302))
    face2.add_vertex((224,297))

    # to draw yellow chicken on the left side
    face2.filled = True
    face2.fill_color = 'Gold '
    window.add(face2)

    # to draw yellow chicken on the left side
    leye2 = GOval(12,9,x=198,y=319)
    leye2.filled = True
    leye2.fill_color = 'saddlebrown'
    window.add(leye2)
    leye3 = GOval(12, 9, x=141, y=334)
    leye3.filled = True
    leye3.fill_color = 'saddlebrown'
    window.add(leye3)
    nose2 = GOval(35,20,x=161,y=328)
    nose2.filled = True
    nose2.fill_color = 'orange'
    window.add(nose2)
    nose21 = GOval(6, 6, x=167, y=336)
    nose21.filled = True
    nose21.fill_color = 'saddlebrown'
    window.add(nose21)
    nose22 = GOval(6, 6, x=181, y=334)
    nose22.filled = True
    nose22.fill_color = 'saddlebrown'
    window.add(nose22)
    nose23 = GOval(15, 8, x=173, y=348)
    nose23.filled = True
    nose23.fill_color = 'orange'
    window.add(nose23)
    # to draw yellow chicken on the left side
    hat = GPolygon()
    hat.add_vertex((121,310))
    hat.add_vertex((114, 319))
    hat.add_vertex((115, 326))
    hat.add_vertex((123, 329))
    hat.add_vertex((127, 325))
    hat.add_vertex((135, 329))
    hat.add_vertex((142, 325))
    hat.add_vertex((145, 321))
    hat.add_vertex((152, 325))
    hat.add_vertex((157, 322))
    hat.add_vertex((160, 315))
    hat.add_vertex((163, 320))
    hat.add_vertex((172, 320))
    hat.add_vertex((177, 312))
    hat.add_vertex((186, 306))
    hat.add_vertex((191, 311))
    hat.add_vertex((200, 314))
    hat.add_vertex((203, 306))
    hat.add_vertex((215, 309))
    hat.add_vertex((218, 303))
    hat.add_vertex((227, 303))
    hat.add_vertex((231, 297))
    hat.add_vertex((225, 291))
    hat.add_vertex((218, 289))
    hat.add_vertex((203, 272))
    hat.add_vertex((184, 265))
    hat.add_vertex((159, 267))
    hat.add_vertex((144, 273))
    hat.add_vertex((126, 285))
    hat.add_vertex((117, 297))
    hat.add_vertex((118, 305))
    hat.add_vertex((121, 308))

    hat.filled = True
    hat.fill_color = 'white'
    window.add(hat)

    # need to write body5 here white bear
    body5 = GPolygon()
    body5.add_vertex((590,307))
    body5.add_vertex((582,332))
    body5.add_vertex((603,336))
    body5.add_vertex((594,410))
    body5.add_vertex((651,410))
    body5.add_vertex((700, 410))
    body5.add_vertex((708, 307))
    body5.filled = True
    body5.fill_color = 'antiquewhite'
    window.add(body5)

    # white bear
    rhand5 = GArc(70,90,-90,180,x=685,y=318)
    rhand5.filled = True
    rhand5.fill_color = 'antiquewhite'
    window.add(rhand5)

    # white bear
    dudu5 = GOval(40,40,x=627,y=334)
    dudu5.filled = True
    dudu5.fill_color = 'red'
    window.add(dudu5)

    ddduu1 = GOval(10,10,x=637,y=344)
    ddduu1.filled = True
    ddduu1.fill_color = 'saddlebrown'
    window.add(ddduu1)

    # white bear
    ddduu2 = GOval(10, 10, x=637, y=359)
    ddduu2.filled = True
    ddduu2.fill_color = 'saddlebrown'
    window.add(ddduu2)

    # white bear
    ddduu3 = GOval(10, 10, x=652, y=344)
    ddduu3.filled = True
    ddduu3.fill_color = 'saddlebrown'
    window.add(ddduu3)

    # white bear
    ddduu4 = GOval(10, 10, x=652, y=359)
    ddduu4.filled = True
    ddduu4.fill_color = 'saddlebrown'
    window.add(ddduu4)

    # white chicken dudu
    dudu7 = GOval(58,88,x=779,y=348)
    dudu7.filled = True
    dudu7.fill_color = 'white'
    window.add(dudu7)

    # white chicken_left_hand
    lhand7 = GArc(100,80,90,180,x=758,y=391)
    lhand7.filled = True
    lhand7.fill_color ='saddlebrown'
    window.add(lhand7)

    # white chicken_right_hand
    rhand7 = GArc(120, 20, -90, 180, x=805, y=391)
    rhand7.filled = True
    rhand7.fill_color = 'saddlebrown'
    window.add(rhand7)

    # white chicken
    face7 = GOval(78, 62, x=770, y=337)
    face7.filled = True
    face7.fill_color = 'white'
    window.add(face7)

    # white chicken
    leye7 = GOval(8, 8, x=789, y=357)
    leye7.filled = True
    leye7.fill_color = 'saddlebrown'
    window.add(leye7)

    # white chicken
    reye7 = GOval(8, 8, x=824, y=357)
    reye7.filled = True
    reye7.fill_color = 'saddlebrown'
    window.add(reye7)

    # white chicken
    upper_mouth = GArc(30,40,0,180,x=795,y=368)
    upper_mouth.filled = True
    upper_mouth.fill_color = 'orange'
    window.add(upper_mouth)

    # white chicken
    lower_mouth = GArc(30, 40, 180, 180, x=795, y=368)
    lower_mouth.filled = True
    lower_mouth.fill_color = 'orange'
    window.add(lower_mouth)

    # to draw the background on the ground
    plan = GArc(850,310,0,180,x=0,y=385)
    plan.filled = True
    plan.fill_color = 'paleturquoise'
    window.add(plan)

    # to draw the brown bear
    face3 = GOval(250,200,x=284,y=96)
    face3.filled = True
    face3.fill_color = 'Peru'
    window.add(face3)
    leye4 = GOval(27,29,x=337,y=203)
    leye4.filled = True
    leye4.fill_color = 'saddlebrown'
    window.add(leye4)
    reye4 = GOval(27, 29, x=460, y=203)
    reye4.filled = True
    reye4.fill_color = 'saddlebrown'
    window.add(reye4)
    mouth2 = GOval(66, 51, x=383, y=216)
    mouth2.filled = True
    mouth2.fill_color = 'white'
    window.add(mouth2)
    nose3 = GOval(14, 14, x=408, y=224)
    nose3.filled = True
    nose3.fill_color = 'saddlebrown'
    window.add(nose3)
    noseline21 = GLine(411,239,396,253)
    noseline21.color = 'saddlebrown'
    window.add(noseline21)
    noseline22 = GLine(419, 239, 435, 253)
    noseline22.color = 'saddlebrown'
    window.add(noseline22)
    lear2 = GOval(69,69,x=267,y=68)
    lear2.filled = True
    lear2.fill_color = 'Peru'
    window.add(lear2)
    rear2 = GOval(69,69,x=473,y=64)
    rear2.filled = True
    rear2.fill_color = 'Peru'
    window.add(rear2)
    llear2= GOval(50, 31, x=273, y=105)
    llear2.filled = True
    llear2.fill_color = 'Gold'
    window.add(llear2)
    rrear2 = GOval(50, 31, x=480, y=100)
    rrear2.filled = True
    rrear2.fill_color = 'Gold'
    window.add(rrear2)
    dudu2 = GRect(90,90,x=373,y=295)
    dudu2.filled = True
    dudu2.fill_color = 'Peru'
    window.add(dudu2)
    lhand3 = GArc(100,90,80,180,x=352,y=295)
    lhand3.filled = True
    lhand3.fill_color = 'Peru'
    window.add(lhand3)
    rhand3 = GArc(110, 90, -95, 180, x=415, y=293)
    rhand3.filled = True
    rhand3.fill_color = 'Peru'
    window.add(rhand3)
    dudu5 = GOval(50,50,x=387,y=320)
    dudu5.filled = True
    dudu5.fill_color = 'white'
    window.add(dudu5)

    # to draw white bear in the right
    lear5 = GOval(60,60,x=550,y=128)
    lear5.filled = True
    lear5.fill_color = 'antiquewhite'
    window.add(lear5)
    llear5 = GOval(38,33,x=558,y=155)
    llear5.filled = True
    llear5.fill_color = 'hotpink'
    window.add(llear5)
    rear5 = GOval(60, 60, x=713, y=121)
    rear5.filled = True
    rear5.fill_color = 'antiquewhite'
    window.add(rear5)
    rrear5 = GOval(38, 33, x=725, y=147)
    rrear5.filled = True
    rrear5.fill_color = 'hotpink'
    window.add(rrear5)
    face5 = GOval(215, 170, x=561, y=153)
    face5.filled = True
    face5.fill_color = 'antiquewhite'
    window.add(face5)
    lleye5 = GOval(24,24,x=595,y=243)
    lleye5.filled = True
    lleye5.fill_color = 'saddlebrown'
    window.add(lleye5)
    rreye5 = GOval(24, 24, x=690, y=243)
    rreye5.filled = True
    rreye5.fill_color = 'saddlebrown'
    window.add(rreye5)
    mouth5 = GOval(45,38,x=632,y=256)
    mouth5.filled = True
    mouth5.fill_color = 'white'
    window.add(mouth5)
    nnose5 = GOval(12,12,x=650,y=262)
    nnose5.filled = True
    nnose5.fill_color = 'saddlebrown'
    window.add(nnose5)
    nose5line1 = GLine(652,271,636,284)
    nose5line1.filled = True
    nose5line1.fill_color = 'saddlebrown'
    window.add(nose5line1)
    nose5line2 = GLine(657, 273, 666, 288)
    nose5line2.filled = True
    nose5line2.fill_color = 'saddlebrown'
    window.add(nose5line2)

    # white bear

    face6 = GPolygon()
    face6.add_vertex((519,266))
    face6.add_vertex((508, 265))
    face6.add_vertex((501, 264))
    face6.add_vertex((494, 270))
    face6.add_vertex((490, 276))
    face6.add_vertex((490, 283))
    face6.add_vertex((494, 291))
    face6.add_vertex((505, 304))
    face6.add_vertex((501, 312))
    face6.add_vertex((509, 317))
    face6.add_vertex((515, 317))
    face6.add_vertex((523, 325))
    face6.add_vertex((533, 329))
    face6.add_vertex((545, 331))
    face6.add_vertex((553, 333))
    face6.add_vertex((558, 339))
    face6.add_vertex((576, 340))
    face6.add_vertex((579, 331))
    face6.add_vertex((591, 317))
    face6.add_vertex((593, 307))
    face6.add_vertex((573, 285))
    face6.add_vertex((561, 276))
    face6.add_vertex((542, 268))
    face6.add_vertex((532, 267))
    face6.add_vertex((533, 262))
    face6.add_vertex((521, 258))
    face6.add_vertex((520, 265))
    face6.filled = True
    face6.fill_color = 'white'
    window.add(face6)

    # white bear
    rhead = GPolygon()
    rhead.add_vertex((532,283))
    rhead.add_vertex((527, 293))
    rhead.add_vertex((533, 296))
    rhead.add_vertex((537, 288))
    rhead.filled = True
    rhead.fill_color = 'white'
    window.add(rhead)

    # white bear
    eye6 = GOval(6,6,x=510,y=283)
    eye6.filled = True
    eye6.fill_color = 'saddlebrown'
    window.add(eye6)






if __name__ == '__main__':
    main()
