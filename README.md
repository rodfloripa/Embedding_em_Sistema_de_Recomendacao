# Superlinked: Resolvendo o Cold Start de Produtos

<div align="justify">

Este sistema aborda diretamente um dos maiores desafios em algoritmos de recomendação: o **Cold Start** (Início a Frio). O fenômeno ocorre quando o sistema não possui dados históricos suficientes para tomar decisões precisas. No nosso modelo, focamos na solução do tipo mais comum em inventários dinâmicos.

Para rodar:

docker build -t meu-jupyter-superlinked .

docker run -p 8888:8888 --name jupyter-ai meu-jupyter-superlinked

---

## ❄️ O Cold Start de Produto (Resolvido ✅)

Em sistemas tradicionais de recomendação (conhecidos como *Collaborative Filtering*), um produto novo é tecnicamente "invisível". Como ninguém clicou, visualizou ou comprou o item ainda, o algoritmo não possui conexões para saber a quem recomendá-lo.



### Como o código resolve este problema:

Diferente das abordagens legadas, utilizamos a **Busca Semântica baseada em Vetores**. Isso elimina a dependência de cliques e foca na essência do item.

1.  **Extração do "DNA" do Produto:** Através do processamento de linguagem natural (NLP), o sistema identifica características fundamentais na descrição (ex: *alta performance*, *esportivo*, *conforto*).
2.  **Mapeamento Imediato:** Esse "DNA" é convertido em um vetor numérico e comparado instantaneamente com os perfis de usuários já existentes no banco de dados.
3.  **Resultado:** O produto torna-se "recomendável" no exato momento em que entra no sistema, sem a necessidade de uma única interação humana prévia.

---

## 📊 Comparativo de Eficácia

| Problema | Status | Estratégia do Código |
| :--- | :--- | :--- |
| **Produto Novo** | **Resolvido** | Usa a descrição textual para mapeamento semântico imediato. |
| **Itens de Nicho** | **Resolvido** | Itens com poucas vendas são recomendados pela afinidade de conteúdo. |
| **Usuário Novo** | **Pendente** | Requer ao menos uma interação inicial ou metadados de perfil. |

</div>

---

> **Nota Técnica:** Ao utilizar o Superlinked, a barreira do "silêncio de dados" é quebrada pela semântica, permitindo que novos inventários tenham tração imediata com o público-alvo correto.

<div align="justify">

O código implementado representa um sistema de **Recomendação Baseada em Conteúdo (Content-Based Recommendation)**. 

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


