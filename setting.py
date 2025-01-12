import pygame
#Character(图片，旋转，大小，位置，字体，名字，位置,颜色默认白色,大小,血量,血量上限，位置,攻击，防御，窗口)
class Character():
    def __init__(self,png,a1,b1,x1,y1,ttf,name,x2,y2,b2,hp,hp_max,x3,y3,akt,defence,window):
        self.png = png
        self.a1 = a1
        self.b1 = b1
        self.x1 = x1
        self.y1 = y1
        self.ttf = ttf
        self.name = name 
        self.x2 = x2
        self.y2 = y2
        self.b2 = b2
        self.hp = hp
        self.hp_max = hp_max
        self.x3 = x3
        self.y3 = y3
        self.akt = akt
        self.defence = defence
        self.window = window
    def Character(self,draw):
        character = pygame.image.load(self.png)
        character_new = pygame.transform.rotozoom(character,self.a1,self.b1)
        character_w,character_h = character_new.get_size()
        text = pygame.font.Font(self.ttf,20)
        character_name = text.render(self.name,True,(0,0,255))
        new_name = pygame.transform.rotozoom(character_name,0,self.b2)
        HP = text.render(f'HP{self.hp}/{self.hp_max}',True,(200,0,0))
        new_HP = pygame.transform.rotozoom(HP,0,self.b2)
        if draw == True:
            self.window.blit(new_name,(self.x2 + character_w/3,self.y2 - character_h/2 + 10))
            self.window.blit(character_new,(self.x1,self.y1 - character_h/2)) 
            self.window.blit(new_HP,(self.x3 + character_w/3,self.y3 + character_h/2))
        pygame.display.update()
        return [new_HP,self.x3 + character_w/3,self.y3 + character_h/2]
    def choice(self):
        character = pygame.image.load(self.png)
        character_new = pygame.transform.rotozoom(character,self.a1,self.b1)
        character_w,character_h = character_new.get_size()
        return [character_w,character_h]



#Button(字体,位置，按钮大小，按钮颜色，按钮内容,字体默认白色,窗口）
class Button:
    def __init__(self,ttf,x,y,w,h,r,g,b,word,window):
        self.ttf = ttf
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.g = g
        self.b = b
        self.word = word
        self.window = window
    def Button(self):
        text = pygame.font.Font(self.ttf,30)
        pygame.draw.rect(self.window,(self.r,self.g,self.b),(self.x,self.y,self.w,self.h))
        button = text.render(self.word,True,(255,255,255))
        tw1,th1 = button.get_size()
        tx1 = self.x + self.w/2 - tw1/2
        ty1 = self.y + self.h/2 - th1/2
        self.window.blit(button,(tx1,ty1))
        pygame.display.update()
        return button,tx1,ty1
def rewrite(window,background,x,y,w2,h2,something):
    w1,h1=something.get_size()
    window.blit(background.subsurface(pygame.Rect(x,y,w1+w2,h1+h2)),(x,y))
    window.blit(something,(x,y))
    pygame.display.update()





