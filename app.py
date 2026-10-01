from flask import Flask, render_template, url_for, request

app = Flask(__name__)

  
    nome = input(nome)
    peso = float(peso)
    altura = float(altura)
    imc = peso / altura ^ 2

@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
  if 
  dados_usuario ={       
    'nome' = request.form(nome)
    'peso' = request.form(peso)
    'altura' = request.form(altura)  
  }

    return render_template ('index.html',
                            **dados_usuario)





if __name__ == '__main__':
    app.run(debug=True)