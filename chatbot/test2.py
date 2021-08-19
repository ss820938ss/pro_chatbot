# from konlpy.tag import Okt
#
# okt = Okt()
# print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
#

# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
#
# nltk.download()
# example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
# stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"
# # 위의 불용어는 명사가 아닌 단어 중에서 저자가 임의로 선정한 것으로 실제 의미있는 선정 기준이 아님
# stop_words = stop_words.split(' ')
# word_tokens = word_tokenize(example)
#
# result = []
# for w in word_tokens:
#     if w not in stop_words:
#         result.append(w)
# # 위의 4줄은 아래의 한 줄로 대체 가능
# # result=[word for word in word_tokens if not word in stop_words]
#
# print(word_tokens)
# print(result)


# sent = '김철수는 극중 두 인격의 사나이 이광수 역을 맡았다. 철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연재(김광수 분)를 찾으러 속세로 내려온 인물이다.'
# new_sent = sent.replace(" ", '') # 띄어쓰기가 없는 문장 임의로 만들기
# print(new_sent)
#
# from pykospacing import Spacing
# spacing = Spacing()
# kospacing_sent = spacing(new_sent)
#
# print(sent)
# print(kospacing_sent)
#
#
# from hanspell import spell_checker
#
# sent = "맞춤법 틀리면 외 않되? 쓰고싶은대로쓰면돼지 "
# spelled_sent = spell_checker.check(sent)
#
# hanspell_sent = spelled_sent.checked
# print(hanspell_sent)
#
# spelled_sent = spell_checker.check(new_sent)
#
# hanspell_sent = spelled_sent.checked
# print(hanspell_sent)
# print(kospacing_sent) # 앞서 사용한 kospacing 패키지에서 얻은 결과

# import urllib.request
# from soynlp import DoublespaceLineCorpus
# from soynlp.word import WordExtractor
#
# urllib.request.urlretrieve("https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt", filename="2016-10-20.txt")
#
# corpus = DoublespaceLineCorpus("2016-10-20.txt")
# len(corpus)

# i = 0
# for document in corpus:
#   if len(document) > 0:
#     print(document)
#     i = i+1
#   if i == 3:
#     break

# word_extractor = WordExtractor()
# word_extractor.train(corpus)
# word_score_table = word_extractor.extract()
#
# print(word_score_table["반포한"].cohesion_forward)
# print(word_score_table["반포한강공원"].cohesion_forward)
#
# print(word_score_table["디스"].right_branching_entropy)
# print(word_score_table["디스플"].right_branching_entropy)

from ckonlpy.tag import Twitter
twitter = Twitter()
twitter.morphs('은경이는 사무실로 갔습니다.')