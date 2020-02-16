from survey import AnonymousSurvey
# 定义一个问题， 并创建一个表示调查的AnonymousSurvey
question = "哪门语言是你第一门学会的语言"
my_survey = AnonymousSurvey(question)
# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# 显示调查结果
print("\n谢谢参加调查的每一位")
my_survey.show_results()