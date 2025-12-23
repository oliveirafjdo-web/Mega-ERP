# Mega-ERP

MetriFy ERP — versão local empacotada para migração.

Conteúdo:
- Aplicação Flask para gestão de vendas, estoque e financeiro.
- Banco local: `metrifiy.db` (SQLite). Para produção, use Postgres/Render.

Rápido:

1. Instale dependências:

```bash
pip install -r requirements.txt
```

2. Rodar local (desenvolvimento):

```bash
python app.py
```

3. Backup/Export para Render:

```bash
python backup_banco.py            # gera backups/metrifiy_backup_*.db
python -m app gerar_export_render # (ou use /admin/backup) gera ZIP com CSVs
python import_render_backup.py backups/metrifiy_render_export_YYYYMMDD_HHMMSS.zip --database-url "<DATABASE_URL>"
```

Arquivos importantes:
- `metrifiy.db` — banco SQLite local
- `backups/` — backups e export ZIPs
- `import_render_backup.py` — importa ZIP para Postgres

Licença: privado
# MetriFy ERP

Versão ajustada com:

- Lucro líquido no dashboard
- Comissão estimada total
- Imposto sobre receita bruta
- Despesas sobre receita líquida (receita - comissão)
- Relatório de lucro com totais por produto e totais gerais
- Filtro de data em vendas e relatório de lucro

## Backup e migração para Render (Postgres)
- Local: acesse **Admin → Backup** e clique em **Exportar pacote Render (ZIP)** para gerar CSVs + manifest.
- Suba o ZIP para o servidor Render (shell ou deploy) e rode `python import_render_backup.py <arquivo.zip>` usando o `DATABASE_URL` do Render.
- Para backup apenas do SQLite local, use **Fazer Backup SQLite** ou execute `python backup_banco.py`.
- Para restaurar localmente (SQLite), use **Restaurar backup** em **Admin → Backup** enviando um `.db` (o banco atual é salvo antes de sobrescrever).
