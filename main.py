from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI(title="AI Agent学习项目")

@app.get("/")
async def root():
    return {"message": "Hello, I'm learning AI Agent!", "status": "ok"}

@app.get("/search")
async def search(query: str):
    """模拟搜索工具 - 第7天会换成真实的"""
    return {
        "query": query,
        "results": [f"关于 '{query}' 的模拟结果1", "模拟结果2"],
        "source": "mock_database"
    }

@app.post("/chat")
async def chat(message: str):
    """模拟对话接口 - 第4天接入真实LLM"""
    return {
        "user_message": message,
        "ai_reply": f"我收到了你的消息：{message}。明天我会学会调用真实的大模型来回答你！",
        "timestamp": "2024-02-10"
    }

# 运行命令：uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)