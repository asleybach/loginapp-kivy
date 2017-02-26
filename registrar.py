#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy

from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '500')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import sqlite3

#asi se crea desde el script la bd en sqlite3.. le damos el nombre: registro
sqlite3_file='registro'
cnn_db=sqlite3.connect(sqlite3_file)
cursor=cnn_db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS datos  (cedula integer PRIMARY KEY, nombre_apellido TEXT)''')

class registroApp(App):
	def __init__(self, **kwargs):
		super(registroApp, self).__init__(**kwargs)
		
									
	def build(self):
		
		self.pantalla=GridLayout(orientation='vertical',spacing=10, padding=10, rows=5)
		self.cintillo=BoxLayout(orientation='horizontal')
		label_cintillo=Label(text="Ventana de Registro:", font_size=40)
		self.cintillo.add_widget(label_cintillo)
		self.pantalla.add_widget(self.cintillo)
		
		self.cintillo2=BoxLayout(orientation='horizontal')
		label_cedula=Label(text="Cédula:", font_size=20)
		text_cedula=TextInput(multiline=False,font_size=30)
		self.cintillo2.add_widget(label_cedula)
		self.cintillo2.add_widget(text_cedula)
		self.pantalla.add_widget(self.cintillo2)
		
		self.cintillo3=BoxLayout(orientation='horizontal')
		label_datos=Label(text="Nombre y Apellido:", font_size=20)
		text_datos=TextInput(multiline=False,font_size=30)
		self.cintillo3.add_widget(label_datos)
		self.cintillo3.add_widget(text_datos)
		self.pantalla.add_widget(self.cintillo3)
		
		self.cintillo_botones=BoxLayout(orientation='horizontal')
		btn_limpiar=Button(text="Limpiar")
		btn_reg=Button(text="Enviar")
		btn_cerrar=Button(text="Cerrar")
		self.cintillo_botones.add_widget(btn_limpiar)
		self.cintillo_botones.add_widget(btn_reg)
		self.cintillo_botones.add_widget(btn_cerrar)
		self.pantalla.add_widget(self.cintillo_botones)
	
		def Enviar(text):
			a=str(text_cedula.text)
			b=str(text_datos.text)
			if a=="" or b=="":
				texto_error='''
\nChequee los datos en cada campo\nPosiblemente nos sean correctos
o esten vacios\n\n\n\nclic fuera de este mensaje para volver'''
				popup = Popup(title=' Datos Incompletos...Chequee por favor ', content=Label(text=texto_error),
				size_hint=(None, None), size=(300,300))
				popup.open()
			else:
				cursor.execute("INSERT INTO datos (cedula, nombre_apellido) VALUES ('" + a + "', '" + b + "')")
				cnn_db.commit()
				print a,b
				text_cedula.text=""
				text_datos.text=""
				texto_correcto='''
\nLos datos fueron enviados\n\n\n
clic fuera de este mensaje para continuar''' 
				popup = Popup(title='¡¡Envio Satisfactorio!!', content=Label(text=texto_correcto),
				size_hint=(None, None), size=(400, 200))
				popup.open()
			
		btn_reg.bind(on_press=Enviar)
		
		def limpiar(text):
			text_cedula.text=""
			text_datos.text=""
		btn_limpiar.bind(on_press=limpiar)
		
		def cancel(self):
			print("Close DataBase")
			cnn_db.close()
			registroApp().stop()
		btn_cerrar.bind(on_press=cancel)
		
		
		return self.pantalla
						
if __name__=='__main__':
	registroApp().run()


