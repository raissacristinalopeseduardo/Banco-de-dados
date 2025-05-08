from flet import*
import pymysql

def main(page:Page):
    page.title = "Exibindo dasdos"
    page.scroll = True


    conexao = pymysql.connect(
        host= "127.0.0.1",
        user= "root",
        #passaword= "",
        database= "raissa"
    )

    cursor = conexao.cursor()


    cursor.execute("SELECT IDCARGO, NOMECARGO FROM cargo")
    resultados = cursor.fetchall()
    page.update()

    def inserir_cargo(nome):
        try:
            conexao = pymysql.connect(
                host= "127.0.0.1",
                user= "root",
            # passaword= "",
                database= "raissa"

            )
            cursor= conexao.cursor()
            sql = "INSERT INTO cargo (nomecargo) VALUES (%s)"
            cursor.execute(sql, (nome,))
            cursor.execute("SELECT IDCARGO, NOMECARGO FROM cargo")
            resultados = cursor.fetchall()
            conexao.commit()
            cursor.close()
            conexao.close()
            return"Usuario inserido com sucesso"
        except Exception as e:
            return f" Erro: {str(e)}"
    
    def iseri(e):
        nome = t.value
        t.value = ""

        resultado = inserir_cargo(nome,)
        txt.value = resultado


        page.update()


    colunas = [
        DataColumn(Text("IDCARGO")),
        DataColumn(Text("NOMECARGO")),

    ]


    linhas = []
    for linha in resultados:
        linhas.append(
            DataRow(
                cells=[DataCell(Text(str(c)))for c in linha]
            )
        )

    t=  TextField(label="Digite seu cargo")
    btniseri = ElevatedButton(text="Inserir", on_click=iseri)
    txt= Text("")
    tabela = DataTable(columns= colunas, rows= linhas)


    page.add(t,btniseri, tabela)

    cursor.close()
    conexao.close()


app(target = main)
