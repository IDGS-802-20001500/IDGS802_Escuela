from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
from db import get_connection
import forms

maestros=Blueprint("maestros",__name__)

@maestros.route("/getMaestros",methods=["GET","POST"])
def getMaestros():
    creat_form=forms.UserForm(request.form)
    maestro = ""
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consultar_maestro()')
            resulset=cursor.fetchall()
            maestro = resulset
    except Exception as ex:
        print(ex)

    return render_template("ABCompletoM.html",form=creat_form,maestro=maestro)

@maestros.route("/insertMaestro", methods=["GET","POST"])
def index():
    create_form=forms.UserForm(request.form)
    if request.method=="POST":
        nombre=create_form.nombre.data
        apellidos=create_form.apellidos.data
        email=create_form.email.data

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call agregar_maestro(%s, %s, %s)',(nombre,apellidos, email))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
            
        return redirect(url_for("maestros.getMaestros"))
    return render_template("agregarMaestro.html",form=create_form)

@maestros.route("/modificarMaestro",methods=["GET","POST"])
def modificar():
    create_form=forms.UserForm(request.form)
    idM = 0
    nombre = ""
    apellidos = ""
    email = ""
    fecha = "";
    
    if request.method=="GET":
        id=request.args.get("id")
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro2(%s)',(id))
                resulset=cursor.fetchall()
                for row in resulset:
                    print(row)
        except Exception as ex:
            print(ex)

        idM, nombre, apellidos, email, fecha = row
        

        create_form.id.data=idM
        create_form.nombre.data=nombre
        create_form.apellidos.data=apellidos
        create_form.email.data=email

    if request.method=="POST":
        id=create_form.id.data
        nombre=create_form.nombre.data
        apellidos=create_form.apellidos.data
        email=create_form.email.data

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call actualizar_maestro(%s, %s, %s, %s)',(nombre,apellidos, email, id))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        
        return redirect(url_for("maestros.getMaestros"))
    return render_template("modificarM.html",form=create_form)

@maestros.route("/eliminarMaestro",methods=["GET","POST"])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=="GET":
        id=request.args.get("id")
        
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro2(%s)',(id))
                resulset=cursor.fetchall()
                for row in resulset:
                    print(row)
        except Exception as ex:
            print(ex)

        idM, nombre, apellidos, email, fecha = row
        

        create_form.id.data=idM
        create_form.nombre.data=nombre
        create_form.apellidos.data=apellidos
        create_form.email.data=email
    if request.method=="POST":
        id=create_form.id.data
        

        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call eliminar_maestro(%s)',(id))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)
        
        return redirect(url_for("maestros.getMaestros"))
    return render_template("eliminarM.html",form=create_form)