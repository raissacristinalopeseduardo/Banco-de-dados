from flet import*
import pymysql

def main(page:Page):
    page.scroll = True


    conn= pymysql.connect(
        host= "127.0.0.1",
        user= "root",
        password= "",
        database= "raissa"
    )
    cursor =conn.cursor()


    def carregar_nomes():
        cursor.execute("SELECT * FROM cargo")
        return cursor.fetchall()
    
    def inserir_nome(e):
        nome = nome_input.value.strip()
        if  nome: 
            cursor.execute("INSERT INTO cargo (nomecargo) VALUES (%s)", (nome,))
            conn.commit()
            nome.input.value = ""
            atualizar_tabela()


    def atualizar_tabela():
        dados = carregar_nomes()
        data_table.rows.clear()
        for row in dados:
            data_table.rows.append(DataRow(cells=[DataCell(Text(str(row[0]))), DataCell(Text(row[1]))]))
        page.update()


    nome_input = TextField(label= "Digite um Nome")
    botao_inserir = ElevatedButton("Inserir", on_click=inserir_nome)

    data_table = DataTable(
        columns=[
            DataColumn(label = Text("ID Cargo")),
            DataColumn(label = Text("Nome do Cargo"))
        ],
        rows=[]
    )


    page.add(nome_input,botao_inserir, data_table)
    atualizar_tabela()

app(target=main)
