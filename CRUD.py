import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="051220",
    database="academiaturmab"
)
print(banco)


def menu():
    print("▬" * 35)
    print("️ ️‍️‍🏋️‍♂️ 💪 ACADEMIA 💪🏋️‍♂️")
    print("♦" * 35)
    print("[1] Inserir")
    print("[2] Remover")
    print("[3] Procurar")
    print("[0] Sair")
    print("♦" * 35)



meucursor = mysql.connector
loop = True
while loop:
    menu()
    escolha = input("Digite o dígito da operação que deseja efetuar: ")
    while True:
        print("♦" * 35)
        print("Qual será o tipo de dado?")
        print("♦" * 35)
        print("[1] Aluno")
        print("[2] Funcionário")
        print("[3] Modalidade")
        print("[4] Personal")
        print("♦" * 35)
        type = int(input("Digite aqui: "))
        if type == 1:
            table = "alunos"
            break
        if type == 2:
            table = "funcionarios"
            break
        if type == 3:
            table = "modalidades"
            break
        if type == 4:
            table = "personal"
            break
        else:
            print("Digite um dígito válido.")
    #Inserir
    if escolha == "1":
        if table == "alunos":
            nome = input("Digite o nome do aluno: ")
            telefone = input(f"Digite o telefone do aluno {nome}: ")
            endereco = input(f"Digite o endereço do aluno {nome}: ")
            cpf = input(f"Digite o CPF do aluno {nome}: ")
            email = input(f'Digite o email do aluno {nome}: ')
            data = (nome, telefone, endereco, cpf, email)
            sql = "INSERT INTO alunos (NOME, TELEFONE, ENDEREÇO, CPF, EMAIL) VALUES (%s, %s, %s, %s, %s)"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print(" ALUNO ADICIONADO COM SUCESSO!")
        if table == "personal":
            nome = input("Digite o nome do personal: ")
            cpf = input(f"Digite o CPF do personal {nome}: ")
            cref = input(f"Digite o CREF do personal {nome}: ")
            telefone = input(f"Digite o telefone do personal {nome}: ")
            endereco = input(f"Digite o endereço do personal {nome}: ")
            data = (cpf, cref, nome, telefone, endereco)
            sql = "INSERT INTO personal (CPF, CREF, NOME, TELEFONE, ENDEREÇO) VALUES (%s, %s, %s, %s, %s)"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print("PERSONAL ADICIONADO COM SUCESSO!")
        if table == "funcionarios":
            nome = input("Digite o nome do funcionario: ")
            cpf = input(f"Digite o CPF do funcionario {nome}: ")
            salario = input(f"Digite o salario do funcionario {nome}: ")
            departamento = input(f"Digite o departamento do funcionario {nome}: ")
            data = (nome, cpf, salario, departamento)
            sql = "INSERT INTO funcionarios (NOME, CPF, SALARIO, DEPARTAMENTO) VALUES (%s, %s, %s, %s)"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print("FUNCIONÁRIO ADICIONADO COM SUCESSO!")
        if table == "modalidades":
            nome = input("Digite o nome da modalidade: ")
            desc = input(f"Digite a descrição da modalidade {nome}:")
            duracao = input(f"Digite a duração da modalidade {nome}: ")
            val = (nome, desc, duracao)
            sql = "INSERT INTO modalidades (NOME, DESCRICAO, DURACAO) VALUES (%s, %s, %s)"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print("MODALIDADE ADICIONADA COM SUCESSO!")
    #Remover
    elif escolha == "2":
        if table == "alunos":
            valor = input("Digite a matrícula do aluno que deseja remover: ")
            data = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print("ALUNO REMOVIDO COM SUCESSO!")
        if table == "personal":
            valor = input("Digite o CREF do personal que deseja remover: ")
            data = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print("PERSONAL REMOVIDO COM SUCESSO!")
        if table == "funcionarios":
            valor = input("Digite o ID do funcionário que deseja remover: ")
            data = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print("FUNCIONÁRIO REMOVIDO COM SUCESSO!")
        if table == "modalidades":
            valor = input("Digite o ID da modalidade que deseja remover: ")
            data = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            meucursor.execute(sql, data)
            banco.commit()
            print("♦" * 35)
            print("MODALIDADE REMOVIDA COM SUCESSO!")
    #Procurar
    elif escolha == "3":
        if table == "alunos":
            meucursor.execute(f"SELECT * FROM {table}")
            resultado = meucursor.fetchall()

            for aluno in resultado:
                print("♦" * 35)
                print(f"MATRÍCULA: {aluno[0]}")
                print(f"NOME: {aluno[1]}")
                print(f"TELEFONE: {aluno[2]}")
                print(f"ENDEREÇO: {aluno[3]}")
                print(f"CPF: {aluno[4]}")
                print(f"EMAIL: {aluno[5]}")
                print("♦" * 35)
        if table == "personal":
            meucursor.execute(f"SELECT * FROM {table}")
            resultado = meucursor.fetchall()

            for personal in resultado:
                print("♦" * 35)
                print(f"NOME: {personal[0]}")
                print(f"CPF: {personal[1]}")
                print(f"CREF: {personal[2]}")
                print(f"TELEFONE: {personal[3]}")
                print(f"ENDEREÇO: {personal[4]}")
                print("♦" * 35)
        if table == "modalidades":
            meucursor.execute(f"SELECT id, nome, descricao, duracao FROM {table}")
            resultado = meucursor.fetchall()

            for modalidade in resultado:
                print("♦" * 35)
                print(f"ID: {modalidade[0]}")
                print(f"NOME: {modalidade[1]}")
                print(f"DESCRIÇÃO: {modalidade[2]}")
                print(f"DURAÇÃO: {modalidade[3]}")
                print("♦" * 35)
        if table == "funcionarios":
            meucursor.execute(f"SELECT id, nome, cpf, salario FROM {table}")
            resultado = meucursor.fetchall()

            for funcionario in resultado:
                print("♦" * 35)
                print(f"ID: {funcionario[0]}")
                print(f"NOME: {funcionario[1]}")
                print(f"CPF: {funcionario[2]}")
                print(f"SALÁRIO: {funcionario[3]}")
                print("♦" * 35)
    elif escolha == "4":
        while True:
            doubt = input("DESEJA SAIR? DIGITE 1 PARA CONFIRMAR OU 2 PARA VOLTAR AO MENU.")
            if doubt != "1" and doubt != "2":
                ...
            else:
                break
        if doubt == "1":
            break
        if doubt == "2":
            ...
print("Programa finalizado!")