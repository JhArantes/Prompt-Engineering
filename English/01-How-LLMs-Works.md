# 🤖 Language Models: How Do They Work?

LLMs (Large Language Models) are trained on billions of words 🧠💬.  
But the idea of a **language model** came before modern AI — it's all about spotting **linguistic patterns**.

📌 Example:  
"I like **pizza**" → whenever we use the verb *like*, it's usually followed by "to" or "of". That’s a predictable pattern!

Language models learn these patterns to **predict the next word**, understanding **structures and relationships** between words.

---

# 🧠 Word Embeddings

**Word Embeddings** are numeric representations (vectors) of words that capture **semantic similarity**.

📍 Example:  
Words like "king" and "queen" are close together, just like "cat" and "dog".

They help the model understand **contextual similarity** — even between different words.

🖼️  
![embeddings](./IMGs/Embeddings.png)  
![word Embedding](./IMGs/Word-Em.png)

---

# 🕹️ Play with the AI

> “Let’s simulate how ChatGPT works!  
For every sentence I write, you reply with the 5 most likely words to complete it — along with their probabilities.  
Just the words and probabilities, nothing else.”

---

## 🔮 Predicting the Next Word

At each step, the AI
