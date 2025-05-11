
# 🧠 Prompt Engineering

**Prompt Engineering** is the process of strategically designing instructions (prompts) so that language models like ChatGPT, Gemini, Claude, or LLaMA produce more accurate, useful, and coherent responses.

Just like we ask different questions to get different answers from people, the way you *formulate* a prompt directly affects the quality of the AI's output.

This document introduces two of the most powerful techniques in Prompt Engineering: **Chain of Thought Prompting** and **Few-Shot Prompting**, and how combining them can lead to exceptional results.

---

## 🔗 Chain of Thought Prompting

**Chain of Thought Prompting** is a technique that guides the model to **think step by step**, explicitly reasoning through a task before delivering the final answer.

In other words, the prompt suggests a logical *chain of reasoning* the model should follow.

[📄 Artigo Chain of Thought no arXiv](https://arxiv.org/abs/2201.11903)


This technique is ideal for:
- Math problems
- Logic or symbolic reasoning
- Complex or ethical decisions
- Multi-variable analysis

💡 **Tip**: Even without examples, simply adding phrases like **"explain step by step"** can trigger this behavior in more advanced models.

---

## ✍️ Few-Shot Prompting

**Few-Shot Prompting** is the technique of providing **two or more full input-output examples** to the model, so it learns the desired pattern before attempting the main task.

📚 Prompting types:
- ❌ **Zero-shot**: only the question or instruction, no examples.
- ☝️ **One-shot**: one single example before the task.
- ✌️ **Few-shot**: two or more examples, followed by the actual task.

This technique allows the model to:
- Understand the **expected format**
- Learn the **type of reasoning** needed
- Respond more **consistently and accurately**

---

## 🚀 Combining Techniques

When you combine **Chain of Thought + Few-Shot Prompting**, you're giving the model both the **response structure** and the **reasoning process** to follow.

This creates highly effective prompts, especially for complex reasoning tasks.

---

## 🧪 Advanced Prompt Example

```txt
Question: I have a list of values. My final result will be 30% of the sum of those values. However, not all values will be included—only those above $40,000. For the list below, count how many values are above $40,000, identify which ones, sum them, and then calculate 30% of that sum.

$10,000  
$20,000  
$50,000  
$60,000

Answer: In this list, there are 4 values. There are 2 values above $40,000: $50,000 and $60,000. Their sum is $110,000. The final result is 30% of that, which is $33,000.

```

---

Question: I have a list of values. My final result will be 30% of the sum of those values. However, not all values will be included—only those above $40,000. For the list below, count how many values are above $40,000, identify which ones, sum them, and then calculate 30% of that sum.

$31,000  
$15,000  
$52,000  
$103,000  
$42,000  
$156,000  
$15,000  
$27,000  
$82,000  
$33,000

Answer:



## ✅ Conclusion

**Prompt Engineering** is a powerful discipline that enhances the interaction between humans and AI. By understanding and applying techniques like:

- 🔗 **Chain of Thought Prompting** – guiding the model to reason step by step  
- ✍️ **Few-Shot Prompting** – showing examples to establish a pattern

you can dramatically improve the relevance, coherence, and accuracy of the AI’s output.

Whether you're solving logic problems, analyzing data, or building intelligent applications, mastering prompt design is a valuable tool in your AI toolkit.

Start small, experiment often, and combine techniques to unlock the full potential of large language models.