#=====================================战斗==================================
#===========================================================================小怪战====================================================================================
def fight1(window,win_width,win_height,health,attack,defense,resurrect,number_guan):
    pygame.mixer.music.load('C:\\game\\picture\\fight_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('head')
    back = pygame.image.load("C:\\game\\picture\\background.png")
    background = pygame.transform.scale(back,(800,600))
    window.blit(background,(0,0))
    pygame.display.flip()
    #=================角色==================
    #Character(图片，旋转，大小，位置，字体，名字，位置,颜色默认白色,大小,血量,血量上限，位置,窗口)
    #主角
    HP = health
    character =Character('C:\\game\\picture\\character.png',0,0.4,win_width/10,win_height*2/7 + 50,'C:\\game\\Uranus_Pixel_11Px.ttf','name',win_width/10,win_height/5 + 50,1,HP,health,win_width/10 - 30,win_height*2/7 + 50,attack,defense,window)
    character.Character(True)

    #Button(字体,位置，按钮大小，按钮颜色，按钮内容,字体默认白色，）
    #技能
    attack1 = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5,100,50,200,0,0,'攻击',window)
    attack_word,attack_x,attack_y = attack1.Button()
    fire = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5 + 55,100,50,0,0,200,'火球',window)
    fire_word,fire_x,fire_y = fire.Button()
    recover = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5 + 110,100,50,0,200,0,'恢复',window) 
    recover_word,recover_x,recover_y = recover.Button() 

    #小怪
    enermy1 = Character('C:\\game\\picture\\enermy.png',0,0.1,win_width*7/10,win_height*3/10,'C:\\game\\Uranus_Pixel_11Px.ttf','enemy1',win_width*7/10-20,win_height*3/10 - 35,1,50,50,win_width*7/10-20,win_height*3/10,10,5,window)
    enermy1.Character(True)
    enermy2 = Character('C:\\game\\picture\\enermy.png',0,0.1,win_width*7/10,win_height*4/5,'C:\\game\\Uranus_Pixel_11Px.ttf','enemy2',win_width*7/10-20,win_height*4/5 - 35,1,50,50,win_width*7/10-20,win_height*4/5,10,5,window)
    enermy2.Character(True)
    akt_enermys = [enermy1,enermy2]
    akt_enermy_num = 0
    akt_enermy = akt_enermys[akt_enermy_num]
    enermy1_pos = [win_width/2,0,win_width/2,win_height/2] 
    enermy2_pos = [win_width/2,win_height/2,win_width/2,win_height/2]
    pos_enermys = [enermy1_pos,enermy2_pos]




    def injure(akt_enermys,resurrect):
        for i in akt_enermys:
            pygame.time.wait(500)
            window.blit(background.subsurface(pygame.Rect(i.x1,i.y1 - i.choice()[1]/2,i.choice()[0],i.choice()[1])),(i.x1,i.y1 - i.choice()[1]/2))
            act_injure = pygame.image.load(i.png)
            act_injure1 = pygame.transform.rotozoom(act_injure,i.a1,i.b1)
            window.blit(act_injure1,(i.x1 - 20,i.y1 - i.choice()[1]/2))
            pygame.display.update()
            pygame.time.wait(100)
            window.blit(background.subsurface(pygame.Rect(i.x1 - 20,i.y1 - i.choice()[1]/2,i.choice()[0],i.choice()[1])),(i.x1 - 20,i.y1 - i.choice()[1]/2))
            window.blit(act_injure1,(i.x1,i.y1 - i.choice()[1]/2))
            pygame.display.update()
            pygame.time.wait(200)
            window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
            act_injured = pygame.image.load(character.png)
            act_injured1 = pygame.transform.rotozoom(act_injured,character.a1,character.b1)
            window.blit(act_injured1,(character.x1 - 20,character.y1 - character.choice()[1]/2))
            pygame.display.update()
            pygame.time.wait(100)
            window.blit(background.subsurface(pygame.Rect(character.x1 - 20,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1 - 20,character.y1 - character.choice()[1]/2))
            window.blit(act_injured1,(character.x1,character.y1 - character.choice()[1]/2))
            pygame.display.update()
            character.hp -= max(i.akt - character.defence,0)
            character_hp = character.Character(False)
            rewrite(window,background,character_hp[1],character_hp[2],50,0,character_hp[0])
            if character.hp <= 0:
                window.fill((0,0,0))
                die_text = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf',20)
                die = die_text.render('You Dead...',True,(155,0,0))
                window.blit(die,(win_width*2/5,win_height/2)) 
                pygame.display.update()
                pygame.time.wait(2000)
                if resurrect > 0:
                    resurrect -= 1
                    break
                elif resurrect == 0:
                    exit()
        return resurrect
    while character.hp > 0 and akt_enermys != []: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = event.pos
                attackTF = False
                fireTF = False
                recoverTF = False
                #========确定技能============
                if  attack1.x <= mx <= attack1.x + attack1.w:
                    if attack1.y <= my <= attack1.y + attack1.h:
                        pygame.draw.rect(window,(100,100,100),(attack1.x,attack1.y,attack1.w,attack1.h))
                        window.blit(attack_word,(attack_x,attack_y))
                        pygame.display.update()
                        attackTF = True
                    elif fire.y <= my <= fire.y + fire.h:
                        pygame.draw.rect(window,(100,100,100),(fire.x,fire.y,fire.w,fire.h))
                        window.blit(fire_word,(fire_x,fire_y))
                        pygame.display.update()
                        fireTF = True
                    elif recover.y <= my <= recover.y + recover.h:
                        pygame.draw.rect(window,(100,100,100),(recover.x,recover.y,recover.w,recover.h))
                        window.blit(recover_word,(recover_x,recover_y))
                        pygame.display.update()  
                        recoverTF = True
                    else:
                        attackTF = False
                        fireTF = False
                        recoverTF = False
                #=============选定攻击对象=======================
                if enermy1.hp > 0:
                    if enermy1.x1 <= mx <= enermy1.x1 + enermy1.choice()[0] and enermy1.y1 - enermy1.choice()[1]/2 <= my <= enermy1.y1 + enermy1.choice()[1]/2:
                        akt_enermy_num = 0
                if enermy2.hp > 0:        
                    if enermy2.x1 <= mx <= enermy2.x1 + enermy2.choice()[0] and enermy2.y1 - enermy1.choice()[1]/2 <= my <= enermy2.y1 + enermy2.choice()[1]/2:
                        akt_enermy_num = -1
            #==========技能结算================
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(window,(200,0,0),(attack1.x,attack1.y,attack1.w,attack1.h))
                window.blit(attack_word,(attack_x,attack_y))
                pygame.draw.rect(window,(0,0,200),(fire.x,fire.y,fire.w,fire.h))
                window.blit(fire_word,(fire_x,fire_y))
                pygame.draw.rect(window,(0,200,0),(recover.x,recover.y,recover.w,recover.h))
                window.blit(recover_word,(recover_x,recover_y))
                pygame.display.update()
                mx,my = event.pos
                if  attack1.x <= mx <= attack1.x + attack1.w:
                    if attack1.y <= my <= attack1.y + attack1.h and attackTF == True:
                        akt_enermy = akt_enermys[akt_enermy_num]
                        akt_enermy.hp -= max(character.akt - akt_enermy.defence,0)
                        enermy_hp = akt_enermy.Character(False)
                        rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                        act_akt = pygame.image.load('C:\\game\\picture\\attakt.png')
                        act_akt1 = pygame.transform.scale(act_akt,(80,220))
                        window.blit(act_akt1,(win_width/10 + 190,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 190,win_height*2/7 - 50,80,220)),(win_width/10 + 190,win_height*2/7 - 50))
                        window.blit(background.subsurface(pygame.Rect(akt_enermy.x1,akt_enermy.y1 - akt_enermy.choice()[1]/2,akt_enermy.choice()[0],akt_enermy.choice()[1])),(akt_enermy.x1,akt_enermy.y1 - akt_enermy.choice()[1]/2))
                        act_attacked = pygame.image.load(akt_enermy.png)
                        act_attacked1 = pygame.transform.rotozoom(act_attacked,0,0.1)
                        window.blit(act_attacked1,(akt_enermy.x1 + 20,akt_enermy.y1 - akt_enermy.choice()[1]/2))
                        pygame.display.update()
                        pygame.time.wait(100)
                        window.blit(background.subsurface(pygame.Rect(akt_enermy.x1 + 20,akt_enermy.y1 - akt_enermy.choice()[1]/2,akt_enermy.choice()[0],akt_enermy.choice()[1])),(akt_enermy.x1 + 20,akt_enermy.y1 - akt_enermy.choice()[1]/2))
                        window.blit(act_attacked1,(akt_enermy.x1,akt_enermy.y1 - akt_enermy.choice()[1]/2))
                        pygame.display.update()
                        if akt_enermy.hp <= 0:
                            window.blit(background.subsurface(pygame.Rect(pos_enermys[akt_enermy_num][0],pos_enermys[akt_enermy_num][1],pos_enermys[akt_enermy_num][2],pos_enermys[akt_enermy_num][3])),(pos_enermys[akt_enermy_num][0],pos_enermys[akt_enermy_num][1]))
                            pygame.display.update()
                            del akt_enermys[akt_enermy_num]
                            akt_enermy_num == 0
                        resurrect = injure(akt_enermys,resurrect)
                    if fire.y <= my <= fire.y + fire.h and fireTF == True:
                        new_akt_enermys = []
                        act_fire = pygame.image.load('C:\\game\\picture\\fire.png')
                        act_fire1 = pygame.transform.scale(act_fire,(230,200))
                        window.blit(act_fire1,(win_width/10 + 190,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(200)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 190,win_height*2/7 - 50,230,200)),(win_width/10 + 190,win_height*2/7 - 50))
                        window.blit(act_fire1,(win_width/10 + 240,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 240,win_height*2/7 - 50,230,200)),(win_width/10 + 240,win_height*2/7 - 50))
                        pygame.display.update()
                        for i in akt_enermys:
                            act_fire_enermy = pygame.image.load('C:\\game\\picture\\fire_enermy.png')
                            act_fire1_enermy = pygame.transform.scale(act_fire_enermy,(i.choice()[0],i.choice()[1]))
                            window.blit(act_fire1_enermy,(i.x1,i.y1 - i.choice()[1]/2))
                            pygame.display.update()
                            pygame.time.wait(300)
                            window.blit(background.subsurface(pygame.Rect(i.x1,i.y1 - i.choice()[1]/2,i.choice()[0],i.choice()[1])),(i.x1,i.y1 - i.choice()[1]/2))
                            act_fired = pygame.image.load(i.png)
                            act_fired1 = pygame.transform.rotozoom(act_fired,i.a1,i.b1)
                            window.blit(act_fired1,(i.x1,i.y1 - i.choice()[1]/2))
                            pygame.display.update()
                            i.hp -= character.akt/2
                            i.hp = int(i.hp)
                            enermy_hp = i.Character(False)
                            rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                            if i.hp > 0:
                                new_akt_enermys.append(i)
                            if i.hp <= 0:
                                window.blit(background.subsurface(pygame.Rect(pos_enermys[akt_enermys.index(i)][0],pos_enermys[akt_enermys.index(i)][1],pos_enermys[akt_enermys.index(i)][2],pos_enermys[akt_enermys.index(i)][3])),(pos_enermys[akt_enermys.index(i)][0],pos_enermys[akt_enermys.index(i)][1]))
                                pygame.display.update()
                                akt_enermy_num = 0
                        akt_enermys = new_akt_enermys
                        resurrect = injure(akt_enermys,resurrect)
                    if recover.y <= my <= recover.y + recover.h and recoverTF == True:
                        act_recover1 = pygame.image.load('C:\\game\\picture\\recover1.png')
                        act_recover2 = pygame.image.load('C:\\game\\picture\\recover2.png')
                        act_recover_new1 = pygame.transform.scale(act_recover1,(character.choice()[0],character.choice()[1]))
                        act_recover_new2 = pygame.transform.scale(act_recover2,(character.choice()[0],character.choice()[1]))                        
                        window.blit(act_recover_new1,(character.x1,character.y1 - character.choice()[1]/2))
                        window.blit(act_recover_new2,(character.x1,character.y1 - character.choice()[1]/2))                        
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
                        act_recovered = pygame.image.load(character.png)
                        act_recovered1 = pygame.transform.rotozoom(act_recovered,character.a1,character.b1)
                        window.blit(act_recovered1,(character.x1,character.y1 - character.choice()[1]/2))
                        pygame.display.update()
                        character.hp += character.akt*2
                        if character.hp >= character.hp_max:
                            character.hp = character.hp_max
                        character_hp = character.Character(False)
                        rewrite(window,background,character_hp[1],character_hp[2],50,0,character_hp[0])
                        resurrect = injure(akt_enermys,resurrect)
            if event.type == pygame.QUIT:
                exit()
        if akt_enermys == []:
            window.fill((255,255,255))
            win_text = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf',20)
            win = win_text.render('You Win!',True,(155,0,0))
            window.blit(win,(win_width*2/5,win_height/2)) 
            pygame.display.update()
            pygame.time.wait(2000)
            number_guan += 1
    pygame.mixer.music.pause()
    return resurrect,number_guan
