import pandas as pd

chatbot_data = pd.read_excel("chatbot_data.xlsx")
# print(chatbot_data)

chat_dic = {}
row = 0
for rule in chatbot_data['rule']:
    chat_dic[row] = rule.split('|')
    row += 1
# print(chat_dic)

def chat(request):
    for k, v in chat_dic.items():
        index = -1
        for word in v:
            try:
                if index == -1:
                    index = request.index(word)
                else:
                    if index < request.index(word, index):
                        index = request.index(word, index)
                    else:
                        index = -1
                        break
            except ValueError:
                index = -1
                break
        if index > -1:
            return chatbot_data['response'][k]
    return '무슨 말인지 모르겠어요'


while True:
    req = input('대화를 입력해보세요.')
    if req == 'exit':
        break
    else:
        print('챗봇 테스트 : ', chat(req))
