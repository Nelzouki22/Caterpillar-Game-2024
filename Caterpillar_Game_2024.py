import pygame
import time
import random

pygame.init()

# إعدادات الشاشة والألوان
white = (255, 255, 255)  # اللون الأبيض
yellow = (255, 255, 102)  # اللون الأصفر
black = (0, 0, 0)  # اللون الأسود
green = (0, 255, 0)  # اللون الأخضر
red = (213, 50, 80)  # اللون الأحمر
blue = (50, 153, 213)  # اللون الأزرق

# أبعاد نافذة اللعبة
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Caterpillar Game')

clock = pygame.time.Clock()
caterpillar_block = 10  # حجم الكتلة في الكاتربيلر
caterpillar_speed = 15  # سرعة الكاتربيلر

# دالة لرسم الكاتربيلر
def our_caterpillar(caterpillar_block, caterpillar_list):
    for x in caterpillar_list:
        pygame.draw.rect(dis, green, [x[0], x[1], caterpillar_block, caterpillar_block])

# دالة لإظهار الرسائل على الشاشة
def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# حلقة اللعبة الرئيسية
def gameLoop():
    game_over = False
    game_close = False

    # تحديد موقع الكاتربيلر
    x1 = dis_width / 2
    y1 = dis_height / 2

    # تحديد تغيرات الموقع
    x1_change = 0
    y1_change = 0

    caterpillar_List = []  # قائمة لتخزين مواقع الكاتربيلر
    Length_of_caterpillar = 1  # طول الكاتربيلر

    # تحديد موقع الطعام بشكل عشوائي
    foodx = round(random.randrange(0, dis_width - caterpillar_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - caterpillar_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # الضغط على Q لإنهاء اللعبة
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # الضغط على C لإعادة تشغيل اللعبة
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -caterpillar_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = caterpillar_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -caterpillar_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = caterpillar_block
                    x1_change = 0

        # التحقق من الاصطدام بالحواف
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, yellow, [foodx, foody, caterpillar_block, caterpillar_block])
        caterpillar_Head = []
        caterpillar_Head.append(x1)
        caterpillar_Head.append(y1)
        caterpillar_List.append(caterpillar_Head)
        if len(caterpillar_List) > Length_of_caterpillar:
            del caterpillar_List[0]

        # التحقق من الاصطدام بنفسه
        for x in caterpillar_List[:-1]:
            if x == caterpillar_Head:
                game_close = True

        # رسم الكاتربيلر
        our_caterpillar(caterpillar_block, caterpillar_List)

        pygame.display.update()

        # التحقق من الاصطدام بالطعام
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - caterpillar_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - caterpillar_block) / 10.0) * 10.0
            Length_of_caterpillar += 1

        clock.tick(caterpillar_speed)

    pygame.quit()
    quit()

gameLoop()

