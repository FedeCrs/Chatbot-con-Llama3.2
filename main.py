import ollama


prompt = "Escribe una función en python para comunicar en vss con "
model = "llama3.2"

response = ollama.run(model=model,
                       messages=[
                           {'role' : 'user', 'content' : prompt}
                           ])

print(response['message']['content'])