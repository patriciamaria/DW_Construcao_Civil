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

#CADASTRAR USUARIO
@app.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrarusuario():
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
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
		return render_template('cadastrarusuario.html', usuario = session['usuario'], lista_usuarios = obter_usuarios(), Alterar = 'alterarUsuario', Excluir = 'excluirUsuario')
	return redirect(url_for('homepage'))


@app.route('/cadastrarusuario/excluir/<int:index>')
def excluirUsuario(index):
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		user = deletar_usuario(index)
		flash('Usuário removido com sucesso!')
		return redirect(url_for('cadastrarusuario'))
	return redirect(url_for('homepage'))

@app.route('/cadastrarproduto')
def cadastrarproduto():
	if 'usuario' in session:
		return render_template('cadastrarproduto.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

@app.route('/cadastrarreserva')
def cadastrarreserva():
	if 'usuario' in session:
		return render_template('cadastrarreserva.html', usuario = session['usuario'])
	return redirect(url_for('homepage'))

#FALTA CORREÇÃO
'''@app.route('/cadastrarproduto', methods=['GET', 'POST'])
def cadastrarproduto():
	if 'usuario' in session and session['usuario']['Tipo'] == 'A':
		if request.method == 'POST':
			nome = request.form['nome']
			tipo = request.form['tipo']
			descricao = request.form['descricao']				
			flash('Produto cadastrado com sucesso!')
		return render_template('cadastrarproduto.html', usuario = session['usuario'], lista_produtos = obter_produtos(), Alterar = 'alterarProduto', Excluir = 'excluirProduto')
	return redirect(url_for('homepage'))


@app.route('/cadastrarreserva', methods=['GET', 'POST'])
def cadastrarreserva():
	if 'usuario' in session and session['usuario']['Tipo'] == 'A' and session['usuario']['Tipo'] == 'U':
		if request.method == 'POST':
			usuario = request.form['usuario']
			descricaopro = request.form['descricaopro']			
			flash('Reserva cadastrada com sucesso!')
		return render_template('cadastrarproduto.html', usuario = session['usuario'], lista_reservas = reservas(), Alterar = 'alterarReserva', Excluir = 'excluirReserva')
	return redirect(url_for('homepage'))'''

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