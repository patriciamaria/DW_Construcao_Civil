from ConsApp import db, models
from ConsApp.models import *

def vincular_user_adress(user_id, adress_id):
	user = Usuario.query.get(user_id)
	adress = Endereco.query.get(adress_id)
	if user and adress is not None:
		user.endereco = adress
		db.session.commit()	
		return user
	else:
		return None

def vincular_user_reserva(user_id, reserva_id):
	user = Usuario.query.get(user_id)
	reserva = Reserva.query.get(reserva_id)
	if user and Reserva is not None:
		user.reserva = reserva
		reserva.id_usuario = user_id
		db.session.commit()	
		return user
	else:
		return None
	
def vincular_reserva_produto(reserva_id, produto_id):
	reserva = Produto.query.get(reserva_id)
	produto = Produto.query.get(produto_id)
	if reserva and produto is not None:
		reserva.produtos.append(produto) 
		livro.reservas.append(reserva)
		db.session.commit()
		return reserva
	else:
		return None

def vincular_produto_categoria(produto_id, categoria_id):
	produto = Produto.query.get(produto_id)
	categoria = Categoria.query.get(categoria_id)
	if produto and categoria is not None:
		produto.categoria_id = categoria.id
		categoria.produtos.append(produto)
		db.session.commit()
		return produto
	else:
		return None

#CRUD ENTIDADE USUÁRIO
def obter_usuarios():
	users = Usuario.query.all()
	
	lista_usuarios = list()

	if users is not None:
		for item in users:
			if item.endereco is not None:
				lista_usuarios.append({'Id':item.id, 'Nome':item.nome, 'Telefone':item.telefone, 'Email':item.email, 'Senha':item.senha, 'Id_Endereço':item.endereco.id, 'Rua':item.endereco.rua, 'Cep':item.endereco.cep, 'Cidade':item.endereco.cidade, 'Tipo':item.tipo,})
			else:
				lista_usuarios.append({'Id':item.id, 'Nome':item.nome, 'Telefone':item.telefone, 'Email':item.email, 'Senha':item.senha, 'Tipo':item.tipo,})	

		return lista_usuarios
	else:
		return None

def obter_usuario(usuario_id):
	user = Usuario.query.get(usuario_id)
	if user is not None:
		return user
	else:
		return None

def validar_login(usuario_email, usuario_senha):
	user = Usuario.query.filter(Usuario.email==usuario_email, Usuario.senha==usuario_senha).first()
	print(user)
	if user is not None:
		return ({'id':user.id, 'Email':user.email, 'Senha':user.senha, 'Nome':user.nome, 'Telefone':user.telefone, 'Tipo':user.tipo})
	else:
		return None


def inserir_usuario(nome, telefone, email, senha, tipo):
	user = Usuario(nome, telefone, email, senha, tipo)
	db.session.add(user)
	db.session.commit()
	return user

def atualizar_usuario(id, nome, telefone, email, senha, tipo):
	user = Usuario.query.get(id)
	if user is not None:
		user.nome = nome
		user.telefone = telefone
		user.email = email
		user.senha = senha
		user.tipo = tipo
		db.session.commit()
		return user
	else:
		return None

def deletar_usuario(id):
	user = Usuario.query.get(id)

	if user is not None:
		db.session.delete(user)
		db.session.commit()
		return user
	else:
		return None

#CRUD ENTIDADE ENDEREÇO
def inserir_endereco(cep, cidade, rua):
	adress = Endereco(cep, cidade, rua)
	db.session.add(adress)
	db.session.commit()
	return adress

def atualizar_endereco(id, cep, cidade, rua):
	adress = Endereco.query.get(id)
	
	if adress is not None:
		adress.cep = cep
		adress.cidade = cidade
		adress.rua = rua
		db.session.commit()
		return adress
	else:
		return None

def deletar_endereco(id):
	adress = Endereco.query.get(id)

	if adress is not None:
		db.session.delete(adress)
		db.session.commit()
		return True
	else:
		return None

def obter_endereco(id):
	adress = Endereco.query.get(id)

	if adress is not None:
		return adress
	else:
		return None

#CRUD ENTIDADE CATEGORIA
def inserir_categoria(tipo, descricao):
	categoria = Categoria(tipo, descricao)
	db.session.add(categoria)
	db.session.commit()
	return categoria

def atualizar_categoria(id, tipo, descricao):
	categoria = Categoria.query.get(id)
	if categoria is not None:
		categoria.tipo = tipo
		categoria.descricao = descricao
		db.session.commit()
		return categoria
	else:
		return None

def deletar_categoria(id):
	categoria = Categoria.query.get(id)
	if categoria is not None:
		db.session.delete(categoria)
		db.session.commit()
		return categoria
	else:
		return None

def obter_categoria(id):
	categoria = Categoria.query.get(id)
	if categoria is not None:
		return categoria
	else:
		return None


#CRUD ENTIDADE PRODUTO
def obter_produtos():
	prods = Produto.query.all()
	
	lista_produtos = list()

	if prods is not None:
		for item in prods:
			if item.endereco is not None:
				lista_produtos.append({'Id':item.id, 'Nome':item.nomep, 'Tipo':item.tipop, 'Descrição':item.descricaop,})
			else:
				lista_produtos.append({'Id':item.id, 'Nome':item.nomep, 'Tipo':item.tipop, 'Descrição':item.descricaop,})	

		return lista_produtos
	else:
		return None

def inserir_produto(nomep, tipop, descricaop):
	produto = Produto(nomep, tipop, descricaop)
	db.session.add(produto)
	db.session.commit()
	return produto

def atualizar_produto(id, nomep):
	produto = Produto.query.get(id)
	if livro is not None:
		produto.nomep = nomep	
		db.session.commit()
		return produto
	else:
		return None

def deletar_produto(id):
	produto = Produto.query.get(id)
	if produto is not None:
		db.session.delete(produto)
		db.session.commit()
		return produto
	else:
		return None

def obter_produto(id):
	produto = Produto.query.get(id)
	if produto is not None:
		return produto
	else:
		return None

#CRUD ENTIDADE RESERVA
def obter_reservas():
	users = Reserva.query.all()
	
	lista_reservas = list()

	if users is not None:
		for item in users:
			if item.endereco is not None:
				lista_reservas.append({'Id':item.id, 'Usuário':item.usuario, 'Descrição do Produto':item.descricaopro,})
			else:
				lista_reservas.append({'Id':item.id, 'Usuário':item.usuario, 'Descrição do Produto':item.descricaopro,})	

		return lista_reservas
	else:
		return None

def inserir_reserva(descricaopro):
	reserva = reserva(descricaopro)
	db.session.add(reserva)
	db.session.commit()
	return reserva

def atualizar_reserva(id, descricaopro):
	reserva = Reserva.query.get(id)
	if reserva is not None:
		reserva.descricaopro = descricaopro
		db.session.commit()
		return reserva
	else:
		return None

def deletar_reserva(id):
	reserva = Reserva.query.get(id)
	if reserva is not None:
		db.session.delete(reserva)
		db.session.commit()
		return reserva
	else:
		return None

def obter_reserva(id):
	reserva = Reserva.query.get(id)
	if reserva is not None:
		return reserva
	else:
		return None