from flet import*
import pymysql


def inserir_cargo(nomecargo):
    try:
        conexao = pymysql.connect(
            host= "127.0.0.1",
            user= "root",
           # passaword= "",
            database= "raissa"

        )
        cursor= conexao.cursor()
        sql = "INSERT INTO cargo (nomecargo) VALUES (%s)"
        cursor.execute(sql, (nomecargo,))
        cursor.execute("SELECT IDCARGO, NOMECARGO FROM cargo")
        resultados = cursor.fetchall()
        conexao.commit()
        cursor.close()
        conexao.close()
        return"Usuario inserido com sucesso"
    except Exception as e:
        return f" Erro: {str(e)}"
    


def main (page:Page):
    page.window.center()
    page.window_width  = 768
    page.window.height = 500
    page.bgcolor = "white"
    page.padding = 0


    def salvarcargo(e):
        nome = nomecar.value
        nomecar.value = ""

        resultado = inserir_cargo(nome,)
        t.value = resultado


        page.update()

    nomecar= TextField(label="Digite seu cargo", )
    btnsalvar = ElevatedButton(text="Salvar", on_click= salvarcargo)
    t = Text("", size=30)
    lista = []

    
    
    Tabela= DataTable(
            columns=[
                DataColumn(Text("ID CARGO")),
                DataColumn(Text("NOME CARGO")),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(Text("fualno")),
                        DataCell(Text("siclano")),
                    ],
                ),
            ],
        )
    


    page.add(nomecar,btnsalvar, t, Tabela)
app(target = main)
