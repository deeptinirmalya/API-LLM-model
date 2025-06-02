import google.generativeai as genai
genai.configure(api_key="AIzaSyCEXzAB9iv_FnhByOeSOYPjYNqxExosW_w")

def chat_with_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    response = model.generate_content(prompt)
    return response.text
# print("hii ask me any thing:")
# while True:
#     prompt = input("you:")
#     reply = chat_with_gemini(prompt)
#     print("geminai:",reply,"\n")