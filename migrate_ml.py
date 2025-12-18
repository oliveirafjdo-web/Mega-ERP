"""
Script de migração para adicionar colunas do Mercado Livre na tabela configuracoes
"""
import os
from sqlalchemy import create_engine, text

# Conectar ao banco
raw_db_url = os.environ.get("DATABASE_URL")
if raw_db_url and raw_db_url.startswith("postgres://"):
    raw_db_url = raw_db_url.replace("postgres://", "postgresql+psycopg2://", 1)

DATABASE_URL = raw_db_url or "sqlite:///metrifiy.db"

print(f"🔗 Conectando ao banco...")
engine = create_engine(DATABASE_URL, future=True)

# Adicionar colunas na tabela configuracoes
alteracoes = [
    "ALTER TABLE configuracoes ADD COLUMN IF NOT EXISTS ml_client_id VARCHAR(255)",
    "ALTER TABLE configuracoes ADD COLUMN IF NOT EXISTS ml_client_secret VARCHAR(255)",
    "ALTER TABLE configuracoes ADD COLUMN IF NOT EXISTS ml_access_token VARCHAR(500)",
    "ALTER TABLE configuracoes ADD COLUMN IF NOT EXISTS ml_refresh_token VARCHAR(500)",
    "ALTER TABLE configuracoes ADD COLUMN IF NOT EXISTS ml_token_expira VARCHAR(50)",
    "ALTER TABLE configuracoes ADD COLUMN IF NOT EXISTS ml_user_id VARCHAR(100)",
]

try:
    with engine.begin() as conn:
        print("\n📊 Adicionando colunas do Mercado Livre...")
        
        for sql in alteracoes:
            try:
                conn.execute(text(sql))
                print(f"   ✓ {sql[:60]}...")
            except Exception as e:
                if "already exists" in str(e).lower() or "duplicate column" in str(e).lower():
                    print(f"   ⊘ Coluna já existe (ok)")
                else:
                    print(f"   ⚠ Erro: {e}")
        
        print("\n✅ Migração concluída!")
        
except Exception as e:
    print(f"\n❌ Erro na migração: {e}")
    import traceback
    traceback.print_exc()
