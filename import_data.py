"""
Script para importar dados do JSON para PostgreSQL
Para usar depois do deploy:
1. Configure a variável DATABASE_URL com a URL do PostgreSQL do Render
2. Execute: python import_data.py
"""
import os
import json
import sys
from sqlalchemy import create_engine, MetaData, Table, inspect, text

def import_json_to_postgres():
    """Importa dados do JSON para PostgreSQL"""
    
    # Obter URL do banco
    database_url = os.environ.get("DATABASE_URL")
    
    if not database_url:
        print("❌ Erro: Variável DATABASE_URL não configurada")
        print("Configure com: $env:DATABASE_URL='sua-url-postgresql'")
        return False
    
    # Ajustar URL para SQLAlchemy
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+psycopg2://", 1)
    
    print(f"🔗 Conectando ao PostgreSQL...")
    
    try:
        engine = create_engine(database_url)
        metadata = MetaData()
        metadata.reflect(bind=engine)
        
        print(f"✅ Conectado com sucesso!")
        
        # Carregar dados do JSON
        json_file = "data_export.json"
        if not os.path.exists(json_file):
            print(f"❌ Arquivo não encontrado: {json_file}")
            return False
        
        print(f"\n📂 Carregando dados de: {json_file}")
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"📊 Encontradas {len(data)} tabelas no arquivo")
        
        # Importar dados
        with engine.begin() as conn:
            for table_name, rows in data.items():
                if not rows:
                    print(f"  ⊘ {table_name}: Sem dados para importar")
                    continue
                
                print(f"  → Importando {table_name}: {len(rows)} registros...")
                
                # Verificar se tabela existe
                if table_name not in metadata.tables:
                    print(f"    ⚠️ Tabela {table_name} não existe no PostgreSQL")
                    continue
                
                table = metadata.tables[table_name]
                
                # Limpar tabela antes de importar (opcional)
                # conn.execute(table.delete())
                
                try:
                    # Inserir dados em lotes
                    batch_size = 500
                    for i in range(0, len(rows), batch_size):
                        batch = rows[i:i+batch_size]
                        conn.execute(table.insert(), batch)
                    
                    print(f"    ✓ {len(rows)} registros importados")
                    
                except Exception as e:
                    print(f"    ❌ Erro ao importar {table_name}: {e}")
                    continue
        
        print(f"\n✅ Importação concluída com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao conectar/importar: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = import_json_to_postgres()
    sys.exit(0 if success else 1)
