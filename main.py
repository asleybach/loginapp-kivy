#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import kivy

from kivy.config import Config
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '500')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class maingridapp(GridLayout):
	def __init__(self, **kwargs):
		super(maingridapp, self).__init__(**kwargs)
		pass
		
class mainappmuestra(App):
	def build(self):
		pantalla=GridLayout(orientation='horizontal',rows=4,spacing=10, padding=10, cols=1)
		label1=Label(text='Sistema en App...',font_size=40,)
		label2=Label(text='Una app para registrar y consultar',font_size=20)
		pantalla.add_widget(label1)
		pantalla.add_widget(label2)
		
		imagen=Image(source= '/data/pythontux.png', norm_image_size=True)
		pantalla.add_widget(imagen)
		
		marco1=BoxLayout(orientation='horizontal', spacing=10, padding=10, cols=2)
		boton=Button(text='Registrar')
		boton_cerrar=Button(text='Cerrar')
		boton2=Button(text='Buscar')
		def registrar(Button):
			os.system("/usr/bin/python registrar.py")
		boton.bind(on_release=registrar)
		def buscar(Button):
			os.system("/usr/bin/python buscar.py")
		boton2.bind(on_release=buscar)
		def cerrar(Button):
			mainappmuestra().stop()
		boton_cerrar.bind(on_press=cerrar)
		
		marco1.add_widget(boton)
		marco1.add_widget(boton_cerrar)
		marco1.add_widget(boton2)
				
		pantalla.add_widget(marco1)		
		return pantalla
		
mainappmuestra().run()
