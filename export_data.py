"""
Script para exportar dados do SQLite para JSON
Para usar: python export_data.py
"""
import sqlite3
import json
import os

def export_sqlite_to_json():
    """Exporta todas as tabelas do SQLite para JSON"""
    
    db_path = "metrifiy.db"
    if not os.path.exists(db_path):
        print(f"❌ Banco de dados não encontrado: {db_path}")
        return
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Para acessar colunas por nome
    cursor = conn.cursor()
    
    # Obter lista de tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = [row[0] for row in cursor.fetchall()]
    
    print(f"📊 Encontradas {len(tables)} tabelas para exportar")
    
    data_export = {}
    
    for table in tables:
        print(f"  → Exportando tabela: {table}")
        
        # Obter dados da tabela
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        
        # Converter para lista de dicionários
        table_data = []
        for row in rows:
            row_dict = {}
            for key in row.keys():
                value = row[key]
                # Converter date/datetime para string
                if value is not None and isinstance(value, (int, float, str)):
                    row_dict[key] = value
                else:
                    row_dict[key] = str(value) if value is not None else None
            table_data.append(row_dict)
        
        data_export[table] = table_data
        print(f"    ✓ {len(table_data)} registros exportados")
    
    conn.close()
    
    # Salvar em JSON
    output_file = "data_export.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data_export, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Dados exportados com sucesso para: {output_file}")
    print(f"📦 Tamanho do arquivo: {os.path.getsize(output_file) / 1024:.2f} KB")
    
    # Mostrar resumo
    print("\n📋 Resumo da exportação:")
    for table, data in data_export.items():
        print(f"  • {table}: {len(data)} registros")

if __name__ == "__main__":
    export_sqlite_to_json()
