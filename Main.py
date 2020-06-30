from ListaDAO import ListaDAO
from Lista import Lista
from datetime import date
from Item import Item


class App:
    def __init__(self):

        self.listaDao = ListaDAO()

    def criaLista(self):
        nome = input("Informe o nome da Lista: ")
        today = date.today()
        status = 'Open'
        lista = Lista(None, nome, today, status)
        lista.id = self.listaDao.insertLista(lista)
        
        self.putItemLista(lista.id)

    def putItemLista(self, id):
        self.id = id
        option = 1
        while option != 0:
            self.item = Item()
            produto = input("Informe o produto para inserir na lista: ")
            qtd = input("Informe a quantidade do produto: ")
            st = 'Not Picked'
            self.item.id = None
            self.item.idLista = self.id
            self.item.item = produto
            self.item.quantidade = qtd
            self.item.status = st
            self.listaDao.appendItem(self.item)
            option = int(input("Deseja inserir outro produto? 1-Sim | 0-Não "))

    def marcaProdutoLIsta(self):
        option = 1
        self.listaDao.showLists()
        escolha = int(input("Informe o id da lista para marcar os produtos: "))
        
        while option != 0:
            self.listaDao.getItensFromLista(escolha)
            prodId = int(input("Informe o id do produto pego: "))
            self.listaDao.checkedItem(prodId)
            option = int(input("Deseja marcar outro produto? 1-Sim | 0-Não "))

    def closeLista(self):
        self.listaDao.showLists()
        escolha = int(input("Informe o id da lista para encerrar: "))
        self.listaDao.closeLista(escolha)

    def Menu(self):
        menu = ''' \n\n\nMenu
0 - Finalizar
1 - Criar Lista
2 - Exibir Lista
3 - Check Produto pego
4 - Encerrar Lista
Escolha: '''
        option = ''

        while option != 0:
            option = int(input(menu))
            if option == 1:
                self.criaLista()
            elif option == 2:
                self.listaDao.showLists()
            elif option == 3:
                self.marcaProdutoLIsta()
            elif option == 4:
                self.closeLista()
            elif option == 0:
                print("Fim da execução!!!")

app = App()
app.Menu()             