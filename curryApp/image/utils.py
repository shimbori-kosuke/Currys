import openai
import requests
import os
from django.conf import settings

API_KEY = settings.GPT_API_KEY

# 画像生成
def chat_gpt_image(prompt):
    openai.api_key = API_KEY
    openai.Model.list()

    # 応答設定
    response = openai.Image.create(
                  prompt = prompt,             # 画像生成に用いる説明文章
                  n = 1,                     # 何枚の画像を生成するか
                  size = '512x512',          # 画像サイズ
                  response_format = "b64_json"    # API応答のフォーマット

                )

    # API応答から画像を指定
    image = response['data'][0]['b64_json']
        
    return image


def chat_gpt(prompt):
    openai.api_key = API_KEY #API KEYをセット
    openai.Model.list() #OpenAIのインスタンスを生成

    #APIを使ってリクエストを投げる
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt= prompt,
        temperature=0.3,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0

    )
    response = response["choices"][0]["text"]

    print(response)

    return response

def create_prompt(input_text, file_name):
    prompt_file = os.path.join(settings.BASE_DIR, 'template', file_name)
    with open(prompt_file, encoding="utf-8") as f:
        file_read = f.read()
    #Chat-GTPへ投げるフォーマットに入力文をセットする。
    prompt = file_read.replace("[input]", input_text)
    return prompt