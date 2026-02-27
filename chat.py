import os
from openai import OpenAI
from dotenv import load_dotenv
import httpx

load_dotenv()

# 创建自定义 httpx 客户端（不使用 proxies）
http_client = httpx.Client(timeout=60.0)

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
    http_client=http_client  # 使用自定义客户端
)

def chat_with_ai(message: str, model: str = "deepseek-chat") -> str:
    """
    调用DeepSeek API进行对话
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一个资深前端工程师，用中文回答技术问题。"},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"调用API出错: {str(e)}"

if __name__ == "__main__":
    print("🤖 DeepSeek AI 测试")
    print("输入 'quit' 退出\n")
    
    while True:
        user_input = input("你: ")
        if user_input.lower() == "quit":
            break
        
        reply = chat_with_ai(user_input)
        print(f"AI: {reply}\n")