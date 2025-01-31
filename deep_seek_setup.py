# from openai import OpenAI
#
# def DeepSeek(api_key, base_url, source, target):
#     client = OpenAI(api_key=api_key, base_url=base_url)
#
#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         # Change this to make DeepSeek translate input
#         messages=[
#             {"role": "system", "content": f"You are a helpful translator capable of translating input from {source} to {target}."},
#             {"role": "user", "content": "Hello"},
#         ],
#         stream=False
#     )
#
#     print(response.choices[0].message.content)
#
#     def get_supported_languages():
#         # Pull languages DeepSeek can translate into and arrange them into a dictionary
#         # with two-letter abbreviations as keys to full language names
#         pass
