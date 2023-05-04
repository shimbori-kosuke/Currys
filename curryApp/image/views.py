from django.shortcuts import render
from django.views import View
from .utils import chat_gpt_image, chat_gpt, create_prompt
from django.http import JsonResponse


class CreateImageView(View):
    
    def get(self, request, *args, **kwargs):

        return render(request, 'image/home.html')
    
    def post(self, request, *args, **kwargs):

        input_sentence = request.POST.get('input_sentence', None)  #画面で入力した説明文を取得
        if input_sentence: 
            # Chat-GPTに投げる命令文を生成
            prompt = create_prompt(input_sentence, "CreateImage.txt")
            response = chat_gpt(prompt)  # Chat-GPTから回答を取得する。
            #tranlate_sentence  = "次の文章を日本語に翻訳してください。\n" + response
            #response_jp = chat_gpt(tranlate_sentence)   # chat-gptで日本語に変換
            image = chat_gpt_image(response)   # 画像生成処理を実行する。

            translated_img = 'data:' + 'image/jpeg' + ';base64,' + image

            context = {
                'input_sentence':input_sentence,
                'response': response,
                'img' : translated_img,
                }
            return JsonResponse(context)
        else:
            return render(request, 'image/home.html')