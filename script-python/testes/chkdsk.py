p = str(input('C:\Users\User>'))
if p == 'chkdsk /f /c':
    sn = str(input('''Não é possível executar o CHKDSK porque o volume está sendo usado por outro
processo. Deseja agendar a verificação
deste volume para a próxima vez em que o sistema for reiniciado? (S/N)''')).strip().upper()
while not sn in (SN):
    str(input('''Não é possível executar o CHKDSK porque o volume está sendo usado por outro
processo. Deseja agendar a verificação
deste volume para a próxima vez em que o sistema for reiniciado? (S/N)''')).strip().upper()
        
