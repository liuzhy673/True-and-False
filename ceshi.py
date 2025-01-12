import pygame
import sys
from openai import OpenAI
def run_ai():
    # 初始化 OpenAI 客户端
    client = OpenAI(
        base_url='http://10.15.88.73:5001/v1',
        api_key='ollama',  # required but ignored
    )

    # 初始化pygame
    pygame.init()
    npc=pygame.image.load('C:\\game\\picture\\npc.png')
    npc=pygame.transform.scale(npc,(60,60))
    yuanbb=pygame.image.load('C:\\game\\picture\\yuanbb.png')
    yuanbb=pygame.transform.scale(yuanbb,(75,60))
    # 设置屏幕尺寸
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 设置窗口标题
    pygame.display.set_caption("聊天窗口")

    # 定义颜色
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    RED = (255, 0, 0)
    BROWN = (165, 42, 42)  # 棕色背景
    BLACK = (0, 0, 0)  # 定义黑色

    # 设置字体和字号
    font = pygame.font.Font('C:\\game\\Uranus_Pixel_11Px.ttf', 24)

    # 文本输入框的参数
    input_box_width = 600
    input_box_height = 50
    input_box_x = (screen_width - input_box_width) // 2
    input_box_y = screen_height - input_box_height - 20

    # 创建文本输入框的矩形
    input_box_rect = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)

    # 文本输入框的颜色
    input_box_color_active = pygame.Color('lightskyblue3')
    input_box_color_inactive = pygame.Color('dodgerblue2')
    input_box_color = input_box_color_inactive

    # 用于判断文本输入框是否被激活
    active = False

    # 用于存储输入的文本
    user_input = ''

    # 定义系统消息
    system_message = """
    You are an AI assistant in a RPG game called SAO. Your role is to guide the player through the game world, 
    including prompting that he'd better have his weapons more powerful or buy some armors
    if the player asks you about the background of this game,you can answer that it's a game world created by 茅场晶彦,he wants to have a duel with you again, so he took asuna as a hostage.
    if the player asks you where is he, you can answer you are in a game world and he was trapped in this world
    if the player asks you how to play this game,you should answer Increase your attack by buying weapons, increase your defense by buying armor, and give you gold if you win or lose
    if the player types something not related with above,please asnwer:"papa,what do you mean?youki didn't understand
    if the player asks who are you,please answer I'm your daugther,youki,papa, you forgot me?
    if the player asks who am I,please answer you are my papa,Kirito
    if the player asks why I'm here this kind of questions, please answer: I know in the real world,you're crazy about the game Sword Art Online, so the system send you here
    
    please make sure (type exit to exit the program) at the end of your every answer

    You should provide helpful tips and answers to the player's questions, but keep your responses concise.
    """

    # 初始化消息列表
    messages = [
        {"role": "system", "content": system_message}
    ]

    def wrap_text(text, font, max_width):
        """将长文本分割成多行，每行的长度不超过max_width"""
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            test_surface = font.render(test_line, True, WHITE)
            if test_surface.get_width() <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)
        return lines

    def render_text(text, font=font, color=WHITE, max_width=input_box_width):
        """将文本渲染为图像，支持自动换行"""
        lines = wrap_text(text, font, max_width)
        surfaces = [font.render(line, True, color) for line in lines]
        return surfaces

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查鼠标点击位置是否在输入框内
                if input_box_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                input_box_color = input_box_color_active if active else input_box_color_inactive
            elif event.type == pygame.KEYDOWN:
                if active:
                    if user_input.lower() in ["exit", "quit"]:
                        print("Chat ends.")
                        running = False
                        break
                    if event.key == pygame.K_RETURN:
                        # print("succeed")
                        print(user_input)
                        messages.append({"role": "user", "content": user_input})
                        user_input = ""
                        try:
                            response = client.chat.completions.create(
                                model="llama3.2",      
                                messages=messages,    
                                max_tokens=150  # 限制回复字数
                            )

                            # 提取模型回复
                            assistant_reply = response.choices[0].message.content
                            print(f"Llama: {assistant_reply}")

                            # 将助手回复添加到对话历史
                            messages.append({"role": "assistant", "content": assistant_reply})

                        except Exception as e:
                            print(f"Error: {e}")
                            print("请检查链接是否正确，或稍后再试。")

                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

        # 填充窗口背景色
        screen.fill(BLACK)

        # 绘制输入框
        pygame.draw.rect(screen, input_box_color, input_box_rect)

        # 渲染输入的文本，支持自动换行
        text_surfaces = render_text(user_input)
        for i, text_surface in enumerate(text_surfaces):
            screen.blit(text_surface, (input_box_x + 5, input_box_y + 5 + i * (text_surface.get_height() + 2)))

        # 设置历史消息显示的最大数量
        max_display_messages = 2

        # 绘制历史消息
        y_offset = 50
        # 只取最新的max_display_messages条消息
        display_messages = messages[-max_display_messages:]
        for message in display_messages:
            if message['role'] != 'system':  # 跳过系统消息的渲染
                text_surfaces = render_text(message['content'])
                for text_surface in text_surfaces:
                    screen.blit(text_surface, (100, y_offset))
                    y_offset += text_surface.get_height() + 2
        screen.blit(yuanbb,(10,50))
        screen.blit(npc,(700,80))
        # 更新屏幕显示
        pygame.display.flip()

        # 控制帧率
        clock.tick(60)

