import mysql.connector as connector
import pandas as pd
# sistema de concessionaria


def connection():
    cnx = connector.connect(user='root', password='',
                            host='localhost', database='aula9')
    return cnx


def create_table(cnx):
    cursor = cnx.cursor()
    query = ('CREATE TABLE IF NOT EXISTS carro(\
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    marca TEXT NOT NULL, \
    modelo TEXT NOT NULL, \
    ano TEXT, \
    valor DECIMAL(10,2)\
    )')
    cursor.execute(query)


def insert_car(cnx, car):
    cursor = cnx.cursor()
    insert = ('INSERT INTO carro(marca, modelo, ano, valor) VALUES(%s, %s, %s, %s)')
    data = (car['marca'], car['modelo'], car['ano'], car['valor'])
    cursor.execute(insert, data)
    cnx.commit()


def update_car(cnx, id_carro, car):
    cursor = cnx.cursor()
    update = ('UPDATE carro SET marca = %s , modelo = %s, ano = %s, valor = %s WHERE id =' + id_carro)
    print (update)
    data = (car['marca'], car['modelo'], car['ano'], car['valor'])
    cursor.execute(update, data)
    cnx.commit()


def delete_car(cnx, id_carro):
    cursor = cnx.cursor()
    delete_c = ('DELETE FROM carro WHERE id =' + id_carro)
    cursor.execute(delete_c)
    cnx.commit()


def search_car(cnx, modelo):
    cursor = cnx.cursor()
    query = ('select * from carro where modelo like "' + modelo + '"')
    cursor.execute(query)
    df = pd.DataFrame(list(cursor), columns = ['ID', 'Marca', 'Modelo','Ano', 'Valor'])
    df = df.sort_values('ID')
    return df

def lista_carros(cnx):
    cursor = cnx.cursor()
    query = ('select * from carro')
    cursor.execute(query)
    df = pd.DataFrame(list(cursor), columns = ['ID', 'Marca', 'Modelo','Ano', 'Valor'])
    df = df.sort_values('ID')
    return df


def desconnect(cnx):
    cnx.close()

if __name__ == '__main__':
    
    connector = connection()
    create_table(connector)
    option = 10

    while option>0:
        
        print()
        print('0 - Sair')
        print('1 - Cadastrar carro')
        print('2 - Atualizar carro')
        print('3 - Buscar carro')
        print('4 - Deletar carro')
        print('5 - Listar todos os carros')
        option = int(input('Escolha um numero da opção: '))
        print()

        if option == 1:
            marca = input('Digite a marca do carro: ')
            modelo = input('Digite a modelo do carro: ')
            ano = input('Digite a ano do carro: ')
            valor = input('Digite a valor do carro: ')
            insert_car(connector, {
                'marca': marca,
                'modelo': modelo,
                'ano': ano,
                'valor': valor
            })
        elif option == 2:
            
            print(lista_carros(connector))
            print()


            id_carro = input('Digite o ID do carro que quer alterar: ')
            print()

            marca = input('Digite a marca do carro: ')
            modelo = input('Digite a modelo do carro: ')
            ano = input('Digite a ano do carro: ')
            valor = input('Digite a valor do carro: ')

            update_car(connector, id_carro, {
                'marca': marca,
                'modelo': modelo,
                'ano': ano,
                'valor': valor
            })

        elif option == 3:
            carro = input('Digite o modelo do carro que quer exibir: ')
            print()
            
            print(search_car(connector,carro))


        elif option == 4:
            
            print(lista_carros(connector))
            print()

            id_carro = input('Digite o ID do carro que quer excluir: ')

            delete_car(connector,id_carro)

        elif option == 5:
            
            print(lista_carros(connector))
        elif option == 0:
            pass
        else:
            print('Digite uma opção valida, na proxima vez!')
    desconnect(connector)
