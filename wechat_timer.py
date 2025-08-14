import time
import pyautogui
import pyperclip

# ====== 用户配置区域 ======
RECIPIENT = "文件传输助手"  # 要发送的好友或群聊名称
MESSAGE = "6"  # 要发送的消息内容
SCHEDULE_TIME = "19:06"  # 发送时间（24小时制）
# =========================

def send_wechat_message():
    """发送微信消息的简单函数"""
    try:
        # 1. 复制消息内容到剪贴板
        current_time = time.strftime("%H:%M")
        formatted_msg = MESSAGE.format(time=current_time)
        pyperclip.copy(formatted_msg)
        
        # 2. 打开微信
        pyautogui.hotkey('ctrl', 'alt', 'w')  # 微信默认快捷键
        time.sleep(1)  # 等待微信打开
        
        # 3. 搜索联系人
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(2)
        pyautogui.write(RECIPIENT)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        
        # 4. 粘贴并发送消息
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        
        # 5. 关闭微信窗口
        pyautogui.hotkey('ctrl', 'alt', 'w')
        
        print(f"[{current_time}] 消息已发送给: {RECIPIENT}")
    except Exception as e:
        print(f"发送失败: {str(e)}")

# 主循环
print(f"微信定时消息已启动，将在 {SCHEDULE_TIME} 发送...")
print("请保持微信登录且窗口不最小化")
print("按 Ctrl+C 停止程序")

while True:
    current_time = time.strftime("%H:%M")
    
    # 检查是否到达发送时间
    if current_time == SCHEDULE_TIME:
        send_wechat_message()
        
        # 避免重复发送（等待到下一分钟）
        time.sleep(60)
    
    # 每分钟检查一次
    time.sleep(30)
