from Connection import DBConnection
from Lista import Lista
from Item import Item

class ListaDAO:
    def __init__(self):
        self.dbConn = DBConnection('localhost', 'alg_Prog_2', 'root', '')
        self.dbConn.getConn()
        

    def insertLista(self, obj):
        self.lista = obj
        query = "INSERT INTO lista (listName, createDate, listStatus) VALUES (%s, %s, %s)"
        parameters = (self.lista.listName, self.lista.createDate, self.lista.status)
        cursor = self.dbConn.getCursor()
        cursor.execute(query, parameters)
        self.dbConn.getCommit()
        return cursor.lastrowid

    def getListIdByName(self, listName):
        nome = listName
        query = "SELECT id FROM lista WHERE listStatus = 'Open' AND listName = %s"
        parameters = nome
        cursor = self.dbConn.getCursor()
        cursor.execute(query, (parameters,))
        result = cursor.fetchone()[0]
        return result

    def appendItem(self, obj):
        self.item = obj
        query = "INSERT INTO itemlista (idLista, item, quantidade, itemStatus) VALUES (%s, %s, %s, %s)"
        parameters = (self.item.idLista, self.item.item, self.item.quantidade, self.item.status)
        cursor = self.dbConn.getCursor()
        cursor.execute(query, parameters)
        self.dbConn.getCommit()

    def getItensFromLista(self, idList):
        length = self.getListlength(idList)
        if length == 0:
            print("Lista não possui itens não marcardos")
        else:
            query = "SELECT id, item, quantidade, itemStatus FROM itemlista WHERE itemStatus = 'Not Picked' AND idLista = %s"
            parameters = idList
            cursor = self.dbConn.getCursor()
            cursor.execute(query, (parameters,))
            result = cursor.fetchall()
            
            header = ('Id', 'Item', 'Quantidade', 'Status')
            print('{:<5} {:<20} {:<8} {:>16}'.format(*header))
            for p in result:
                linha = (p[0], p[1].decode(), p[2].decode(), p[3].decode())
                print('{:<5} {:<20} {:<16} {:>10}'.format(*linha))

    def showLists(self):
        query = "SELECT id, listName, createDate, listStatus FROM lista"
        cursor = self.dbConn.getCursor()
        cursor.execute(query)
        result = cursor.fetchall()

        header = ('id', 'Lista', 'Data', 'Status')
        print('{:<5} {:<20} {:^12} {:>16}'.format(*header))
        for x in result:
            linha = (x[0], x[1].decode(), str(x[2]), x[3].decode())
            print('{:<5} {:<20} {:>12} {:>16}'.format(*linha))

    def closeLista(self, id):
        query = "UPDATE lista SET listStatus = 'Done' WHERE id = %s"
        parameters = id
        cursor = self.dbConn.getCursor()
        cursor.execute(query, (parameters,))
        self.dbConn.getCommit()
        status = self.checkListStatus(id)
        if status == 'Done':
            print("Lista Atualizada com sucesso")
        else:
            print("Erro ao atualizar lista")

    def checkListStatus(self, id):
        query = "SELECT listStatus FROM lista WHERE id = %s"
        parameters = id
        cursor = self.dbConn.getCursor()
        cursor.execute(query, (parameters,))
        result = cursor.fetchone()[0].decode()
        return result

    def checkedItem(self, id):
        query = "UPDATE itemlista SET itemStatus = 'Picked' WHERE id = %s"
        parameters = id
        cursor = self.dbConn.getCursor()
        cursor.execute(query, (parameters,))
        self.dbConn.getCommit()

    def getListlength(self, id):
        query = "SELECT COUNT(id) total FROM itemlista WHERE itemStatus = 'Not Picked' AND idLista = %s"
        parameters = id
        cursor = self.dbConn.getCursor()
        cursor.execute(query, (parameters,))
        result = cursor.fetchone()[0]
        return result