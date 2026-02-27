import openai
from fastapi import FastAPI

print("✅ Python 环境正常")
print(f"OpenAI 版本: {openai.__version__}")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello AI Agent"}