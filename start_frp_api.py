from openai import OpenAI
import httpx
import ssl

# 创建自定义HTTP客户端，禁用SSL验证
http_client = httpx.Client(verify=False)

client = OpenAI(
    base_url="https:///v1", 
    api_key="lm-studio",
    http_client=http_client
)

messages = [
    {"role": "system", "content": "You are a helpful assistant"}
]

while True:
    user_input = input("你：")
    if user_input.strip().lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user_input})

    stream = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528-qwen3-8b",
        messages=messages,
        temperature=0.7,
        stream=True,
    )

    reply = []
    for chunk in stream:
        token = chunk.choices[0].delta.content or ""
        print(token, end="", flush=True)
        reply.append(token)
    print()
    messages.append({"role": "assistant", "content": "".join(reply)})