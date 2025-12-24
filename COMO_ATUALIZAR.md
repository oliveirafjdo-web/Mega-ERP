# 🔄 Como Atualizar o Sistema Online

## Fluxo de Atualização Automática

Sempre que você fizer alterações no código aqui e enviar para o GitHub, o Render **detecta automaticamente** e faz o deploy da nova versão!

---

## 📝 Passo a Passo para Atualizar

### 1. Fazer Alterações no Código
- Edite qualquer arquivo (.py, .html, etc.)
- Teste localmente se quiser

### 2. Enviar para o GitHub
Execute estes comandos no terminal:

```bash
# Adicionar todos os arquivos modificados
git add .

# Criar commit com mensagem descritiva
git commit -m "Descrição da alteração feita"

# Enviar para o GitHub
git push origin main
```

### 3. Deploy Automático no Render
- ✅ O Render detecta a mudança automaticamente
- ✅ Faz o build e deploy da nova versão
- ✅ Em 2-3 minutos, seu site está atualizado!

---

## 🎯 Exemplo Prático

**Você alterou o arquivo `app.py`:**

```bash
# Salvar a alteração no Git
git add app.py
git commit -m "Corrigido bug no cálculo de estoque"
git push origin main
```

**Pronto!** Em 2-3 minutos a alteração estará online! 🎉

---

## ⚡ Comandos Rápidos

### Atualizar tudo de uma vez:
```bash
git add . ; git commit -m "Atualizações gerais" ; git push origin main
```

### Ver o que foi modificado:
```bash
git status
```

### Ver histórico de alterações:
```bash
git log --oneline
```

---

## 🔍 Acompanhar o Deploy

1. Acesse: https://dashboard.render.com
2. Clique no seu Web Service (`erp-metrifiy`)
3. Veja os **"Events"** para acompanhar o deploy em tempo real
4. Quando aparecer "Deploy live", a atualização foi aplicada!

---

## ⚠️ Importante

- **Banco de dados NÃO é afetado** - seus dados permanecem intactos
- **Uploads são perdidos** - o Render Free não tem armazenamento persistente
- **Variáveis de ambiente** - não precisam ser reatualizadas

---

## 🆘 Problemas?

Se o deploy falhar:
1. Veja os logs no Render Dashboard
2. Corrija o erro localmente
3. Faça novo commit e push
4. O Render tenta novamente automaticamente

---

**Dica:** Sempre teste alterações críticas localmente antes de enviar para produção!
