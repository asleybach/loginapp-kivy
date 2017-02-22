#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import kivy
import sqlite3
import reportlab
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from reportlab.pdfgen import canvas

sqlite3_file='registro'
cnn_db=sqlite3.connect(sqlite3_file)
cursor=cnn_db.cursor()

class registroApp(App):
	def __init__(self, **kwargs):
		super(registroApp, self).__init__(**kwargs)
											
	def build(self):
		
		self.pantalla=GridLayout(orientation='vertical',spacing=10, padding=10, rows=5)
		self.cintillo=BoxLayout(orientation='horizontal')
		label_cintillo=Label(text="Serching...", font_size=40)
		self.cintillo.add_widget(label_cintillo)
		self.pantalla.add_widget(self.cintillo)
		
		self.cintillo2=BoxLayout(orientation='horizontal')
		label_cedula=Label(text="Cédula:", font_size=20)
		text_cedula=TextInput(multiline=False,font_size=30)
		self.cintillo2.add_widget(label_cedula)
		self.cintillo2.add_widget(text_cedula)
		self.pantalla.add_widget(self.cintillo2)
		
		self.cintillo3=BoxLayout(orientation='vertical')
		label_salida1=Label(text="", font_size=20)
		self.cintillo3.add_widget(label_salida1)
		label_salida2=Label(text="", font_size=20)
		self.cintillo3.add_widget(label_salida2)
		self.pantalla.add_widget(self.cintillo3)
		
		self.cintillo_botones=BoxLayout(orientation='horizontal')
		btn_imprimir=Button(text="Imprimir")
		btn_buscar=Button(text="Buscar")
		btn_cerrar=Button(text="Cerrar")
		btn_limpiar=Button(text="Limpiar")
		self.cintillo_botones.add_widget(btn_limpiar)
		self.cintillo_botones.add_widget(btn_imprimir)
		self.cintillo_botones.add_widget(btn_buscar)
		self.cintillo_botones.add_widget(btn_cerrar)
		self.pantalla.add_widget(self.cintillo_botones)
	
		def buscar(text):
			a=str(text_cedula.text)
			if a=="":
				texto_error='''
\nChequee el dato cédula en campo correspondiente\nPosiblemente nos sea correcto
o este vacio\n\n\n\nclic fuera de este mensaje para volver'''
				popup = Popup(title=' Datos Incompletos...Chequee por favor ', content=Label(text=texto_error),
				size_hint=(None, None), size=(400,350))
				popup.open()
			else:
				cursor.execute("SELECT cedula, nombre_apellido from datos WHERE cedula ='" + a + "'")
				text_cedula.text=""
				cnn_db.commit()
				for raw in cursor:
						label_salida1.text = ("Cédula: " + str(raw[0]))
						label_salida2.text = ("Nombre y Apellido: " + raw[1])				
		btn_buscar.bind(on_press=buscar)
		
		def Imprimir(Button):
			ver=str(label_salida1.text)
			if ver == "":
				texto_error='''
\nChequee la busqueda correspondiente\nno hay datos que imprimir\n\n\n\nclic fuera de este mensaje para volver'''
				popup = Popup(title=' Error ', content=Label(text=texto_error),
				size_hint=(None, None), size=(400,350))
				popup.open()
			else:
				text_cedula.text=""
				label_salida1.text=""
				label_salida2.text=""
				c = canvas.Canvas("factura.pdf")
				c.drawString(50,700,"Bienvenidos al servicio de facturación con ReportLab")
				c.drawString(100,600,"En esta sección se espera la factura impresa")
				c.showPage()
				c.save()
				os.popen("/usr/bin/evince-previewer hello.pdf")
				
#falta colocar datos aqui del pdf creado e imprimir
		
		def limpiar(self):
			text_cedula.text=""
			label_salida1.text=""
			label_salida2.text=""
		btn_limpiar.bind(on_release=limpiar)
		
		def cancel(self):
			cnn_db.close()
			print("Close DataBase")
			registroApp().stop()
		btn_cerrar.bind(on_press=cancel)
				
		return self.pantalla
						
if __name__=='__main__':
	registroApp().run()
