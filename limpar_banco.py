"""
Script para limpar o banco de dados (deletar produtos, vendas e transações)
Mantém usuários e estrutura das tabelas
"""
import os
import sys
from sqlalchemy import create_engine, text, inspect

# Conectar ao banco de dados
raw_db_url = os.environ.get("DATABASE_URL")
if raw_db_url and raw_db_url.startswith("postgres://"):
    raw_db_url = raw_db_url.replace("postgres://", "postgresql+psycopg2://", 1)

DATABASE_URL = raw_db_url or "sqlite:///metrifiy.db"

print(f"🔗 Conectando ao banco...")
print(f"   {DATABASE_URL[:40]}...")

try:
    engine = create_engine(DATABASE_URL, future=True)
    
    # Verificar quais tabelas existem
    inspector = inspect(engine)
    tabelas_existentes = inspector.get_table_names()
    print(f"\n📋 Tabelas encontradas: {', '.join(tabelas_existentes)}")
    
    with engine.begin() as conn:
        print("\n🗑️  Limpando dados das tabelas...")
        
        # Deletar dados na ordem correta (respeitando foreign keys)
        tabelas_para_limpar = [
            "finance_transactions",
            "vendas", 
            "produtos",
        ]
        
        total_deletados = 0
        for tabela in tabelas_para_limpar:
            if tabela in tabelas_existentes:
                result = conn.execute(text(f"DELETE FROM {tabela}"))
                deletados = result.rowcount
                total_deletados += deletados
                print(f"   ✓ {tabela}: {deletados} registros deletados")
            else:
                print(f"   ⊘ {tabela}: não existe")
        
        print(f"\n✅ Banco limpo com sucesso!")
        print(f"   Total de registros deletados: {total_deletados}")
        print(f"   Usuários mantidos: ✓")
        print(f"\n💡 Você pode fazer novas importações agora.")
        
except Exception as e:
    print(f"\n❌ Erro ao limpar banco: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
