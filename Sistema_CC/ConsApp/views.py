from ConsApp import app
from flask import render_template, redirect, url_for, request, session, flash
from management import *

#INSERINDO O ADMIN
user1 = inserir_usuario('Patricia', '88 9 1234 5678', 'admin', 'admin', 'A')
endereco1 = inserir_endereco('62800-000', 'Aracati', 'José de Alencar 123')
vincular_user_adress(user1.id, endereco1.id)

# 

@app.route('/') 
@app.route('/home')
def homepage():
	if 'usuario' in session:
		return render_template('index.html', usuario = session['usuario'])
	return render_template('index.html', usuario = None)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if 'usuario' in session:
		return redirect(url_for('homepage'))
	if request.method == 'POST':
		email = request.form['email']
		senha = request.form['senha']
		if validar_login(email, senha):
			session['usuario'] = validar_login(email, senha)
			return redirect(url_for('homepage'))
		else:
			print('não deu certo')

	return render_template('login.html')


@app.route('/logout')
def logout():
	session.pop('usuario', None)
	return redirect(url_for('homepage'))

def isAdmin():
	return 'usuario' in session and session['usuario']['Tipo'] == 'A'

#CADASTRO DE USUÁRIO
@app.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrarusuario():
	if not isAdmin():
		return redirect(url_for('homepage'))
	
	user = Usuario('','','','','')
	address = Endereco('', '', '')
	
	if request.method == 'POST':
		nome = request.form['nome']
		telefone = request.form['telefone']
		email = request.form['email']
		senha = request.form['senha']

		rua = request.form['rua']
		cep = request.form['cep']
		cidade = request.form['cidade']
		
		tipo = request.form['tipo']
		
		user = inserir_usuario(nome, telefone, email, senha, tipo)
		endereco = inserir_endereco(cep, cidade, rua)
		vincular_user_adress(user.id, endereco.id)
		
		flash('Usuário cadastrado com sucesso!')
		user = models.Usuario.query.get(user.id)
	
	return render_template('cadastrarusuario.html', u=user, a=address, lista_usuarios = obter_usuarios(), Alterar = 'alterarUsuario', Excluir = 'excluirUsuario')
	

#EXCLUIR USUÁRIO
@app.route('/cadastrarusuario/excluir/<int:index>')
def excluirUsuario(index):
	if not isAdmin():
		return redirect(url_for('homepage'))
	
	if deletar_usuario(index) is not None:
		flash('Usuário removido com sucesso!')
	else:
		flash('Erro!')
	return redirect(url_for('cadastrarusuario'))
	
#ALTERAR USUÁRIO
@app.route('/cadastrarusuario/alterar/<int:index>', methods=['GET', 'POST'])
def alterarUsuario(index):
	if not isAdmin():
		return redirect(url_for('homepage'))

	user = obter_usuario(index)
	address = obter_endereco(user.id_endereco)
	
	if request.method == 'POST':
		nome = request.form['nome']
		telefone = request.form['telefone']
		email = request.form['email']
		senha = request.form['senha']
		
		rua = request.form['rua']
		cep = request.form['cep']
		cidade = request.form['cidade']
		
		tipo = request.form['tipo']		
		
		user = atualizar_usuario(index, nome, telefone, email, senha, tipo)

		endereco = atualizar_endereco(user.id_endereco, cep, cidade, rua)
		vincular_user_adress(user.id, endereco.id)

		flash('Registro alterado com sucesso!')		
		user = models.Usuario.query.get(index)	

	return render_template('cadastrarusuario.html', u=user, a=address, lista_usuarios = obter_usuarios(), Alterar = 'alterarUsuario', Excluir = 'excluirUsuario')
	
#CADASTRAR PRODUTO (NÃO ESTÁ FUNCIONANDO)
@app.route('/cadastrarproduto', methods=['GET', 'POST'])
def cadastrarproduto():
	if not isAdmin():
		return redirect(url_for('homepage'))
	
	if request.method == 'POST':
		nomep = request.form['nomep']
		tipop = request.form['tipop']
		descricaop = request.form['descricaop']
		produto = inserir_produto(nomep, tipop, descricaop)				
		flash('Produto cadastrado com sucesso!')
	return render_template('cadastrarproduto.html', usuario = session['usuario'], lista_produtos = obter_produtos(), Alterar = 'alterarProduto', Excluir = 'excluirProduto')
	
#EXCLUIR PRODUTO
@app.route('/cadastrarproduto/excluir/<int:index>')
def excluirProduto(index):
	if not isAdmin():
		return redirect(url_for('homepage'))
	
	produto = deletar_produto(index)
	flash('Produto removido com sucesso!')
	return redirect(url_for('cadastrarproduto'))
	
#CADASTRAR RESERVA
@app.route('/cadastrarreserva', methods=['GET', 'POST'])
def cadastrarreserva():
	if 'usuario' in session and (session['usuario']['Tipo'] == 'A' or session['usuario']['Tipo'] == 'U'):
		if request.method == 'POST':
			usuario = request.form['usuario']
			descricaopro = request.form['descricaopro']	
			reserva = inserir_reserva(descricaopro)		
			flash('Reserva cadastrada com sucesso!')
		return render_template('cadastrarreserva.html', usuario = session['usuario'], lista_reservas = obter_reservas(), Alterar = 'alterarReserva', Excluir = 'excluirReserva')
	return redirect(url_for('homepage'))

#EXCLUIR RESERVA
@app.route('/cadastrarreserva/excluir/<int:index>')
def excluirReserva(index):
	if 'usuario' in session and (session['usuario']['Tipo'] == 'A' or session['usuario']['Tipo'] == 'U'):
		reserva = deletar_reserva(index)
		flash('Reserva removida com sucesso!')
		return redirect(url_for('cadastrarreserva'))
	return redirect(url_for('homepage'))

#ESTOQUE
@app.route('/estoque')
def estoque():
	if 'usuario' in session:
		return render_template('estoque.html', usuario = session['usuario'])
	return render_template('estoque.html', usuario = None)

#TIJOLO
@app.route('/tijolo')
def tijolo():
	if 'usuario' in session:
		return render_template('tijolo.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

#TELHA
@app.route('/telha')
def telha():
	if 'usuario' in session:
		return render_template('telha.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

#CIMENTO
@app.route('/cimento')
def cimento():
	if 'usuario' in session:
		return render_template('cimento.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

#PISO
@app.route('/piso')
def piso():
	if 'usuario' in session:
		return render_template('piso.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

#ARGAMASSA
@app.route('/argamassa')
def argamassa():
	if 'usuario' in session:
		return render_template('argamassa.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

#REJUNTE
@app.route('/rejunte')
def rejunte():
	if 'usuario' in session:
		return render_template('rejunte.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))


@app.route('/about')
def sobre():
	if 'usuario' in session:
		return render_template('sobre.html', usuario = session['usuario'])
	return render_template('sobre.html', usuario = None)