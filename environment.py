import pygame
import sys
import data_module
import storecode
import cv2
import setting
import coin_number
import ceshi
import random
def run_random():
    if random.random()<0.5:
        a=random.randint(50,600)
        b=random.randint(400,1100)
    elif random.random()<1:
        a=random.randint(400,1500)
        b=random.randint(50,450)
    return a,b
def box_place():
    testlist6=[]
    c,d=run_random()
    for e in range(c,c+51):
        for f in range(d,d+51):
            testlist6.append((e,f))
    return c,d,testlist6
def run_program():
    # 加载人物
    name="Kirito"
    health=100
    attack=20
    defense=5
    resurrect=0

    box_touch=True
    # 窗口大小

    pygame.init()
    screen=pygame.display.set_mode((data_module.width,data_module.height))

    # 引入时钟
    clock=pygame.time.Clock()

    # 内容加载区域#############################################################
    # 加载图片
    background=pygame.image.load('C:\\game\\picture\\yuana.png')
    background=pygame.transform.scale(background,(2*data_module.width,2*data_module.height))
    # print("背景图片加载成功")
    player=pygame.image.load('C:\\game\\picture\\yuanb.png')
    player=pygame.transform.scale(player,(65,65))
    # print("玩家图片加载成功")

    # 加载商店
    store=pygame.image.load('C:\\game\\picture\\yuanc.png')
    store=pygame.transform.scale(store,(100,100))
    # print("商店系统加载成功")

    # 加载金币
    coins=pygame.image.load('C:\\game\\picture\\coins.png')
    coins=pygame.transform.scale(coins,(30,30))

    # 加载字体
    try:
        font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)  # 指定中文字体文件
    except IOError:
        print("字体文件加载失败，请确保Uranus_Pixel_11Px.ttf文件在程序目录下")
        sys.exit()

    # 设置颜色
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    RED = (255, 0, 0)
    BROWN = (165, 42, 42)  # 棕色背景
    BLACK = (0, 0, 0)  # 定义黑色

    # 金币初始值
    coins_number = coin_number.get_coin()


    # 游戏内调整区域##########################################################
    # 获取坐标，第二行确保人物在中间
    player_rect=player.get_rect()
    player_rect.center=(data_module.width//2-25,data_module.height//2-25)


    # 获取坐标，确保商店在左下角
    store_rect=store.get_rect()
    store_rect.center=(data_module.width,data_module.height)

    # 范围检测
    testlist1=[]
    for a in range(735,811):
        for b in range(550,611):
            testlist1.append((a,b))
    testlist2=[]
    for a in range(1180,1261):
        for b in range(850,951):
            testlist2.append((a,b))
    testlist3=[]
    for a in range(210,281):
        for b in range(270,311):
            testlist3.append((a,b))
    testlist4=[]
    for a in range(1180,1261):
        for b in range(550,651):
            testlist4.append((a,b))
    testlist5=[]
    for a in range(800,851):
        for b in range(300,351):
            testlist5.append((a,b))
    number_run_store=0
    number_run_game=0
    running=True

    # 金币最初始数量为1000
    # 最初始数量为600
    coins_number=coin_number.get_coin()
    headfont = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 96)  # 指定中文字体文件
    gamefont = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 72)  # 指定中文字体文件
    # 开始做游戏封面
    scene1=pygame.image.load('C:\\game\\picture\\first.png')
    scene1=pygame.transform.scale(scene1,(data_module.width,data_module.height))
    yuanbb=pygame.image.load('C:\\game\\picture\\yuanbb.png')
    yuanbb=pygame.transform.scale(yuanbb,(350,300))
    alert=pygame.image.load('C:\\game\\picture\\alert.png')
    alert=pygame.transform.scale(alert,(60,60))
    npc=pygame.image.load('C:\\game\\picture\\npc.png')
    npc=pygame.transform.scale(npc,(300,200))
    npc_block=pygame.image.load('C:\\game\\picture\\npc_block.png')
    npc_block=pygame.transform.scale(npc_block,(60,60))
    asuna=pygame.image.load('C:\\game\\picture\\asuna.png')
    asuna=pygame.transform.scale(asuna,(60,60))
    asunabb=pygame.image.load('C:\\game\\picture\\asunabb.png')
    asunabb=pygame.transform.scale(asunabb,(160,300))
    firstbb=pygame.image.load('C:\\game\\picture\\firstbb.png')
    firstbb=pygame.transform.scale(firstbb,(300,200))
    chuansong=pygame.image.load('C:\\game\\picture\\chuansong.png')
    chuansong=pygame.transform.scale(chuansong,(100,100))
    health_limit=pygame.image.load('C:\\game\\picture\\health.png')
    health_limit=pygame.transform.scale(health_limit,(30,30))
    box_open=pygame.image.load('C:\\game\\picture\\box_open.png')
    box_open=pygame.transform.scale(box_open,(70,50))

    # 第一个画面的函数
    juqingo=True
    def scene_1():
        # 定义区域
        continue_area = (400,320,300,100)  # 继续区域的位置和大小
        exit_area = (400,420,300,100)      # 退出区域的位置和大小

        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    mouse_x, mouse_y = event.pos
                    if continue_area[0] <= mouse_x <= continue_area[0] + continue_area[2] and continue_area[1] <= mouse_y <= continue_area[1] + continue_area[3]:
                    # 执行继续程序的代码
                        return None
                    # 这里可以添加你的代码逻辑
                    elif exit_area[0] <= mouse_x <= exit_area[0] + exit_area[2] and exit_area[1] <= mouse_y <= exit_area[1] + exit_area[3]:
                        # 执行退出程序的代码
                        pygame.quit()
                        sys.exit()

            # 绘制第一个画面
            screen.blit(scene1,(0,0))
            screen.blit(firstbb,(20,310))
            # screen.blit(asunabb,(0,250))
            texthead = headfont.render("新艾恩葛朗特", True, BLACK)
            screen.blit(texthead, (140, 140))
            gamestart=gamefont.render("开始游戏",True,BLACK)
            screen.blit(gamestart, (400, 320))
            gameover=gamefont.render("退出程序",True,BLACK)
            screen.blit(gameover, (400, 420))
            pygame.display.flip()

    def scene_2():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            screen.blit(player,(data_module.width//2-20,data_module.height//2))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            pygame.display.flip()
    def scene_3():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            screen.blit(player,(data_module.width//2-20,data_module.height//2))
            screen.blit(npc_block,(data_module.width//3,data_module.height//2))
            screen.blit(alert,(data_module.width//2,data_module.height//2-60))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            pygame.display.flip()
    def scene_4():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            screen.blit(player,(data_module.width//2-20,data_module.height//2))
            screen.blit(yuanbb,(500,300))
            screen.blit(npc_block,(data_module.width//3,data_module.height//2))
            text1=font.render("这里是哪里？发生什么了？",True,WHITE)
            screen.blit(text1, (100, 400))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            pygame.display.flip()
    def scene_5():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None
            
            # 绘制第二个画面
            screen.blit(background, (0, 0))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))

            # 绘制NPC
            screen.blit(npc_block, (data_module.width // 3, data_module.height // 2))

            # 移动角色到NPC的位置
            target_x = data_module.width // 4 + player_rect.width // 2+43
            target_y = data_module.height // 2 + player_rect.height // 2-32

            # 确保角色不会移动过快
            move_step = data_module.speed

            # 向目标X坐标移动
            if player_rect.x < target_x:
                player_rect.x = min(player_rect.x + move_step, target_x)
            elif player_rect.x > target_x:
                player_rect.x = max(player_rect.x - move_step, target_x)

            # 向目标Y坐标移动
            if player_rect.y < target_y:
                player_rect.y = min(player_rect.y + move_step, target_y)
            elif player_rect.y > target_y:
                player_rect.y = max(player_rect.y - move_step, target_y)

            # 绘制角色
            screen.blit(player, player_rect)

            pygame.display.flip()
            pygame.time.Clock().tick(30)  # 控制帧率为30FPS

    def scene_6():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            screen.blit(npc_block,(data_module.width//3,data_module.height//2))
            screen.blit(player,(data_module.width//3+10,data_module.height//2))
            screen.blit(npc,(0,350))
            text1=font.render("爸爸！",True,WHITE)
            screen.blit(text1, (400, 400))
            pygame.display.flip()
    def scene_7():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            screen.blit(npc_block,(data_module.width//3,data_module.height//2))
            screen.blit(player,(data_module.width//3+10,data_module.height//2))
            screen.blit(yuanbb,(500,300))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            
            text1=font.render("结衣，你怎么在这里？",True,WHITE)
            screen.blit(text1, (100, 400))
            pygame.display.flip()
    def scene_8():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            screen.blit(npc_block,(data_module.width//3,data_module.height//2))
            screen.blit(player,(data_module.width//3+10,data_module.height//2))
            screen.blit(npc,(0,350))
            text1=font.render("呜呜呜，妈妈又被茅场晶彦抓走了！怎么办？",True,WHITE)
            screen.blit(text1, (400, 400))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            pygame.display.flip()
    def scene_9():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            screen.blit(npc_block,(data_module.width//3,data_module.height//2))
            screen.blit(player,(data_module.width//3+10,data_module.height//2))
            screen.blit(yuanbb,(500,300))
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            text1=font.render("他到底想干什么？",True,WHITE)
            screen.blit(text1, (100, 400))
            pygame.display.flip()
    def scene_10():
        while juqingo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 检测到鼠标点击，跳转到下一个画面
                    return None

            # 绘制第二个画面
            screen.blit(background,(0,0))
            screen.blit(npc_block,(data_module.width//3,data_module.height//2))
            screen.blit(player,(data_module.width//3+10,data_module.height//2))
            screen.blit(npc,(-20,350))
            text1=font.render("爸爸，如果你有什么不清楚的可以问我，",True,WHITE)
            screen.blit(text1, (300, 400))
            text2=font.render("我可以感知到他们的方向，妈妈现在向东去了！",True,WHITE)
            screen.blit(text2, (300, 430))
            text3=font.render("我们可以先去商店买些东西，或许可以得到",True,WHITE)
            text4=font.render("一些帮助.",True,WHITE)
            click_to_continue=gamefont.render("click to continue",True,WHITE)
            screen.blit(click_to_continue, (200, 100))
            screen.blit(text3, (300, 460))
            screen.blit(text4, (300, 490))
            pygame.display.flip()
    scene_1()
    scene_2()
    scene_3()
    scene_4()
    player_rect.center=(data_module.width//2-20,data_module.height//2+25)
    scene_5()
    scene_6()
    scene_7()
    scene_8()
    scene_9()
    scene_10()
    number_guan=1
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        # 按键时一定要英文模式，不然按不了，这里是检测按键
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and player_rect.y>=0:
            player_rect.y -= data_module.speed
        if keys[pygame.K_s] and player_rect.y<=2*data_module.height-65:
            player_rect.y += data_module.speed
        if keys[pygame.K_a] and player_rect.x>=0:
            player_rect.x -= data_module.speed
        if keys[pygame.K_d] and player_rect.x<=2*data_module.width-65:
            player_rect.x += data_module.speed
        # 计算摄像机位置
        camera_x = player_rect.x - data_module.width//2
        camera_y = player_rect.y - data_module.height//2

        # 限制摄像机位置，防止超出游戏世界边界
        camera_x = max(0, min(camera_x, data_module.width))
        camera_y = max(0, min(camera_y, data_module.height))

        # 应用摄像机偏移
        screen.blit(background, (-camera_x, -camera_y))

        # 一定注意由于我有个变量store，不能再有个store的module，不然分不清
        screen.blit(store,(store_rect.x - camera_x, store_rect.y - camera_y))
        if (player_rect.x,player_rect.y) in testlist1:
            resurrect,health,attack,defense=storecode.run_store(resurrect,health,attack,defense)
            number_run_store+=1
            screen=pygame.display.set_mode((data_module.width,data_module.height))
            player_rect.center=(720,520)
            screen.blit(background, (-camera_x, -camera_y))
            screen.blit(store,(store_rect.x - camera_x, store_rect.y - camera_y))
            screen.blit(chuansong,(data_module.width*1.5-camera_x,data_module.height*1.5-camera_y))
        # 这行是总展示，放在末尾ds
        if (player_rect.x,player_rect.y) in testlist2:
            if number_guan==1:
                resurrect,number_guan = setting.fight1(screen,data_module.width,data_module.height,health,attack,defense,resurrect,number_guan)
                # print(resurrect)
                coins_number=coin_number.increase_coin(500)
                number_run_game+=1
                screen=pygame.display.set_mode((data_module.width,data_module.height))
                player_rect.center=(1140,800)
                screen.blit(background, (-camera_x, -camera_y))
                screen.blit(store,(store_rect.x - camera_x, store_rect.y - camera_y))
                screen.blit(chuansong,(data_module.width*1.5-camera_x,data_module.height*1.5-camera_y))
            elif number_guan==2:
                resurrect,number_guan = setting.fight2(screen,data_module.width,data_module.height,health,attack,defense,resurrect,number_guan)
                print(resurrect)
                coins_number=coin_number.increase_coin(500)
                number_run_game+=1
                screen=pygame.display.set_mode((data_module.width,data_module.height))
                player_rect.center=(1140,800)
                screen.blit(background, (-camera_x, -camera_y))
                screen.blit(store,(store_rect.x - camera_x, store_rect.y - camera_y))
                screen.blit(chuansong,(data_module.width*1.5-camera_x,data_module.height*1.5-camera_y))
            elif number_guan==3:
                resurrect,number_guan = setting.fight3(screen,data_module.width,data_module.height,health,attack,defense,resurrect,number_guan)
                cap = cv2.VideoCapture("C:\\game\\picture\\ending.mp4")
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break   
                    resized_frame = cv2.resize(frame,(800,600))
                    cv2.imshow("Risized Video", resized_frame)
                    if cv2.waitKey(1) & 0xFF == ord(' '):
                        break
                cap.release()
                cv2.destroyAllWindows()
                exit()
        if (player_rect.x,player_rect.y) in testlist4:
            resurrect,none = setting.fight1(screen,data_module.width,data_module.height,health,attack,defense,resurrect,number_guan)
            screen=pygame.display.set_mode((data_module.width,data_module.height))
            coins_number=coin_number.increase_coin(500)
            player_rect.center=(1140,550)

            screen.blit(background, (-camera_x, -camera_y))
            screen.blit(store,(store_rect.x - camera_x, store_rect.y - camera_y))
            screen.blit(chuansong,(data_module.width*1.5-camera_x,data_module.height*1.5-camera_y))
        # 这行是总展示，放在末尾
        # if (player_rect.x,player_rect.y) in testlist5:
        if (player_rect.x,player_rect.y) in testlist3:
            if number_run_game==0 and number_run_store==0:
                screen.blit(npc,data_module.youki)
                text1=font.render("我们可以先去商店购买一些东西来",True,WHITE)
                screen.blit(text1,data_module.textyouki1)
                text2=font.render("增加我们的攻击力",True,WHITE)
                screen.blit(text2,data_module.textyouki2)
            elif number_run_game==0 and number_run_store==1:
                screen.blit(npc,data_module.youki)
                text1=font.render("现在我们有了强力的武器，可以去",True,WHITE)
                screen.blit(text1,data_module.textyouki1)
                text2=font.render("打第一关了！",True,WHITE)
                screen.blit(text2,data_module.textyouki2)
            elif number_run_game==1 and number_run_store==1:
                screen.blit(npc,data_module.youki)
                text1=font.render("对于第二关来讲，我们手中的武器",True,WHITE)
                screen.blit(text1,data_module.textyouki1)
                text2=font.render("攻击或许不够，可以去买更强力的",True,WHITE)
                screen.blit(text2,data_module.textyouki2)
                text3=font.render("武器！",True,WHITE)
                screen.blit(text3,data_module.textyouki3)
            elif number_run_game==1 and number_run_store==2:
                screen.blit(npc,data_module.youki)
                text1=font.render("现在我们有了更强力的武器，可以",True,WHITE)
                screen.blit(text1,data_module.textyouki1)
                text2=font.render("去打第二关了！",True,WHITE)
                screen.blit(text2,data_module.textyouki2)
            else:
                ceshi.run_ai()
                screen=pygame.display.set_mode((data_module.width,data_module.height))
                player_rect.center=(data_module.width // 3+30, data_module.height // 2)
        # 展示一下interactive object
        if box_touch:
            j,k,l=box_place()
            # print(j,k,l)
            box_touch=not box_touch
        screen.blit(box_open,(j-camera_x,k-camera_y))
        if (player_rect.x,player_rect.y) in l:
            coins_number=coin_number.increase_coin(20)
            box_touch=not box_touch
        
        
        # 绘制玩家
        screen.blit(player, (player_rect.x-camera_x, player_rect.y-camera_y ))
        # 绘制金币d
        coins_x=max(10,min(player_rect.x-camera_x-data_module.width//2,data_module.width-camera_x+10))
        coins_y=max(10,min(player_rect.y-camera_y-data_module.height//2,data_module.height-camera_y+10))
        screen.blit(coins,(coins_x,coins_y))

        # 这边还要加一个金币数量增加的小程序

        coins_number = coin_number.get_coin()

        
        show_coins=font.render(f":{coins_number}",True,YELLOW)
        screen.blit(show_coins,(coins_x+30,coins_y))
        screen.blit(health_limit,(coins_x,coins_y+50))
        show_health=font.render(f":{health}",True,YELLOW)
        screen.blit(show_health,(coins_x+30,coins_y+50))
        show_defense=font.render(f"防御:{defense}",True,WHITE)
        screen.blit(show_defense,(coins_x+10,coins_y+80))
        show_attack=font.render(f"攻击:{attack}",True,WHITE)
        screen.blit(show_attack,(coins_x+10,coins_y+110))
        # 展示NPC
        screen.blit(npc_block, (data_module.width // 3-camera_x, data_module.height // 2-camera_y))
        screen.blit(alert,(data_module.width//3-camera_x,data_module.height//2-60-camera_y))

        # 展示战斗地点
        screen.blit(chuansong,(data_module.width*1.5-camera_x,data_module.height*1.5-camera_y))
        screen.blit(chuansong,(data_module.width*1.5-camera_x,data_module.height-camera_y))

        # 这里是打小怪传送门的字体显示
        text1=font.render("金币关入口",True,WHITE)
        screen.blit(text1,((data_module.width*1.5-camera_x,data_module.height-camera_y-20)))
        text2=font.render("主线关卡入口",True,WHITE)
        screen.blit(text2,(data_module.width*1.5-camera_x,data_module.height*1.5-camera_y-20))
        # 显示金币数量
        # 这行是总展示，放在末尾
        pygame.display.flip()
        clock.tick(data_module.fps)

    pygame.quit()
    sys.exit()
