# Sistema de Recomendação Reversa com Superlinked

<div align="justify">

O código implementado representa um sistema de **Recomendação Baseada em Conteúdo (Content-Based Recommendation)** operando de forma invertida. Em vez da abordagem tradicional de perguntar *"o que este usuário gostaria de comprar?"*, mudamos o foco para o produto: *"quais usuários possuem um perfil que combina com este novo item?"*.

---

## 🧠 Como o sistema funciona nos bastidores

### 1. Modelagem Semântica (O "Cérebro")
O coração do sistema é o **Schema** do usuário, focado no campo `historico_texto`. Utilizamos o modelo de *Deep Learning* `all-MiniLM-L6-v2`, que atua como um tradutor de linguagem natural para vetores (listas de números).

A grande vantagem desta abordagem é a **compreensão contextual**: o sistema entende que termos como "futebol" e "maratona" pertencem ao universo semântico de "esportes", permitindo conexões que uma busca por palavra-chave simples ignoraria.



### 2. Construção do Perfil (A "Identidade")
Ao alimentar o sistema com dados de compras ou interesses, criamos **âncoras** no espaço vetorial. O perfil de cada usuário é a soma semântica do seu histórico:
* **Perfil Marcos:** O vetor é posicionado próximo a conceitos de performance, artigos esportivos e couro.
* **Perfil Julia:** O vetor é atraído para a vizinhança de instrumentos musicais, cordas e cultura rock.

### 3. A Query de "Matchmaking"
Quando um `novo_produto` (ex: *"Tênis de maratona"*) é inserido, o Superlinked executa os seguintes passos:
1.  **Vetorização:** Converte a descrição do produto em um vetor numérico.
2.  **Similaridade de Cosseno:** Compara o vetor do produto com os vetores de todos os usuários.
3.  **Cálculo Geométrico:** O sistema mede o "ângulo" entre os vetores. No espaço vetorial, **proximidade geométrica significa afinidade de interesse**.



### 4. Ranking de Afinidade
O resultado é uma lista ranqueada por relevância técnica:
* **Vencedor:** O usuário cujo histórico "aponta" para a mesma direção semântica do novo produto.
* **Resultado Prático:** Marcos recebe a recomendação do tênis porque seu histórico esportivo é matematicamente compatível, enquanto Julia é descartada para este item específico por sua distância temática.

---

## 🚀 Vantagens sobre a busca tradicional

Diferente dos sistemas legados baseados em palavras-chave exatas (onde oferecer um "calçado" para quem comprou uma "bola" poderia falhar), o Superlinked utiliza o **contexto**. Isso elimina o problema de sinônimos e permite recomendações muito mais humanas e precisas.

</div>

---

> **Próximo Passo Sugerido:** > Implementar um gatilho automático de notificação. Deseja adaptar o código para que o sistema dispare um alerta sempre que a afinidade (score) entre um novo produto e um usuário ultrapassar **0.5**?
