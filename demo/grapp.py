
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="medalpaca/medalpaca-7b", tokenizer="medalpaca/medalpaca-7b")
question = "What are the symptoms of diabetes?"
context = "Diabetes is a metabolic disease that causes high blood sugar. The symptoms include increased thirst, frequent urination, and unexplained weight loss."
answer = qa_pipeline({"question": question, "context": context})
print(answer)
