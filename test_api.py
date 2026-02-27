import httpx
import json

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    """测试根接口"""
    response = httpx.get(f"{BASE_URL}/")
    print("=== 根接口 ===")
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
    print()

def test_chat():
    """测试AI对话接口"""
    url = f"{BASE_URL}/chat"
    data = {"message": "你好，我是前端工程师，正在学习AI Agent"}
    
    print("=== /chat 接口 ===")
    print(f"请求: {json.dumps(data, ensure_ascii=False)}")
    
    response = httpx.post(url, json=data, timeout=60.0)
    print(f"状态码: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"AI回复: {result.get('ai_reply', '无回复')}")
        print(f"模型: {result.get('model', '未知')}")
    else:
        print(f"错误: {response.text}")
    print()

if __name__ == "__main__":
    try:
        test_root()
        test_chat()
    except Exception as e:
        print(f"测试失败: {e}")
        print("请确保服务已启动: uvicorn main:app --reload")