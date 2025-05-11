# 🧠 Engenharia de Prompt (Prompt Engineering)

**Engenharia de Prompt** é o processo de desenhar instruções (prompts) de forma estratégica para que modelos de linguagem como o ChatGPT, Gemini, Claude ou Llama produzam resultados mais precisos, úteis e coerentes.

Assim como fazemos perguntas diferentes para obter respostas diferentes de uma pessoa, com modelos de IA isso também acontece. A forma como você *constrói* o prompt influencia diretamente a qualidade da resposta.

Este documento explica duas das técnicas mais poderosas em Prompt Engineering: **Chain of Thought Prompting** e **Few-Shot Prompting** — além de como combiná-las para obter resultados excepcionais.

---

## 🔗 Chain of Thought Prompting (Cadeia de Pensamento)

**Chain of Thought Prompting** é uma técnica onde orientamos o modelo a **pensar passo a passo**, explicitando o raciocínio necessário para resolver o problema.

Ou seja, o prompt sugere uma *cadeia lógica de pensamento* que o modelo deve seguir antes de dar a resposta final.

[📄 Artigo Chain of Thought no arXiv](https://arxiv.org/abs/2201.11903)


Essa técnica é ideal para:
- Problemas matemáticos
- Questões de lógica ou raciocínio simbólico
- Decisões complexas ou éticas
- Análises com múltiplas variáveis

💡 **Dica**: Mesmo sem exemplos prévios, adicionar frases como **“explique passo a passo”** ao seu prompt já ativa esse comportamento em modelos mais avançados.

---

## ✍️ Few-Shot Prompting (Prompting com Exemplos)

**Few-shot prompting** é a técnica de fornecer **dois ou mais exemplos completos** de entrada e saída ao modelo, para que ele entenda o padrão desejado antes da tarefa principal.

📚 Tipos de prompting:
- ❌ **Zero-shot**: apenas a pergunta ou comando, sem exemplos.
- ☝️ **One-shot**: um único exemplo antes da tarefa.
- ✌️ **Few-shot**: dois ou mais exemplos, seguidos da tarefa principal.

Essa técnica permite que o modelo:
- Reconheça o **formato** da resposta esperada
- Entenda o **tipo de raciocínio** necessário
- Se comporte de forma mais **consistente e precisa**

---

## 🚀 Combinando as Técnicas

Ao combinar **Chain of Thought + Few-shot Prompting**, você oferece ao modelo não apenas o padrão de resposta, mas também **como pensar** para chegar nela.

Essa união produz prompts muito poderosos, principalmente em tarefas com raciocínio complexo.

---

### 🧪 Exemplo de Prompt Avançado

```txt
Pergunta: Tenho uma lista de valores. O meu resultado final será 30% da soma desses valores. Porém, nem todos os valores serão somados, apenas aqueles acima de R$40.000,00. Para a lista abaixo, conte quantos valores existem acima de R$40.000,00, quais são eles, faça a soma desses valores e, no fim, calcule o valor de 30% dessa soma.

R$10.000,00  
R$20.000,00  
R$50.000,00  
R$60.000,00

Resposta: Nessa lista, existem 4 valores. Há 2 valores acima de R$40.000,00, que são R$50.000,00 e R$60.000,00. A soma desses valores é R$110.000,00. O resultado final é 30% desse valor, portanto, 30% de R$110.000,00, que resulta em R$33.000,00.

```

---

Pergunta: Tenho uma lista de valores. O meu resultado final será 30% da soma desses valores. Porém, nem todos os valores serão somados, apenas aqueles acima de R$40.000,00. Para a lista abaixo, conte quantos valores existem acima de R$40.000,00, quais são eles, faça a soma desses valores e, no fim, calcule o valor de 30% dessa soma.

R$31.000,00  
R$15.000,00  
R$52.000,00  
R$103.000,00  
R$42.000,00  
R$156.000,00  
R$15.000,00  
R$27.000,00  
R$82.000,00  
R$33.000,00

Resposta:


# 🧠 Engenharia de Prompt (Prompt Engineering)

**Engenharia de Prompt** é o processo de desenhar instruções (prompts) de forma estratégica para que modelos de linguagem como o ChatGPT, Gemini, Claude ou Llama produzam resultados mais precisos, úteis e coerentes.

Assim como fazemos perguntas diferentes para obter respostas diferentes de uma pessoa, com modelos de IA isso também acontece. A forma como você *constrói* o prompt influencia diretamente a qualidade da resposta.

Este documento explica duas das técnicas mais poderosas em Prompt Engineering: **Chain of Thought Prompting** e **Few-Shot Prompting** — além de como combiná-las para obter resultados excepcionais.

---

## 🔗 Chain of Thought Prompting (Cadeia de Pensamento)

**Chain of Thought Prompting** é uma técnica onde orientamos o modelo a **pensar passo a passo**, explicitando o raciocínio necessário para resolver o problema.

Ou seja, o prompt sugere uma *cadeia lógica de pensamento* que o modelo deve seguir antes de dar a resposta final.

[📄 Artigo Chain of Thought no arXiv](https://arxiv.org/abs/2201.11903)

Essa técnica é ideal para:
- Problemas matemáticos
- Questões de lógica ou raciocínio simbólico
- Decisões complexas ou éticas
- Análises com múltiplas variáveis

💡 **Dica**: Mesmo sem exemplos prévios, adicionar frases como **“explique passo a passo”** ao seu prompt já ativa esse comportamento em modelos mais avançados.

---

## ✍️ Few-Shot Prompting (Prompting com Exemplos)

**Few-shot prompting** é a técnica de fornecer **dois ou mais exemplos completos** de entrada e saída ao modelo, para que ele entenda o padrão desejado antes da tarefa principal.


---

## 🚀 Combinando as Técnicas

Ao combinar **Chain of Thought + Few-shot Prompting**, você oferece ao modelo não apenas o padrão de resposta, mas também **como pensar** para chegar nela.

Essa união produz prompts muito poderosos, principalmente em tarefas com raciocínio complexo.



