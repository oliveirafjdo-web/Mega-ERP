with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

routes_total = 0
routes_login = 0
routes_protected = 0

for i, line in enumerate(lines):
    if '@app.route' in line:
        routes_total += 1
        
        if '/login' in line or '/logout' in line:
            routes_login += 1
            continue
            
        # Verificar se tem @login_required na próxima linha
        if i + 1 < len(lines) and '@login_required' in lines[i + 1]:
            routes_protected += 1
        # Ou na linha seguinte (caso tenha outro decorator)
        elif i + 2 < len(lines) and '@login_required' in lines[i + 2]:
            routes_protected += 1

routes_necessitam = routes_total - routes_login

print(f'Total de rotas: {routes_total}')
print(f'Rotas login/logout: {routes_login}')
print(f'Rotas que necessitam proteção: {routes_necessitam}')
print(f'Rotas protegidas: {routes_protected}')
print()

if routes_protected >= routes_necessitam:
    print('✅ TODAS AS ROTAS ESTÃO PROTEGIDAS!')
else:
    print(f'❌ FALTAM {routes_necessitam - routes_protected} ROTAS')
