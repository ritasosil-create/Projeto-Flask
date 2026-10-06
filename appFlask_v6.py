from flask import Flask, render_template, request

app_cassia = Flask(__name__,template_folder='t_templates')  #cria o objeto Flask, que é a aplicação web, e define a pasta templates como pasta de templates


@app_cassia.route('/ola')
def raiz():   #esta função está vinculada a rota  /ola
    return render_template('homepage.html')  #retorna o arquivo index.html que está na pasta templates

#veja que o id é um parâmetro da rota e faz parte da URL, e não vai confundir com a rota /ola
@app_cassia.route('/ola/<id>') 
def saudacao(id):
   return render_template('homepage_nome.html', campoNome= id) 
   #retorna o arquivo homepage.html que está na pasta templates. No .html tem o campo {{campoNome}} que vai receber o valor do parâmetro id da rota


#@app_cassia.route('/ola/<id>')
#def saudacao():
#    nome = request.args.get("id")
#    return render_template('homepage_nome.html', campoNome= nome) #retorna o arquivo homepage.html que está na pasta templates

@app_cassia.route('/')
@app_cassia.route('/index')
def index():   #esta função está vinculada a rota raíz / e rota /index
    return render_template('t_index.html', nome ="Turma 2025") 

@app_cassia.route('/contato')
def contato():
    return render_template('t_contato.html')  

@app_cassia.route('/usuario')
def dados_usuario():
    #nome_usuario="Mariela"
    dados_usu = {"nome": "Mariela", "profissao": "Professora EBTT", "disciplina":"Desenvolvimento Web III"}
    return render_template("t_usuario.html", dados = dados_usu)
                                           #parâmetro recebe argumento
                                           #colocar o site no ar

@app_cassia.route('/usuario/<p_nome>/<p_profissao>/<p_disciplina>')
def dados_usuario2(p_nome, p_profissao, p_disciplina):
    dados_usu = {"nome": p_nome, "profissao": p_profissao, "disciplina": p_disciplina}
    return render_template("usuario.html", dados = dados_usu)

@app_cassia.route('/login')
def login():
    return render_template("t_login.html")

@app_cassia.route('/autenticar', methods=['GET','POST'])
def autenticarUsuario():
    if request.method == 'POST':
       usuario = request.form.get("nome_usuario")
       senha = request.form.get("senha")
    else:   
       usuario = request.args.get("nome_usuario")
       senha = request.args.get("senha")

    return f"usuario: {usuario} e senha: {senha} recebidos com sucesso!"


#esta função não está vinculado a rota, mas pode ser usada dentro de uma rota ou outra função ou invocada de fora
def saudacaoes(nome): 
    return f"Boa noite, {nome}!. Tudo bem?"

#maiores detalhes nos slides que estão no AVA.
if __name__ == '__main__':  #verifica se o arquivo está sendo executado diretamente, e não importado
    meu_site.run(port=7000)

meu_site.run( port=6000)    #executa caso o o arquivo seja importado, mas não é uma boa prática, pois pode gerar conflito de portas