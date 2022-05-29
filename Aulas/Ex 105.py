def notas(*num, sit = False):
    """
    notas(*num, sit = False)
    :param num: Notas a receber
    :param sit: Mostra a situação (RUIM, RAZOÁVEL, BOA)
    :return: DICIÓNARIO com Total de notas, maior nota, menor nota, media de nota.
    """
    aluno = dict()
    nota = num
    aluno['total'] = len(num)
    nmax = nmin = soma =  0
    for i in (num):
        soma += i
        if i > nmax:
            nmax = i
            aluno['maior'] = nmax
        if i > nmin and nmin == 0 or i < nmin:
            nmin = i
            aluno['menor'] = nmin
        aluno['media'] = soma / aluno['total']
    if sit:
        if aluno['media'] <= 5:
            aluno['situação'] = 'RUIM'
        elif aluno['media'] > 5  and aluno['media'] < 7:
            aluno['situação']  = 'RAZOÁVEL'
        elif aluno['media'] >= 7:
            aluno['situação'] = 'BOA'

    return aluno
#programa principal
resp = notas(7,7,4,8,10, 2, 3, 5, 1, 5, 1, 5,1 ,3 ,5 , 3)
print(resp)
