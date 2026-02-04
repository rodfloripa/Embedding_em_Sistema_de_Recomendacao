

import time
from superlinked.framework.dsl.index.index import Index
from superlinked.framework.dsl.executor.in_memory.in_memory_executor import InMemoryExecutor
from superlinked.framework.dsl.source.in_memory_source import InMemorySource
from superlinked.framework.dsl.space.text_similarity_space import TextSimilaritySpace
from superlinked.framework.dsl.query.query import Query
from superlinked.framework.common.schema.schema import Schema
from superlinked.framework.common.schema.schema_factory import SchemaFactory
from superlinked.framework.common.schema.schema_type import SchemaType

# Imports resilientes
from superlinked.framework.common.schema.schema_object import String, SchemaField
try:
    from superlinked.framework.common.schema.id_schema_object import IdField
except ImportError:
    IdField = SchemaField

# 1. Definição dos Schemas
class PerfilUsuario(Schema):
    id: IdField
    historico_texto: String # Aqui acumulamos as descrições do que ele comprou

# Registro
SchemaFactory.calculate_schema_information(PerfilUsuario, SchemaType.SCHEMA)
u = PerfilUsuario()

# 2. Espaço e Índice
modelo = "sentence-transformers/all-MiniLM-L6-v2"
space_perfil = TextSimilaritySpace(text=u.historico_texto, model=modelo)
index_usuario = Index(space_perfil)

# 3. Setup
source_u = InMemorySource(u)
executor = InMemoryExecutor(sources=[source_u], indices=[index_usuario])
app = executor.run()

# 4. Dados Fictícios
# Simulando o Marcos (comprou Bola) e a Julia (comprou Guitarra)
source_u.put([
    {"id": "user_marcos", "historico_texto": "Bola de futebol profissional de couro equipamento esportivo"},
    {"id": "user_julia", "historico_texto": "Guitarra elétrica com distorção pesada instrumento musical de cordas"},
    {"id": "user_maria", "historico_texto": "Playstation"}
])

time.sleep(1)

# 5. O Novo Produto chegando ao sistema
novo_produto = "Tênis de alta performance para corrida e maratonas esportivas"

# 

query_match = (
    Query(index_usuario, weights={space_perfil: 1.0})
    .find(u)
    .similar(space_perfil, novo_produto)
)

resultados = app.query(query_match)

# 6. Exibição
print(f"--- ANALISANDO DESTINO PARA: {novo_produto} ---")
entries = getattr(resultados, 'entries', [])
if not entries:
    print("Nenhum match encontrado.")
else:
    for entry in entries:
        uid = getattr(entry, 'id', 'N/A')
        score = getattr(entry, 'score', 0)
        if score == 0 and hasattr(entry, 'metadata'):
            score = entry.metadata.score
        print(f"-> Usuário Recomendado: {uid} (Afinidade: {score:.4f})")
