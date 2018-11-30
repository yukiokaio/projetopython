# -*- coding: utf-8 -*-
from data import *
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/avisos/404.html')

@app.errorhandler(405)
def method_not_found(e):
    return render_template('/avisos/405.html')
    
@app.route('/criador')
def criador():
    return render_template('criador.html')

@app.route('/cadastrar', methods = ['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        
        codigo = request.form.get('codigo')
        nome = request.form.get('nome')
        desenvolvedor = request.form.get('desenvolvedor')
        ano = request.form.get('ano')
        nota = request.form.get('nota')
        valor = request.form.get('valor')

        if (codigo and nome and desenvolvedor and ano and nota and valor):
            j = Jogo(codigo,nome,desenvolvedor,ano,nota,valor)
            try:
                db.session.add(j)
                db.session.commit()
                return render_template('/avisos/aviso1.html')
            except exc.IntegrityError:
                return render_template('/avisos/aviso2.html')  

            db.session.commit()
        else:
            return render_template('/avisos/aviso5.html') 

    return render_template('cadastrar.html')


@app.route('/listar')
def listar():
    jogos = Jogo.query.all()
    cont,totalN,totalV = 0,0,0
    for j in jogos:
        totalN += j.nota
        totalV += j.valor
        cont += 1
    totalN /= cont
    return render_template('listar.html',jogos = jogos,totalV=totalV,totalN=totalN,cont=cont)


@app.route('/excluir', methods = ['GET','POST'])
def excluir():
    
    if request.method == 'POST':
        codigo = request.form.get('codigo')

        if codigo:
            jogo = Jogo.query.filter_by(codigo=codigo).first()
            if jogo!= None:
                db.session.delete(jogo)
                db.session.commit()
                return render_template('/avisos/aviso6.html')
            else:
                return render_template('/avisos/aviso4.html') 
        else:
            return render_template('/avisos/aviso5.html') 

    return render_template('excluir.html')


@app.route('/alterar',methods = ['GET','POST'])
def alterar():
    jogo = None
    
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        nome = request.form.get('nome')
        desenvolvedor = request.form.get('desenvolvedor')
        ano = request.form.get('ano')
        nota = request.form.get('nota')
        valor = request.form.get('valor')
        jogo = Jogo.query.filter_by(codigo=codigo).first()

        if jogo != None:
            if (codigo and nome and desenvolvedor and ano and nota and valor):
                jogo.nome = nome
                jogo.desenvolvedor = desenvolvedor
                jogo.ano = ano
                jogo.nota = nota
                jogo.valor = valor
                db.session.commit()
                return render_template('/avisos/aviso3.html')
            else:
                return render_template('/avisos/aviso5.html')
        else:
            return render_template('/avisos/aviso4.html')

    return render_template('alterar.html',jogo=jogo) 


@app.route('/localizar',methods = ['GET','POST'])
def localizar():
    jogo=None
    if request.method == 'POST':
        codigo = request.form.get('codigo')
    
        if codigo:
            jogo = Jogo.query.filter_by(codigo=codigo).first()
            if jogo == None:
                return render_template('/avisos/aviso4.html') 
        else:
            return render_template('/avisos/aviso5.html') 
    
    return render_template('localizar.html',jogo=jogo)

    
if __name__ == '__main__':
    app.run(debug=True) # para funcionar pelo CMD
    #app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080))) # para funcionar no c9