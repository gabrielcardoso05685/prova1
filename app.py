from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
   if request.method == 'POST':
         
        nome == request.form(nome),
        peso == request.form(peso),
        altura  == request.form(altura) 
  

return render_template ('index.html',
                            nome=nome,
                            peso=peso,
                            altura=altura)

@app.route('/equipe')
def foto_equipe():
return render_template ('equipe.html')





if __name__ == '__main__':
    app.run(debug=True)