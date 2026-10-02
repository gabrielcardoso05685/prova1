from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculo_imc():
    nome = request.form(nome),
    peso = request.form(peso),
    altura  = request.form(altura),
    indice_imc = peso / altura ^ 2
    indice_imc = float(indice_imc)

   return (indice)

@app.route('/', methods=['GET', 'POST'])


@app.route('/', methods=['POST'])
def pagina_inicial():
   if request.method == 'POST':
        
        return render_template ('index.html',
                                nome=nome,
                                peso=peso,
                                altura=altura)
   


@app.route('/equipe')
def foto_equipe():
 return render_template ('equipe.html')





if __name__ == '__main__':
    app.run(debug=True)