#==================================================================================精英关===================================================
def fight2(window,win_width,win_height,health,attack,defense,resurrect,number_guan):
    pygame.mixer.music.load('C:\\game\\picture\\fight_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('head')
    back = pygame.image.load("C:\\game\\picture\\background.png")
    background = pygame.transform.scale(back,(800,600))
    window.blit(background,(0,0))
    pygame.display.flip()
    fight_rounds = 1

    #=================角色==================
    #Character(图片，旋转，大小，位置，字体，名字，位置,颜色默认白色,大小,血量,血量上限，位置,窗口)
    #主角
    HP = health
    character =Character('C:\\game\\picture\\character.png',0,0.4,win_width/10,win_height*2/7 + 50,'C:\\game\\Uranus_Pixel_11Px.ttf','name',win_width/10,win_height/5 + 50,1,HP,health,win_width/10 - 30,win_height*2/7 + 50,attack,defense,window)
    character.Character(True)
   
    #Button(字体,位置，按钮大小，按钮颜色，按钮内容,字体默认白色，）
    #技能
    attack1 = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5,100,50,200,0,0,'攻击',window)
    attack_word,attack_x,attack_y = attack1.Button()
    fire = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5 + 55,100,50,0,0,200,'火球',window)
    fire_word,fire_x,fire_y = fire.Button()
    recover = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5 + 110,100,50,0,200,0,'恢复',window) 
    recover_word,recover_x,recover_y = recover.Button() 

    #精英怪
    elite_enermy = Character('C:\\game\\picture\\elite_enermy.png',0,0.3,win_width*6/10,win_height/2,'C:\\game\\Uranus_Pixel_11Px.ttf','elite_enemy',win_width*6/10-20,win_height/2 - 35,1.4,50,50,win_width*6/10-20,win_height/2,15,10,window)
    elite_enermy.Character(True)
    elite_enermy_pos = [win_width/2,0,win_width/2,win_height] 
    HP_rounds = 1

    def injure(elite_enermy,fight_rounds,resurrect):
        if elite_enermy.hp > 0:
            pygame.time.wait(500)
            window.blit(background.subsurface(pygame.Rect(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2,elite_enermy.choice()[0],elite_enermy.choice()[1])),(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
            act_injure = pygame.image.load(elite_enermy.png)
            act_injure1 = pygame.transform.rotozoom(act_injure,elite_enermy.a1,elite_enermy.b1)
            window.blit(act_injure1,(elite_enermy.x1 - 20,elite_enermy.y1 - elite_enermy.choice()[1]/2))
            pygame.display.update()
            pygame.time.wait(100)
            window.blit(background.subsurface(pygame.Rect(elite_enermy.x1 - 20,elite_enermy.y1 - elite_enermy.choice()[1]/2,elite_enermy.choice()[0],elite_enermy.choice()[1])),(elite_enermy.x1 - 20,elite_enermy.y1 - elite_enermy.choice()[1]/2))
            window.blit(act_injure1,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
            pygame.display.update()
            pygame.time.wait(200)
            if fight_rounds % 4 != 0:
                window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
                act_injured = pygame.image.load(character.png)
                act_injured1 = pygame.transform.rotozoom(act_injured,character.a1,character.b1)
                window.blit(act_injured1,(character.x1 - 20,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                pygame.time.wait(100)
                window.blit(background.subsurface(pygame.Rect(character.x1 - 20,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1 - 20,character.y1 - character.choice()[1]/2))
                window.blit(act_injured1,(character.x1,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                character.hp -= max(elite_enermy.akt - character.defence,0)
            elif fight_rounds % 4 == 0:
                act_elite_injured = pygame.image.load('C:\\game\\picture\\act_elite_attact.png')
                act_elite_injured1 = pygame.transform.scale(act_elite_injured,(character.choice()[0],character.choice()[1]))
                window.blit(act_elite_injured1,(character.x1,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                pygame.time.wait(500)
                window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
                act_injured = pygame.image.load(character.png)
                act_injured1 = pygame.transform.rotozoom(act_injured,character.a1,character.b1)
                window.blit(act_injured1,(character.x1 - 20,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                pygame.time.wait(200)
                window.blit(background.subsurface(pygame.Rect(character.x1 - 20,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1 - 20,character.y1 - character.choice()[1]/2))
                window.blit(act_injured1,(character.x1,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                character.hp -= elite_enermy.akt * 2
                character.hp = int(character.hp)
            character_hp = character.Character(False)
            rewrite(window,background,character_hp[1],character_hp[2],50,0,character_hp[0])
            if character.hp <= 0:
                window.fill((0,0,0))
                die_text = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf',20)
                die = die_text.render('You Dead...',True,(155,0,0))
                window.blit(die,(win_width*2/5,win_height/2)) 
                pygame.display.update()
                pygame.time.wait(2000)
                if resurrect > 0:
                    resurrect -= 1
                elif resurrect == 0:
                    exit()
        return resurrect
 
    while character.hp > 0 and elite_enermy.hp > 0  : 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = event.pos
                attackTF = False
                fireTF = False
                recoverTF = False
                #========确定技能============
                if  attack1.x <= mx <= attack1.x + attack1.w:
                    if attack1.y <= my <= attack1.y + attack1.h:
                        pygame.draw.rect(window,(100,100,100),(attack1.x,attack1.y,attack1.w,attack1.h))
                        window.blit(attack_word,(attack_x,attack_y))
                        pygame.display.update()
                        attackTF = True
                    elif fire.y <= my <= fire.y + fire.h:
                        pygame.draw.rect(window,(100,100,100),(fire.x,fire.y,fire.w,fire.h))
                        window.blit(fire_word,(fire_x,fire_y))
                        pygame.display.update()
                        fireTF = True
                    elif recover.y <= my <= recover.y + recover.h:
                        pygame.draw.rect(window,(100,100,100),(recover.x,recover.y,recover.w,recover.h))
                        window.blit(recover_word,(recover_x,recover_y))
                        pygame.display.update()  
                        recoverTF = True
                    else:
                        attackTF = False
                        fireTF = False
                        recoverTF = False
            #==========技能结算================
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(window,(200,0,0),(attack1.x,attack1.y,attack1.w,attack1.h))
                window.blit(attack_word,(attack_x,attack_y))
                pygame.draw.rect(window,(0,0,200),(fire.x,fire.y,fire.w,fire.h))
                window.blit(fire_word,(fire_x,fire_y))
                pygame.draw.rect(window,(0,200,0),(recover.x,recover.y,recover.w,recover.h))
                window.blit(recover_word,(recover_x,recover_y))
                pygame.display.update()
                mx,my = event.pos
                if  attack1.x <= mx <= attack1.x + attack1.w:
                    if attack1.y <= my <= attack1.y + attack1.h and attackTF == True:
                        elite_enermy.hp -= max(character.akt - elite_enermy.defence,0)
                        enermy_hp = elite_enermy.Character(False)
                        rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                        act_akt = pygame.image.load('C:\\game\\picture\\attakt.png')
                        act_akt1 = pygame.transform.scale(act_akt,(80,220))
                        window.blit(act_akt1,(win_width/10 + 190,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 190,win_height*2/7 - 50,80,220)),(win_width/10 + 190,win_height*2/7 - 50))
                        window.blit(background.subsurface(pygame.Rect(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2,elite_enermy.choice()[0],elite_enermy.choice()[1])),(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                        act_attacked = pygame.image.load(elite_enermy.png)
                        act_attacked1 = pygame.transform.rotozoom(act_attacked,elite_enermy.a1,elite_enermy.b1)
                        window.blit(act_attacked1,(elite_enermy.x1 + 20,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                        pygame.display.update()
                        pygame.time.wait(100)
                        window.blit(background.subsurface(pygame.Rect(elite_enermy.x1 + 20,elite_enermy.y1 - elite_enermy.choice()[1]/2,elite_enermy.choice()[0],elite_enermy.choice()[1])),(elite_enermy.x1 + 20,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                        window.blit(act_attacked1,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                        pygame.display.update()
                        if elite_enermy.hp <= 0:
                            if HP_rounds > 0:
                                act_resurrect1 = pygame.image.load('C:\\game\\picture\\resurrect1.png')
                                act_resurrect11 = pygame.transform.scale(act_resurrect1,(elite_enermy.choice()[0],elite_enermy.choice()[1]))
                                window.blit(act_resurrect11,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(300)
                                act_resurrect2 = pygame.image.load('C:\\game\\picture\\resurrect2.png')
                                act_resurrect21 = pygame.transform.scale(act_resurrect2,(elite_enermy.choice()[0],elite_enermy.choice()[1]))
                                window.blit(act_resurrect21,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(500)
                                act_resurrected = pygame.image.load(elite_enermy.png)
                                act_resurrected1 = pygame.transform.rotozoom(act_resurrected,elite_enermy.a1,elite_enermy.b1)
                                window.blit(background.subsurface(pygame.Rect(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2,elite_enermy.choice()[0],elite_enermy.choice()[1])),(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                window.blit(act_resurrected1,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                pygame.display.update()
                                elite_enermy.hp_max = 100
                                elite_enermy.akt = 20
                                elite_enermy.defence = 20
                                elite_enermy.hp = elite_enermy.hp_max
                                HP_rounds -= 1
                                enermy_hp = elite_enermy.Character(False)
                                rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                            else:
                                window.blit(background.subsurface(pygame.Rect(elite_enermy_pos[0],elite_enermy_pos[1],elite_enermy_pos[2],elite_enermy_pos[3])),(elite_enermy_pos[0],elite_enermy_pos[1]))
                                pygame.display.update()
                        resurrect = injure(elite_enermy,fight_rounds,resurrect)
                    if fire.y <= my <= fire.y + fire.h and fireTF == True:
                        act_fire = pygame.image.load('C:\\game\\picture\\fire.png')
                        act_fire1 = pygame.transform.scale(act_fire,(230,200))
                        window.blit(act_fire1,(win_width/10 + 190,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(200)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 190,win_height*2/7 - 50,230,200)),(win_width/10 + 190,win_height*2/7 - 50))
                        window.blit(act_fire1,(win_width/10 + 240,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 240,win_height*2/7 - 50,230,200)),(win_width/10 + 240,win_height*2/7 - 50))
                        pygame.display.update()
                        act_fire_enermy = pygame.image.load('C:\\game\\picture\\fire_enermy.png')
                        act_fire1_enermy = pygame.transform.scale(act_fire_enermy,(elite_enermy.choice()[0],elite_enermy.choice()[1]))
                        window.blit(act_fire1_enermy,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                        pygame.display.update()
                        pygame.time.wait(300)
                        window.blit(background.subsurface(pygame.Rect(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2,elite_enermy.choice()[0],elite_enermy.choice()[1])),(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                        act_fired = pygame.image.load(elite_enermy.png)
                        act_fired1 = pygame.transform.rotozoom(act_fired,elite_enermy.a1,elite_enermy.b1)
                        window.blit(act_fired1,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                        pygame.display.update()
                        elite_enermy.hp -= character.akt/2
                        elite_enermy.hp = int(elite_enermy.hp)
                        enermy_hp = elite_enermy.Character(False)
                        rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                        if elite_enermy.hp <= 0:
                            if HP_rounds > 0:
                                act_resurrect1 = pygame.image.load('C:\\game\\picture\\resurrect1.png')
                                act_resurrect11 = pygame.transform.scale(act_resurrect1,(elite_enermy.choice()[0],elite_enermy.choice()[1]))
                                window.blit(act_resurrect11,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(300)
                                act_resurrect2 = pygame.image.load('C:\\game\\picture\\resurrect2.png')
                                act_resurrect21 = pygame.transform.scale(act_resurrect2,(elite_enermy.choice()[0],elite_enermy.choice()[1]))
                                window.blit(act_resurrect21,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(500)
                                act_resurrected = pygame.image.load(elite_enermy.png)
                                act_resurrected1 = pygame.transform.rotozoom(act_resurrected,elite_enermy.a1,elite_enermy.b1)
                                window.blit(background.subsurface(pygame.Rect(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2,elite_enermy.choice()[0],elite_enermy.choice()[1])),(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                window.blit(act_resurrected1,(elite_enermy.x1,elite_enermy.y1 - elite_enermy.choice()[1]/2))
                                pygame.display.update()
                                elite_enermy.hp_max = 100
                                elite_enermy.akt = 20
                                elite_enermy.defence = 20
                                elite_enermy.hp = elite_enermy.hp_max
                                HP_rounds -= 1
                                enermy_hp = elite_enermy.Character(False)
                                rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                            else:
                                window.blit(background.subsurface(pygame.Rect(elite_enermy_pos[0],elite_enermy_pos[1],elite_enermy_pos[2],elite_enermy_pos[3])),(elite_enermy_pos[0],elite_enermy_pos[1]))
                                pygame.display.update()
                        resurrect = injure(elite_enermy,fight_rounds,resurrect)
                    if recover.y <= my <= recover.y + recover.h and recoverTF == True:
                        act_recover1 = pygame.image.load('C:\\game\\picture\\recover1.png')
                        act_recover2 = pygame.image.load('C:\\game\\picture\\recover2.png')
                        act_recover_new1 = pygame.transform.scale(act_recover1,(character.choice()[0],character.choice()[1]))
                        act_recover_new2 = pygame.transform.scale(act_recover2,(character.choice()[0],character.choice()[1]))                        
                        window.blit(act_recover_new1,(character.x1,character.y1 - character.choice()[1]/2))
                        window.blit(act_recover_new2,(character.x1,character.y1 - character.choice()[1]/2))                        
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
                        act_recovered = pygame.image.load(character.png)
                        act_recovered1 = pygame.transform.rotozoom(act_recovered,character.a1,character.b1)
                        window.blit(act_recovered1,(character.x1,character.y1 - character.choice()[1]/2))
                        pygame.display.update()
                        character.hp += character.akt*2
                        if character.hp >= character.hp_max:
                            character.hp = character.hp_max
                        character_hp = character.Character(False)
                        rewrite(window,background,character_hp[1],character_hp[2],50,0,character_hp[0])
                        resurrect = injure(elite_enermy,fight_rounds,resurrect)
                if HP_rounds == 0:
                    fight_rounds += 1
            if event.type == pygame.QUIT:
                exit()
        if elite_enermy.hp <= 0 and HP_rounds == 0:
            window.fill((255,255,255))
            win_text = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf',20)
            win = win_text.render('You Win!',True,(155,0,0))
            window.blit(win,(win_width*2/5,win_height/2)) 
            pygame.display.update()
            pygame.time.wait(2000)
            number_guan += 1
    pygame.mixer.music.pause()
    return resurrect,number_guan

#==================================================================================BOSS关===================================================
def fight3(window,win_width,win_height,health,attack,defense,resurrect,number_guan):
    pygame.mixer.music.load('C:\\game\\picture\\fight_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.display.set_caption('head')
    back = pygame.image.load("C:\\game\\picture\\background.png")
    background = pygame.transform.scale(back,(800,600))
    window.blit(background,(0,0))
    pygame.display.flip()
    fight1_rounds = 1
    fight2_rounds = 1

    #=================角色==================
    #Character(图片，旋转，大小，位置，字体，名字，位置,颜色默认白色,大小,血量,血量上限，位置,窗口)
    #主角
    HP = health
    character =Character('C:\\game\\picture\\character.png',0,0.4,win_width/10,win_height*2/7 + 50,'C:\\game\\Uranus_Pixel_11Px.ttf','name',win_width/10,win_height/5 + 50,1,HP,health,win_width/10 - 30,win_height*2/7 + 50,attack,defense,window)
    character.Character(True)
   
    #Button(字体,位置，按钮大小，按钮颜色，按钮内容,字体默认白色，）
    #技能
    attack1 = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5,100,50,200,0,0,'攻击',window)
    attack_word,attack_x,attack_y = attack1.Button()
    fire = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5 + 55,100,50,0,0,200,'火球',window)
    fire_word,fire_x,fire_y = fire.Button()
    recover = Button('C:\\game\\Uranus_Pixel_11Px.ttf',win_width/10,win_height*3/5 + 110,100,50,0,200,0,'恢复',window) 
    recover_word,recover_x,recover_y = recover.Button() 

    #BOSS
    BOSS = Character('C:\\game\\picture\\BOSS.png',0,0.22,win_width*4/7,win_height/2,'C:\\game\\Uranus_Pixel_11Px.ttf','BOSS',win_width*4/7 + 40,win_height/2 - 35,1.4,50,50,win_width*4/7 + 30,win_height/2,30,20,window)
    BOSS.Character(True)
    BOSS_pos = [win_width/2,0,win_width/2,win_height] 
    HP_rounds = 2

    def injure(BOSS,fight1_rounds,fight2_rounds,resurrect):
        if BOSS.hp > 0:
            pygame.time.wait(500)
            window.blit(background.subsurface(pygame.Rect(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
            act_injure = pygame.image.load(BOSS.png)
            act_injure1 = pygame.transform.rotozoom(act_injure,BOSS.a1,BOSS.b1)
            window.blit(act_injure1,(BOSS.x1 - 20,BOSS.y1 - BOSS.choice()[1]/2))
            pygame.display.update()
            pygame.time.wait(100)
            window.blit(background.subsurface(pygame.Rect(BOSS.x1 - 20,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1 - 20,BOSS.y1 - BOSS.choice()[1]/2))
            window.blit(act_injure1,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
            pygame.display.update()
            pygame.time.wait(200)
            if fight1_rounds % 4 != 0:
                window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
                act_injured = pygame.image.load(character.png)
                act_injured1 = pygame.transform.rotozoom(act_injured,character.a1,character.b1)
                window.blit(act_injured1,(character.x1 - 20,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                pygame.time.wait(100)
                window.blit(background.subsurface(pygame.Rect(character.x1 - 20,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1 - 20,character.y1 - character.choice()[1]/2))
                window.blit(act_injured1,(character.x1,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                character.hp -= max(BOSS.akt - character.defence,0)
            elif fight1_rounds % 4 == 0:
                act_BOSS_injured = pygame.image.load('C:\\game\\picture\\act_elite_attact.png')
                act_BOSS_injured1 = pygame.transform.scale(act_BOSS_injured,(character.choice()[0],character.choice()[1]))
                window.blit(act_BOSS_injured1,(character.x1,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                pygame.time.wait(500)
                window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
                act_injured = pygame.image.load(character.png)
                act_injured1 = pygame.transform.rotozoom(act_injured,character.a1,character.b1)
                window.blit(act_injured1,(character.x1 - 20,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                pygame.time.wait(200)
                window.blit(background.subsurface(pygame.Rect(character.x1 - 20,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1 - 20,character.y1 - character.choice()[1]/2))
                window.blit(act_injured1,(character.x1,character.y1 - character.choice()[1]/2))
                pygame.display.update()
                character.hp -= BOSS.akt * 2
                character.hp = int(character.hp)
            character_hp = character.Character(False)
            rewrite(window,background,character_hp[1],character_hp[2],50,0,character_hp[0])
            if fight2_rounds % 5 == 0:
                pygame.time.wait(500)
                act_BOSS_recover = pygame.image.load('C:\\game\\picture\\BOSS_recover.png')
                act_BOSS_recover1 = pygame.transform.scale(act_BOSS_recover,(BOSS.choice()[0],BOSS.choice()[1]))
                window.blit(act_BOSS_recover1,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                pygame.display.update()
                pygame.time.wait(500)
                act_BOSS_recovered = pygame.image.load(BOSS.png)
                act_BOSS_recovered1 = pygame.transform.rotozoom(act_BOSS_recovered,BOSS.a1,BOSS.b1)
                window.blit(background.subsurface(pygame.Rect(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                window.blit(act_BOSS_recovered1,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                pygame.display.update()
                BOSS.hp += BOSS.akt
                if BOSS.hp > BOSS.hp_max:
                    BOSS.hp =BOSS.hp_max
                BOSS_hp = BOSS.Character(False)
                rewrite(window,background,BOSS_hp[1],BOSS_hp[2],50,0,BOSS_hp[0])
            if character.hp <= 0:
                window.fill((0,0,0))
                die_text = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf',20)
                die = die_text.render('You Dead...',True,(155,0,0))
                window.blit(die,(win_width*2/5,win_height/2)) 
                pygame.display.update()
                pygame.time.wait(2000)
                if resurrect > 0:
                    resurrect -= 1
                elif resurrect == 0:
                    exit()
        return resurrect

    while character.hp > 0 and BOSS.hp > 0  : 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = event.pos
                attackTF = False
                fireTF = False
                recoverTF = False
                #========确定技能============
                if  attack1.x <= mx <= attack1.x + attack1.w:
                    if attack1.y <= my <= attack1.y + attack1.h:
                        pygame.draw.rect(window,(100,100,100),(attack1.x,attack1.y,attack1.w,attack1.h))
                        window.blit(attack_word,(attack_x,attack_y))
                        pygame.display.update()
                        attackTF = True
                    elif fire.y <= my <= fire.y + fire.h:
                        pygame.draw.rect(window,(100,100,100),(fire.x,fire.y,fire.w,fire.h))
                        window.blit(fire_word,(fire_x,fire_y))
                        pygame.display.update()
                        fireTF = True
                    elif recover.y <= my <= recover.y + recover.h:
                        pygame.draw.rect(window,(100,100,100),(recover.x,recover.y,recover.w,recover.h))
                        window.blit(recover_word,(recover_x,recover_y))
                        pygame.display.update()  
                        recoverTF = True
                    else:
                        attackTF = False
                        fireTF = False
                        recoverTF = False
            #==========技能结算================
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.draw.rect(window,(200,0,0),(attack1.x,attack1.y,attack1.w,attack1.h))
                window.blit(attack_word,(attack_x,attack_y))
                pygame.draw.rect(window,(0,0,200),(fire.x,fire.y,fire.w,fire.h))
                window.blit(fire_word,(fire_x,fire_y))
                pygame.draw.rect(window,(0,200,0),(recover.x,recover.y,recover.w,recover.h))
                window.blit(recover_word,(recover_x,recover_y))
                pygame.display.update()
                mx,my = event.pos
                if  attack1.x <= mx <= attack1.x + attack1.w:
                    if attack1.y <= my <= attack1.y + attack1.h and attackTF == True:
                        BOSS.hp -= max(character.akt - BOSS.defence,0)
                        enermy_hp = BOSS.Character(False)
                        rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                        act_akt = pygame.image.load('C:\\game\\picture\\attakt.png')
                        act_akt1 = pygame.transform.scale(act_akt,(80,220))
                        window.blit(act_akt1,(win_width/10 + 190,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 190,win_height*2/7 - 50,80,220)),(win_width/10 + 190,win_height*2/7 - 50))
                        window.blit(background.subsurface(pygame.Rect(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                        act_attacked = pygame.image.load(BOSS.png)
                        act_attacked1 = pygame.transform.rotozoom(act_attacked,BOSS.a1,BOSS.b1)
                        window.blit(act_attacked1,(BOSS.x1 + 20,BOSS.y1 - BOSS.choice()[1]/2))
                        pygame.display.update()
                        pygame.time.wait(100)
                        window.blit(background.subsurface(pygame.Rect(BOSS.x1 + 20,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1 + 20,BOSS.y1 - BOSS.choice()[1]/2))
                        window.blit(act_attacked1,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                        pygame.display.update()
                        if BOSS.hp <= 0:
                            if HP_rounds > 0:
                                act_resurrect1 = pygame.image.load('C:\\game\\picture\\resurrect1.png')
                                act_resurrect11 = pygame.transform.scale(act_resurrect1,(BOSS.choice()[0],BOSS.choice()[1]))
                                window.blit(act_resurrect11,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(300)
                                act_resurrect2 = pygame.image.load('C:\\game\\picture\\resurrect2.png')
                                act_resurrect21 = pygame.transform.scale(act_resurrect2,(BOSS.choice()[0],BOSS.choice()[1]))
                                window.blit(act_resurrect21,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(500)
                                act_resurrected = pygame.image.load(BOSS.png)
                                act_resurrected1 = pygame.transform.rotozoom(act_resurrected,BOSS.a1,BOSS.b1)
                                window.blit(background.subsurface(pygame.Rect(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                window.blit(act_resurrected1,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                pygame.display.update()
                                BOSS.hp_max +=50
                                BOSS.akt += 10
                                BOSS.defence += 5
                                BOSS.hp = BOSS.hp_max
                                HP_rounds -= 1
                                if HP_rounds == 0:
                                    window.blit(background.subsurface(pygame.Rect(BOSS_pos[0],BOSS_pos[1],BOSS_pos[2],BOSS_pos[3])),(BOSS_pos[0],BOSS_pos[1]))
                                    BOSS.png = 'C:\\game\\picture\\BOSS2.png'
                                    BOSS.Character(True)
                                enermy_hp = BOSS.Character(False)
                                rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                            else:
                                window.blit(background.subsurface(pygame.Rect(BOSS_pos[0],BOSS_pos[1],BOSS_pos[2],BOSS_pos[3])),(BOSS_pos[0],BOSS_pos[1]))
                                pygame.display.update()
                        resurrect = injure(BOSS,fight1_rounds,fight2_rounds,resurrect)
                    if fire.y <= my <= fire.y + fire.h and fireTF == True:
                        act_fire = pygame.image.load('C:\\game\\picture\\fire.png')
                        act_fire1 = pygame.transform.scale(act_fire,(230,200))
                        window.blit(act_fire1,(win_width/10 + 190,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(200)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 190,win_height*2/7 - 50,230,200)),(win_width/10 + 190,win_height*2/7 - 50))
                        window.blit(act_fire1,(win_width/10 + 240,win_height*2/7 - 50))
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(win_width/10 + 240,win_height*2/7 - 50,230,200)),(win_width/10 + 240,win_height*2/7 - 50))
                        pygame.display.update()
                        act_fire_enermy = pygame.image.load('C:\\game\\picture\\fire_enermy.png')
                        act_fire1_enermy = pygame.transform.scale(act_fire_enermy,(BOSS.choice()[0],BOSS.choice()[1]))
                        window.blit(act_fire1_enermy,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                        pygame.display.update()
                        pygame.time.wait(300)
                        window.blit(background.subsurface(pygame.Rect(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                        act_fired = pygame.image.load(BOSS.png)
                        act_fired1 = pygame.transform.rotozoom(act_fired,BOSS.a1,BOSS.b1)
                        window.blit(act_fired1,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                        pygame.display.update()
                        BOSS.hp -= character.akt/2
                        BOSS.hp = int(BOSS.hp)
                        enermy_hp = BOSS.Character(False)
                        rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                        if BOSS.hp <= 0:
                            if HP_rounds > 0:
                                act_resurrect1 = pygame.image.load('C:\\game\\picture\\resurrect1.png')
                                act_resurrect11 = pygame.transform.scale(act_resurrect1,(BOSS.choice()[0],BOSS.choice()[1]))
                                window.blit(act_resurrect11,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(300)
                                act_resurrect2 = pygame.image.load('C:\\game\\picture\\resurrect2.png')
                                act_resurrect21 = pygame.transform.scale(act_resurrect2,(BOSS.choice()[0],BOSS.choice()[1]))
                                window.blit(act_resurrect21,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                pygame.display.update()
                                pygame.time.wait(500)
                                act_resurrected = pygame.image.load(BOSS.png)
                                act_resurrected1 = pygame.transform.rotozoom(act_resurrected,BOSS.a1,BOSS.b1)
                                window.blit(background.subsurface(pygame.Rect(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2,BOSS.choice()[0],BOSS.choice()[1])),(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                window.blit(act_resurrected1,(BOSS.x1,BOSS.y1 - BOSS.choice()[1]/2))
                                pygame.display.update()
                                BOSS.hp_max += 50
                                BOSS.akt += 10
                                BOSS.defence += 5
                                BOSS.hp = BOSS.hp_max
                                HP_rounds -= 1
                                if HP_rounds == 0:
                                    window.blit(background.subsurface(pygame.Rect(BOSS_pos[0],BOSS_pos[1],BOSS_pos[2],BOSS_pos[3])),(BOSS_pos[0],BOSS_pos[1]))
                                    BOSS.png = 'C:\\game\\picture\\BOSS2.png'
                                    BOSS.Character(True)
                                enermy_hp = BOSS.Character(False)
                                rewrite(window,background,enermy_hp[1],enermy_hp[2],50,0,enermy_hp[0])
                            else:
                                window.blit(background.subsurface(pygame.Rect(BOSS_pos[0],BOSS_pos[1],BOSS_pos[2],BOSS_pos[3])),(BOSS_pos[0],BOSS_pos[1]))
                                pygame.display.update()
                        resurrect = injure(BOSS,fight1_rounds,fight2_rounds,resurrect)
                    if recover.y <= my <= recover.y + recover.h and recoverTF == True:
                        act_recover1 = pygame.image.load('C:\\game\\picture\\recover1.png')
                        act_recover2 = pygame.image.load('C:\\game\\picture\\recover2.png')
                        act_recover_new1 = pygame.transform.scale(act_recover1,(character.choice()[0],character.choice()[1]))
                        act_recover_new2 = pygame.transform.scale(act_recover2,(character.choice()[0],character.choice()[1]))                        
                        window.blit(act_recover_new1,(character.x1,character.y1 - character.choice()[1]/2))
                        window.blit(act_recover_new2,(character.x1,character.y1 - character.choice()[1]/2))                        
                        pygame.display.update()
                        pygame.time.wait(400)
                        window.blit(background.subsurface(pygame.Rect(character.x1,character.y1 - character.choice()[1]/2,character.choice()[0],character.choice()[1])),(character.x1,character.y1 - character.choice()[1]/2))
                        act_recovered = pygame.image.load(character.png)
                        act_recovered1 = pygame.transform.rotozoom(act_recovered,character.a1,character.b1)
                        window.blit(act_recovered1,(character.x1,character.y1 - character.choice()[1]/2))
                        pygame.display.update()
                        character.hp += character.akt*2
                        if character.hp >= character.hp_max:
                            character.hp = character.hp_max
                        character_hp = character.Character(False)
                        rewrite(window,background,character_hp[1],character_hp[2],50,0,character_hp[0])
                        resurrect = injure(BOSS,fight1_rounds,fight2_rounds,resurrect)
                if HP_rounds < 2:
                    fight1_rounds += 1
                if HP_rounds == 0:
                    fight2_rounds += 1
            if event.type == pygame.QUIT:
                exit()
        if BOSS.hp <= 0 and HP_rounds == 0:
            window.fill((255,255,255))
            win_text = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf',20)
            win = win_text.render('You Win!',True,(155,0,0))
            window.blit(win,(win_width*2/5,win_height/2)) 
            pygame.display.update()
            pygame.time.wait(2000)
            number_guan += 1
    pygame.mixer.music.pause()
    return resurrect,number_guan