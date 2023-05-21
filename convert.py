import os
from pypinyin import lazy_pinyin

conversation = []

print("输入简体中文即可转换成机器学习可使用的汉语拼音，输入stop结束进程")

while True:
    text = input("\n在这里输入文本：")
    if text == "stop":
        break
    pinyin = lazy_pinyin(text)
    pinyin_text = "".join(pinyin)
    conversation.append(f"User: {text}\nAI: {pinyin_text}\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("输入简体中文即可转换成机器学习可使用的汉语拼音，输入stop结束进程")
    print('\n'.join(conversation))
