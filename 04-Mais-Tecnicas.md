# 🧠 Técnicas Avançadas de Engenharia de Prompt

Este documento apresenta **três técnicas poderosas** para melhorar a capacidade de raciocínio e a confiabilidade das respostas em modelos de linguagem (LLMs):  
**Least-to-Most Prompting**, **Chain of Verification** e **Self-Consistency**.

---

## 🔁 Least-to-Most Prompting (Do Mais Fácil ao Mais Difícil)

Essa técnica resolve problemas complexos ao **dividi-los em etapas menores**, começando pelos subproblemas mais simples e avançando até os mais difíceis.  
A ideia é construir o raciocínio gradualmente, passo a passo.

✅ **Ideal para:**
- Problemas matemáticos complexos  
- Questões de lógica ou programação  
- Explicações educacionais estruturadas  

---

## ✅ Chain of Verification (Cadeia de Verificação)

Essa abordagem busca aumentar a **confiança nas respostas** por meio de um processo de auto-verificação.

### Como funciona:
1. 📝 **Resposta Inicial**  
   O modelo responde normalmente à pergunta principal.

2. ❓ **Geração de Perguntas de Verificação**  
   Ele cria perguntas específicas para validar partes da própria resposta.

3. 🔍 **Execução das Verificações**  
   Ele responde a essas novas perguntas para checar a coerência.

4. ✅ **Resposta Final Verificada**  
   Com base nas verificações, ele ajusta ou confirma sua resposta.

**Aplicações comuns:**  
Verificação de código, análises complexas, tomadas de decisão com múltiplos critérios.

---

## 🔄 Self-Consistency (Autoconsistência)

Em vez de gerar apenas uma resposta, o modelo é executado **várias vezes com o mesmo prompt**.  
Depois, com base em todas as respostas geradas, é escolhida aquela que aparece com mais frequência (como uma votação).

💡 Isso reduz o efeito da aleatoriedade e melhora a **precisão e estabilidade** das respostas.

✅ **Muito útil para:**
- Problemas de matemática e lógica  
- Questões simbólicas ou estruturadas  
- Tarefas que exigem consistência nas decisões  

---

## 📦 Resumo Geral

| Técnica                  | Objetivo Principal                            | Melhor Aplicação                           |
|--------------------------|-----------------------------------------------|--------------------------------------------|
| Least-to-Most Prompting  | Resolver por etapas crescentes de dificuldade | Raciocínio complexo e educativo             |
| Chain of Verification    | Validar a resposta com perguntas auxiliares   | Verificação de código, análise crítica      |
| Self-Consistency         | Obter consenso entre múltiplas execuções      | Lógica matemática, tarefas determinísticas  |

---

### 🧠 Em engenharia de prompt, não basta perguntar — é preciso **ensinar o modelo a pensar, verificar e decidir melhor**.
