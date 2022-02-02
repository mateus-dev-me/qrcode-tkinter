
from tkinter import *
from tkinter import messagebox
import pyqrcode
import os


class App():
	def __init__(self):
		self.window = Tk()
		self.window.title('Creator Qrcode')

		#Dimensões
		width = None
		height = None

		self.label1 = Label(text='Insira a mensagem', padx=10, pady=10, font=('Helvetica', 12))
		self.label1.grid(row=0, column=0, sticky=N + S + E + W)

		self.label2 = Label(text='Titulo do Arquivo', padx=10, pady=10, font=('Helvetica', 12))
		self.label2.grid(row=1, column=0, sticky=N + S + E + W)

		self.msg = StringVar()
		self.msgEntry = Entry(self.window, textvariable=self.msg, width=30, font=('Helvetica', 12))
		self.msgEntry.grid(row=0, column=1, sticky=N + S + E + W)

		self.txt = StringVar()
		self.txtEntry = Entry(self.window, textvariable=self.txt, font=('Helvetica', 12))
		self.txtEntry.grid(row=1, column=1, sticky=N + S + E + W)

		createbutton = Button(self.window, text='Gerar Qrcode', width=15, command=self.create, font=('Helvetica', 12))
		createbutton.grid(row=0, column=2, sticky=N + S + E + W)

		createbutton2 = Button(self.window, text='Salvar o Qrcode', width=15, command=self.save, font=('Helvetica', 12))
		createbutton2.grid(row=1, column=2, sticky=N + S + E + W)

		self.notifiquiteLabel = Label(self.window)
		self.notifiquiteLabel.grid(row=2, column=1, sticky=N + S + E + W)

		self.sublabel = Label(self.window, text="")
		self.sublabel.grid(row=3, column=1, sticky=N + S + E + W)

		totalrows = 3
		totalcolumn = 3
		for row in range(totalrows + 1):
			self.window.grid_rowconfigure(row, weight=1)
		for col in range(totalcolumn + 1):
			self.window.grid_columnconfigure(col, weight=1)

		self.window.mainloop()

	def create(self):
		if len(self.msg.get()) != 0:
			global myQr
			#Cria o Qrcode
			myQr = pyqrcode.create(self.msg.get())
			#Renderiza o código Qrcode gerado com escala igual a 6
			qrImage = myQr.xbm(scale=6)

			global image
			#Cria uma imagem do Qrcode renderizado
			image = BitmapImage(data=qrImage)
		else:
			messagebox.showinfo('Erro', 'Por favor insira o conteúdo da mensagem')
		try:
			self.drawQrcode()
		except:
			messagebox.showinfo('Erro', 'Erro ao desenhar o Qrcode')

	def drawQrcode(self):
		global image
		self.notifiquiteLabel.config(image=image)
		self.sublabel.config(text='Seu Qrcode foi:  ' + self.msg.get())

	def save(self):
		#Armazena o caminho de diretório atual + \\QR Codes
		dir = path1 = os.getcwd() + "/QR Codes"

		if not os.path.exists(dir):
			#Cria um diretório
			os.makedirs(dir)
		try:
			global qrImage, myQr
			if len(self.txt.get()) != 0:
				qrImage = myQr.png(os.path.join(dir, self.txt.get() + ".png"), scale=6)
			else:
				messagebox.showinfo('Erro', 'Insira o titulo da imagem')
		except:
			messagebox.showinfo('Erro', 'Erro ao salvar a imagem')


App()
