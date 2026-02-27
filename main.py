from fastapi import FastAPI
from pydantic import BaseModel
from chat import chat_with_ai

app = FastAPI(title="AI Agent学习项目 - Day1")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {
        "message": "AI Agent API 运行中",
        "status": "ok",
        "features": ["/chat - AI对话", "/search - 模拟搜索"]
    }

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """真实AI对话接口"""
    ai_reply = chat_with_ai(request.message)
    return {
        "user_message": request.message,
        "ai_reply": ai_reply,
        "model": "deepseek-chat",
        "note": "知识截止2024-07，明天接入实时搜索"
    }

@app.get("/search")
async def search(query: str):
    """明天升级为真实搜索工具"""
    return {
        "query": query,
        "results": ["模拟结果：明天这里会调用真实搜索API"],
        "status": "placeholder"
    }