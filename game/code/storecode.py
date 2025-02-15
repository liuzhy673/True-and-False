import pygame
import sys
import data_module
import coin_number # type: ignore
testcase4=[]
testcase5=[]
for a in range(380,411):
    for b in range(200,231):
        testcase4.append((a,b))

for a in range(420,451):
    for b in range(200,231):
        testcase5.append((a,b))
def run_store(resurrect,health,attack,defense):
    # 初始化pygame
    pygame.init()

    # 设置屏幕大小
    screen_width = data_module.width
    screen_height = data_module.height
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('game store')

    # 加载图片和字体
    mistress = pygame.image.load('C:\\game\\picture\\storemistress.png')
    mistress = pygame.transform.scale(mistress, (260, 230))
    dialogue = pygame.image.load('C:\\game\\picture\\dialogue.png')
    dialogue = pygame.transform.scale(dialogue, (600, 200))
    coins = pygame.image.load('C:\\game\\picture\\coins.png')
    coins = pygame.transform.scale(coins, (30, 30))
    yes = pygame.image.load('C:\\game\\picture\\yes.png')
    yes = pygame.transform.scale(yes, (30, 30))
    no = pygame.image.load('C:\\game\\picture\\no.png')
    no = pygame.transform.scale(no, (30, 30))
    health_limit=pygame.image.load('C:\\game\\picture\\health.png')
    health_limit=pygame.transform.scale(health_limit,(30,30))
    try:
        font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 36)
    except IOError:
        print("字体文件加载失败,请确保Uranus_Pixel_11Px.ttf文件在程序目录下")
        sys.exit()
    background_image = pygame.image.load('C:\\game\\picture\\test.png')
    background_image = pygame.transform.scale(background_image, (800,600))

    # 设置颜色
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    RED = (255, 0, 0)
    BROWN = (165, 42, 42)
    BLACK = (0, 0, 0)

    # 金币初始值
    coins_number = coin_number.get_coin()

    # 按钮设置
    button_width = 120
    button_height = 80
    button_padding = 10

    # 按钮文本
    button_texts = [
        ["身体强化", "攻击力+5"],
        ["装备强化", "攻击力+15"],
        ["生命炼成", "血量上限+20"],
        ["武器防御", "防御+5"],
        ["重甲升级", "防御+10"],
        ["复活药水", "顾名思义"]
    ]

    # 按钮颜色
    button_colors = [
        WHITE, GREEN, BLUE, YELLOW, ORANGE, RED
    ]

    # 按钮位置
    button_positions = []
    num_buttons_per_row = len(button_texts) // 2
    for row_index, row in enumerate([button_texts[:num_buttons_per_row], button_texts[num_buttons_per_row:]]):
        row_positions = []
        for col_index, text in enumerate(row):
            start_x = (screen_width - (num_buttons_per_row * button_width + (num_buttons_per_row - 1) * button_padding)) // 2
            x = start_x + col_index * (button_width + button_padding) - 150
            y = 300 + (button_height + button_padding) * row_index
            row_positions.append((x, y))
        button_positions.extend(row_positions)

    # 创建按钮
    buttons = []
    for index, (pos, text_pair) in enumerate(zip(button_positions, button_texts)):
        button = {
            'rect': pygame.Rect(pos[0], pos[1], button_width, button_height),
            'texts': text_pair,
            'color': button_colors[index % len(button_colors)]
        }
        buttons.append(button)

    # 创建退出按钮
    exit_button_width = 80
    exit_button_height = 40
    exit_button = {
        'rect': pygame.Rect(screen_width - exit_button_width - 10, 10, exit_button_width, exit_button_height),
        'text': "退出",
        'color': RED
    }

    # 游戏主循环
    running = True
    while running:
        tiny_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 18)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                mouse_x, mouse_y = event.pos
                continue_area1=(480,210,30,30)
                continue_area2=(520,210,30,30)

                for button in buttons:
                    if button['rect'].collidepoint(mouse_pos):
                        if button['texts'][0] == "复活药水" and coins_number >= 200:
                            buying = True
                            while buying:
                                screen.blit(background_image, (0, 0))

                                shop_text_surface = font.render('商店', True, WHITE)
                                shop_text_rect = shop_text_surface.get_rect(topleft=(10, 10))
                                screen.blit(shop_text_surface, shop_text_rect)

                                for button in buttons:
                                    pygame.draw.rect(screen, button['color'], button['rect'])
                                    for i, text in enumerate(button['texts']):
                                        small_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)
                                        text_surface = small_font.render(text, True, BLACK)
                                        text_rect = text_surface.get_rect(center=button['rect'].center)
                                        if i == 0:
                                            text_rect.centery = button['rect'].centery - 10
                                        else:
                                            text_rect.centery = button['rect'].centery + 10
                                        screen.blit(text_surface, text_rect)

                                pygame.draw.rect(screen, exit_button['color'], exit_button['rect'])
                                exit_text_surface = font.render(exit_button['text'], True, BLACK)
                                exit_text_rect = exit_text_surface.get_rect(center=exit_button['rect'].center)
                                screen.blit(exit_text_surface, exit_text_rect)
                                screen.blit(coins, (10, 35))
                                show_coins = font.render(f"{coins_number}", True, YELLOW)
                                screen.blit(show_coins, (25, 35))
                                screen.blit(mistress, (500, 250))
                                
                                screen.blit(dialogue, (250, 100))
                                
                                textwritten1 = tiny_font.render("本游戏没有复活药水就是一命游戏", True, BLACK)
                                screen.blit(textwritten1, (335, 142))
                                textwritten2 = tiny_font.render("所以立刻买入吧！", True, BLACK)
                                screen.blit(textwritten2, (335, 162))
                                textwritten3 = tiny_font.render("售价：200", True, BLACK)
                                screen.blit(textwritten3, (335, 182))
                                screen.blit(yes, (480, 210))  # 确保 yes 图片已定义
                                screen.blit(no, (520, 210))  # 确保 no 图片已定义

                                pygame.display.flip()  # 更新屏幕显示

                                for event in pygame.event.get():  # 处理新的事件
                                    if event.type == pygame.QUIT:
                                        running = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = event.pos
                                        if (continue_area1[0] <= mouse_x <= continue_area1[0] + continue_area1[2] and
                                                continue_area1[1] <= mouse_y <= continue_area1[1] + continue_area1[3]):
                                            coins_number = coin_number.decrease_coin(200)  # 减少100金币
                                            resurrect+=1
                                            buying = False
                                        elif (continue_area2[0] <= mouse_x <= continue_area2[0] + continue_area2[2] and
                                            continue_area2[1] <= mouse_y <= continue_area2[1] + continue_area2[3]):
                                            buying = False

                                if not buying:
                                    # 恢复主界面
                                    screen.blit(background_image, (0, 0))  # 绘制背景
                                    screen.blit(mistress, (500, 250))
                                    screen.blit(dialogue, (250, 100))
                                    textwritten = tiny_font.render("错过此家就没下家了哦！", True, BLACK)
                                    screen.blit(textwritten, (335, 142))
                                    screen.blit(coins, (10, 35))
                                    show_coins = font.render(f"{coins_number}", True, YELLOW)
                                    screen.blit(show_coins, (25, 35))
                                    pygame.display.flip()  # 更新屏幕显示
                                    break
                        if button['texts'][0] == "身体强化" and coins_number >= 150:
                            buying = True
                            while buying:
                                screen.blit(background_image, (0, 0))

                                shop_text_surface = font.render('商店', True, WHITE)
                                shop_text_rect = shop_text_surface.get_rect(topleft=(10, 10))
                                screen.blit(shop_text_surface, shop_text_rect)

                                for button in buttons:
                                    pygame.draw.rect(screen, button['color'], button['rect'])
                                    for i, text in enumerate(button['texts']):
                                        small_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)
                                        text_surface = small_font.render(text, True, BLACK)
                                        text_rect = text_surface.get_rect(center=button['rect'].center)
                                        if i == 0:
                                            text_rect.centery = button['rect'].centery - 10
                                        else:
                                            text_rect.centery = button['rect'].centery + 10
                                        screen.blit(text_surface, text_rect)

                                pygame.draw.rect(screen, exit_button['color'], exit_button['rect'])
                                exit_text_surface = font.render(exit_button['text'], True, BLACK)
                                exit_text_rect = exit_text_surface.get_rect(center=exit_button['rect'].center)
                                screen.blit(exit_text_surface, exit_text_rect)
                                screen.blit(coins, (10, 35))
                                show_coins = font.render(f"{coins_number}", True, YELLOW)
                                screen.blit(show_coins, (25, 35))
                                screen.blit(mistress, (500, 250))
                                
                                screen.blit(dialogue, (250, 100))
                                
                                textwritten1 = tiny_font.render("武器经过洗练，攻击力+5，有小", True, BLACK)
                                screen.blit(textwritten1, (335, 142))
                                textwritten2 = tiny_font.render("部分的提升。", True, BLACK)
                                screen.blit(textwritten2, (335, 162))
                                textwritten3 = tiny_font.render("售价：150", True, BLACK)
                                screen.blit(textwritten3, (335, 182))
                                screen.blit(yes, (480, 210))  # 确保 yes 图片已定义
                                screen.blit(no, (520, 210))  # 确保 no 图片已定义

                                pygame.display.flip()  # 更新屏幕显示

                                for event in pygame.event.get():  # 处理新的事件
                                    if event.type == pygame.QUIT:
                                        running = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = event.pos
                                        if (continue_area1[0] <= mouse_x <= continue_area1[0] + continue_area1[2] and
                                                continue_area1[1] <= mouse_y <= continue_area1[1] + continue_area1[3]):
                                            coins_number = coin_number.decrease_coin(150)  # 减少100金币
                                            attack+=5
                                            buying = False
                                        elif (continue_area2[0] <= mouse_x <= continue_area2[0] + continue_area2[2] and
                                            continue_area2[1] <= mouse_y <= continue_area2[1] + continue_area2[3]):
                                            buying = False

                                if not buying:
                                    # 恢复主界面
                                    screen.blit(background_image, (0, 0))  # 绘制背景
                                    screen.blit(mistress, (500, 250))
                                    screen.blit(dialogue, (250, 100))
                                    textwritten = tiny_font.render("错过此家就没下家了哦！", True, BLACK)
                                    screen.blit(textwritten, (335, 142))
                                    screen.blit(coins, (10, 35))
                                    show_coins = font.render(f"{coins_number}", True, YELLOW)
                                    screen.blit(show_coins, (25, 35))
                                    pygame.display.flip()  # 更新屏幕显示
                                    break

                        if button['texts'][0] == "装备强化" and coins_number >= 400:
                            buying = True
                            while buying:
                                screen.blit(background_image, (0, 0))

                                shop_text_surface = font.render('商店', True, WHITE)
                                shop_text_rect = shop_text_surface.get_rect(topleft=(10, 10))
                                screen.blit(shop_text_surface, shop_text_rect)

                                for button in buttons:
                                    pygame.draw.rect(screen, button['color'], button['rect'])
                                    for i, text in enumerate(button['texts']):
                                        small_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)
                                        text_surface = small_font.render(text, True, BLACK)
                                        text_rect = text_surface.get_rect(center=button['rect'].center)
                                        if i == 0:
                                            text_rect.centery = button['rect'].centery - 10
                                        else:
                                            text_rect.centery = button['rect'].centery + 10
                                        screen.blit(text_surface, text_rect)

                                pygame.draw.rect(screen, exit_button['color'], exit_button['rect'])
                                exit_text_surface = font.render(exit_button['text'], True, BLACK)
                                exit_text_rect = exit_text_surface.get_rect(center=exit_button['rect'].center)
                                screen.blit(exit_text_surface, exit_text_rect)
                                screen.blit(coins, (10, 35))
                                show_coins = font.render(f"{coins_number}", True, YELLOW)
                                screen.blit(show_coins, (25, 35))
                                screen.blit(mistress, (500, 250))
                                
                                screen.blit(dialogue, (250, 100))
                                
                                textwritten1 = tiny_font.render("由于重新锻造，武器大幅度的", True, BLACK)
                                screen.blit(textwritten1, (335, 142))
                                textwritten2 = tiny_font.render("增强，我的工艺可不是盖的！", True, BLACK)
                                screen.blit(textwritten2, (335, 162))
                                textwritten3 = tiny_font.render("售价：400", True, BLACK)
                                screen.blit(textwritten3, (335, 182))
                                screen.blit(yes, (480, 210))  # 确保 yes 图片已定义
                                screen.blit(no, (520, 210))  # 确保 no 图片已定义

                                pygame.display.flip()  # 更新屏幕显示

                                for event in pygame.event.get():  # 处理新的事件
                                    if event.type == pygame.QUIT:
                                        running = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = event.pos
                                        if (continue_area1[0] <= mouse_x <= continue_area1[0] + continue_area1[2] and
                                                continue_area1[1] <= mouse_y <= continue_area1[1] + continue_area1[3]):
                                            coins_number = coin_number.decrease_coin(400)  # 减少100金币
                                            attack+=15
                                            buying = False
                                        elif (continue_area2[0] <= mouse_x <= continue_area2[0] + continue_area2[2] and
                                            continue_area2[1] <= mouse_y <= continue_area2[1] + continue_area2[3]):
                                            buying = False

                                if not buying:
                                    # 恢复主界面
                                    screen.blit(background_image, (0, 0))  # 绘制背景
                                    screen.blit(mistress, (500, 250))
                                    screen.blit(dialogue, (250, 100))
                                    textwritten = tiny_font.render("错过此家就没下家了哦！", True, BLACK)
                                    screen.blit(textwritten, (335, 142))
                                    screen.blit(coins, (10, 35))
                                    show_coins = font.render(f"{coins_number}", True, YELLOW)
                                    screen.blit(show_coins, (25, 35))
                                    pygame.display.flip()  # 更新屏幕显示
                                    break
                        if button['texts'][0] == "生命炼成" and coins_number >= 350:
                            buying = True
                            while buying:
                                screen.blit(background_image, (0, 0))

                                shop_text_surface = font.render('商店', True, WHITE)
                                shop_text_rect = shop_text_surface.get_rect(topleft=(10, 10))
                                screen.blit(shop_text_surface, shop_text_rect)

                                for button in buttons:
                                    pygame.draw.rect(screen, button['color'], button['rect'])
                                    for i, text in enumerate(button['texts']):
                                        small_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)
                                        text_surface = small_font.render(text, True, BLACK)
                                        text_rect = text_surface.get_rect(center=button['rect'].center)
                                        if i == 0:
                                            text_rect.centery = button['rect'].centery - 10
                                        else:
                                            text_rect.centery = button['rect'].centery + 10
                                        screen.blit(text_surface, text_rect)

                                pygame.draw.rect(screen, exit_button['color'], exit_button['rect'])
                                exit_text_surface = font.render(exit_button['text'], True, BLACK)
                                exit_text_rect = exit_text_surface.get_rect(center=exit_button['rect'].center)
                                screen.blit(exit_text_surface, exit_text_rect)
                                screen.blit(coins, (10, 35))
                                show_coins = font.render(f"{coins_number}", True, YELLOW)
                                screen.blit(show_coins, (25, 35))
                                screen.blit(mistress, (500, 250))
                                
                                screen.blit(dialogue, (250, 100))
                                
                                textwritten1 = tiny_font.render("可以提高自身生命上限，外挂", True, BLACK)
                                screen.blit(textwritten1, (335, 142))
                                textwritten2 = tiny_font.render("般的道具。需要购买吗？", True, BLACK)
                                screen.blit(textwritten2, (335, 162))
                                textwritten3 = tiny_font.render("售价：350", True, BLACK)
                                screen.blit(textwritten3, (335, 182))
                                screen.blit(yes, (480, 210))  # 确保 yes 图片已定义
                                screen.blit(no, (520, 210))  # 确保 no 图片已定义

                                pygame.display.flip()  # 更新屏幕显示

                                for event in pygame.event.get():  # 处理新的事件
                                    if event.type == pygame.QUIT:
                                        running = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = event.pos
                                        if (continue_area1[0] <= mouse_x <= continue_area1[0] + continue_area1[2] and
                                                continue_area1[1] <= mouse_y <= continue_area1[1] + continue_area1[3]):
                                            coins_number = coin_number.decrease_coin(350)  # 减少100金币
                                            health+=20
                                            buying = False
                                        elif (continue_area2[0] <= mouse_x <= continue_area2[0] + continue_area2[2] and
                                            continue_area2[1] <= mouse_y <= continue_area2[1] + continue_area2[3]):
                                            buying = False

                                if not buying:
                                    # 恢复主界面
                                    screen.blit(background_image, (0, 0))  # 绘制背景
                                    screen.blit(mistress, (500, 250))
                                    screen.blit(dialogue, (250, 100))
                                    textwritten = tiny_font.render("错过此家就没下家了哦！", True, BLACK)
                                    screen.blit(textwritten, (335, 142))
                                    screen.blit(coins, (10, 35))
                                    show_coins = font.render(f"{coins_number}", True, YELLOW)
                                    screen.blit(show_coins, (25, 35))
                                    pygame.display.flip()  # 更新屏幕显示
                                    break
                        if button['texts'][0] == "武器防御" and coins_number >= 150:
                            buying = True
                            while buying:
                                screen.blit(background_image, (0, 0))

                                shop_text_surface = font.render('商店', True, WHITE)
                                shop_text_rect = shop_text_surface.get_rect(topleft=(10, 10))
                                screen.blit(shop_text_surface, shop_text_rect)

                                for button in buttons:
                                    pygame.draw.rect(screen, button['color'], button['rect'])
                                    for i, text in enumerate(button['texts']):
                                        small_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)
                                        text_surface = small_font.render(text, True, BLACK)
                                        text_rect = text_surface.get_rect(center=button['rect'].center)
                                        if i == 0:
                                            text_rect.centery = button['rect'].centery - 10
                                        else:
                                            text_rect.centery = button['rect'].centery + 10
                                        screen.blit(text_surface, text_rect)

                                pygame.draw.rect(screen, exit_button['color'], exit_button['rect'])
                                exit_text_surface = font.render(exit_button['text'], True, BLACK)
                                exit_text_rect = exit_text_surface.get_rect(center=exit_button['rect'].center)
                                screen.blit(exit_text_surface, exit_text_rect)
                                screen.blit(coins, (10, 35))
                                show_coins = font.render(f"{coins_number}", True, YELLOW)
                                screen.blit(show_coins, (25, 35))
                                screen.blit(mistress, (500, 250))
                                
                                screen.blit(dialogue, (250, 100))
                                
                                textwritten1 = tiny_font.render("本游戏中的轻防具，可以有效防止", True, BLACK)
                                screen.blit(textwritten1, (335, 142))
                                textwritten2 = tiny_font.render("高强度的伤害。", True, BLACK)
                                screen.blit(textwritten2, (335, 162))
                                textwritten3 = tiny_font.render("售价：150", True, BLACK)
                                screen.blit(textwritten3, (335, 182))
                                screen.blit(yes, (480, 210))  # 确保 yes 图片已定义
                                screen.blit(no, (520, 210))  # 确保 no 图片已定义

                                pygame.display.flip()  # 更新屏幕显示

                                for event in pygame.event.get():  # 处理新的事件
                                    if event.type == pygame.QUIT:
                                        running = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = event.pos
                                        if (continue_area1[0] <= mouse_x <= continue_area1[0] + continue_area1[2] and
                                                continue_area1[1] <= mouse_y <= continue_area1[1] + continue_area1[3]):
                                            coins_number = coin_number.decrease_coin(150)  # 减少100金币
                                            defense+=5
                                            buying = False
                                        elif (continue_area2[0] <= mouse_x <= continue_area2[0] + continue_area2[2] and
                                            continue_area2[1] <= mouse_y <= continue_area2[1] + continue_area2[3]):
                                            buying = False

                                if not buying:
                                    # 恢复主界面
                                    screen.blit(background_image, (0, 0))  # 绘制背景
                                    screen.blit(mistress, (500, 250))
                                    screen.blit(dialogue, (250, 100))
                                    textwritten = tiny_font.render("错过此家就没下家了哦！", True, BLACK)
                                    screen.blit(textwritten, (335, 142))
                                    screen.blit(coins, (10, 35))
                                    show_coins = font.render(f"{coins_number}", True, YELLOW)
                                    screen.blit(show_coins, (25, 35))
                                    pygame.display.flip()  # 更新屏幕显示
                                    break
                        if button['texts'][0] == "重甲升级" and coins_number >= 350:
                            # print("run again")
                            buying = True
                            while buying:
                                screen.blit(background_image, (0, 0))

                                shop_text_surface = font.render('商店', True, WHITE)
                                shop_text_rect = shop_text_surface.get_rect(topleft=(10, 10))
                                screen.blit(shop_text_surface, shop_text_rect)

                                for button in buttons:
                                    pygame.draw.rect(screen, button['color'], button['rect'])
                                    for i, text in enumerate(button['texts']):
                                        small_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)
                                        text_surface = small_font.render(text, True, BLACK)
                                        text_rect = text_surface.get_rect(center=button['rect'].center)
                                        if i == 0:
                                            text_rect.centery = button['rect'].centery - 10
                                        else:
                                            text_rect.centery = button['rect'].centery + 10
                                        screen.blit(text_surface, text_rect)

                                pygame.draw.rect(screen, exit_button['color'], exit_button['rect'])
                                exit_text_surface = font.render(exit_button['text'], True, BLACK)
                                exit_text_rect = exit_text_surface.get_rect(center=exit_button['rect'].center)
                                screen.blit(exit_text_surface, exit_text_rect)
                                screen.blit(coins, (10, 35))
                                show_coins = font.render(f"{coins_number}", True, YELLOW)
                                screen.blit(show_coins, (25, 35))
                                screen.blit(mistress, (500, 250))
                                
                                screen.blit(dialogue, (250, 100))
                                
                                textwritten1 = tiny_font.render("重型装甲锻造，升级后一般的普攻", True, BLACK)
                                screen.blit(textwritten1, (335, 142))
                                textwritten2 = tiny_font.render("无法直接打到你，只有法穿才能伤", True, BLACK)
                                screen.blit(textwritten2, (335, 162))
                                textwritten3 = tiny_font.render("分毫，也正是因此不要大意被一波了！", True, BLACK)
                                screen.blit(textwritten3, (335, 182))
                                textwritten4 = tiny_font.render("售价：350", True, BLACK)
                                screen.blit(textwritten4, (335, 195))
                                screen.blit(yes, (480, 210))  # 确保 yes 图片已定义
                                screen.blit(no, (520, 210))  # 确保 no 图片已定义

                                pygame.display.flip()  # 更新屏幕显示

                                for event in pygame.event.get():  # 处理新的事件
                                    if event.type == pygame.QUIT:
                                        running = False
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_x, mouse_y = event.pos
                                        if (continue_area1[0] <= mouse_x <= continue_area1[0] + continue_area1[2] and
                                                continue_area1[1] <= mouse_y <= continue_area1[1] + continue_area1[3]):
                                            coins_number = coin_number.decrease_coin(350)  # 减少100金币
                                            defense+=10
                                            buying = False
                                        elif (continue_area2[0] <= mouse_x <= continue_area2[0] + continue_area2[2] and
                                            continue_area2[1] <= mouse_y <= continue_area2[1] + continue_area2[3]):
                                            buying = False

                                if not buying:
                                    # 恢复主界面
                                    screen.blit(background_image, (0, 0))  # 绘制背景
                                    screen.blit(mistress, (500, 250))
                                    screen.blit(dialogue, (250, 100))
                                    textwritten = tiny_font.render("错过此家就没下家了哦！", True, BLACK)
                                    screen.blit(textwritten, (335, 142))
                                    screen.blit(coins, (10, 35))
                                    show_coins = font.render(f"{coins_number}", True, YELLOW)
                                    screen.blit(show_coins, (25, 35))
                                    pygame.display.flip()  # 更新屏幕显示
                                    break
                       
                        print(f"Clicked {button['texts'][0]}")
                        print(coins_number)
                if exit_button['rect'].collidepoint(mouse_pos):
                    print(f"Clicked {exit_button['text']}")
                    running = False

        screen.blit(background_image, (0, 0))

        shop_text_surface = font.render('商店', True, WHITE)
        shop_text_rect = shop_text_surface.get_rect(topleft=(10, 10))
        screen.blit(shop_text_surface, shop_text_rect)

        for button in buttons:
            pygame.draw.rect(screen, button['color'], button['rect'])
            for i, text in enumerate(button['texts']):
                small_font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)
                text_surface = small_font.render(text, True, BLACK)
                text_rect = text_surface.get_rect(center=button['rect'].center)
                if i == 0:
                    text_rect.centery = button['rect'].centery - 10
                else:
                    text_rect.centery = button['rect'].centery + 10
                screen.blit(text_surface, text_rect)

        pygame.draw.rect(screen, exit_button['color'], exit_button['rect'])
        exit_text_surface = font.render(exit_button['text'], True, BLACK)
        exit_text_rect = exit_text_surface.get_rect(center=exit_button['rect'].center)
        screen.blit(exit_text_surface, exit_text_rect)

        screen.blit(mistress, (500, 250))
        screen.blit(dialogue, (250, 100))
        
        textwritten = tiny_font.render("错过此家就没下家了哦！", True, BLACK)
        screen.blit(textwritten, (335, 142))
        screen.blit(coins, (20, 35))
        show_coins = font.render(f":{coins_number}", True, YELLOW)
        screen.blit(show_coins, (45, 35))
        screen.blit(health_limit,(25,75))
        show_health=font.render(f":{health}",True,YELLOW)
        screen.blit(show_health,(55,75))
        show_defense=font.render(f"防御:{defense}",True,WHITE)
        screen.blit(show_defense,(35,105))
        show_attack=font.render(f"攻击:{attack}",True,WHITE)
        screen.blit(show_attack,(35,145))
        pygame.display.flip()
    return resurrect,health,attack,defense

