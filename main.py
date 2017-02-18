#!/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

'''Esta aplicacion solamente sirve para obtener ciertos
datos de registro y al hacer clic...muestra los datos enviados'''

class registroApp(App):
	def __init__(self, **kwargs):
		super(registroApp, self).__init__(**kwargs)
		pass 
									
	def build(self):
		
		self.pantalla=GridLayout(orientation='vertical',spacing=10, padding=10, rows=5)
		self.cintillo=BoxLayout(orientation='horizontal')
		label_cintillo=Label(text="Login Screen", font_size=40)
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
		btn_cancelar=Button(text="Cancelar")
		self.cintillo_botones.add_widget(btn_limpiar)
		self.cintillo_botones.add_widget(btn_reg)
		self.cintillo_botones.add_widget(btn_cancelar)
		self.pantalla.add_widget(self.cintillo_botones)
	
		def salida(text):
			a=str(text_cedula.text)
			b=str(text_datos.text)
			print a,b
			text_cedula.text=""
			text_datos.text=""
		btn_reg.bind(on_press=salida)
		
		def limpiar(text):
			text_cedula.text=""
			text_datos.text=""
		btn_limpiar.bind(on_press=limpiar)
		
		def cancel(self):
			registroApp().stop()
		btn_cancelar.bind(on_press=cancel)
		
		
		return self.pantalla
						
if __name__=='__main__':
	registroApp().run()


