# 🧠 Prompt Engineering – Advanced Techniques

This document explores **three advanced techniques** in Prompt Engineering to improve reasoning and reliability in large language models (LLMs):  
**Least-to-Most Prompting**, **Chain of Verification**, and **Self-Consistency**.

---

## 🔁 Least-to-Most Prompting

This strategy breaks down complex problems into **a sequence of simpler subproblems**, starting from the least difficult and gradually increasing in complexity. The model solves each part in order, using the previous solutions to build toward the final answer.

✅ **Best for:**
- Multi-step math problems
- Logical reasoning tasks
- Educational or tutoring prompts

---

## ✅ Chain of Verification

This technique ensures **answer validation** by adding a self-checking phase after the model gives its initial response.

### How it works:
1. 📝 **Initial Prompt and Answer**  
   The model answers the original question.

2. ❓ **Generate Verification Questions**  
   It then creates questions to check the key parts of its own answer.

3. 🔄 **Run Verifications**  
   The model answers these self-generated questions.

4. ✅ **Final Verified Answer**  
   It produces a revised and more reliable final answer based on the validations.

**Example Use Cases:** Coding, complex decisions, data interpretation.

---

## 🔄 Self-Consistency

Instead of depending on a **single output**, this method prompts the model **multiple times** with the same question and collects all responses.

Then, it analyzes them to select the **most frequent answer** (majority vote).

💡 This helps eliminate randomness and leads to **more stable and accurate** responses.

✅ **Especially useful for:**
- Math word problems
- Symbolic or logical reasoning
- Any task where deterministic output is preferred

---

## 📦 Summary

| Technique              | Purpose                                         | Ideal For                            |
|------------------------|-------------------------------------------------|--------------------------------------|
| Least-to-Most Prompting| Step-by-step buildup of understanding           | Complex reasoning tasks              |
| Chain of Verification  | Adds validation by generating self-check steps | Critical, multi-faceted questions    |
| Self-Consistency       | Boosts reliability by repeating and comparing  | Math, logic, and structured outputs  |

---

### 🧠 Prompt Engineering is not only about “what” you ask — but also **how you guide** the model to think, verify, and decide.

