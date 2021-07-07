# importações utilizadas:
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QLineEdit, QPushButton
from PyQt5 import QtGui
import pyperclip
import random


# Classe da janela
class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()

        # Dados da tela:
        self.topo = 250
        self.esquerda = 250
        self.largura = 500
        self.altura = 250
        self.titulo = 'Gerador de Senhas'
        self.setFixedSize(500, 250)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Label Tipo de Caracteres
        label1 = QLabel(self)
        label1.setText('Marque os tipos de caracter da senha:')
        label1.move(20, 10)
        label1.resize(450, 40)
        label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:black}')

        # CheckBox Senha com Letras:
        self.CheckLetras = QCheckBox(self)
        self.CheckLetras.move(30, 40)
        self.CheckLetras.setText('Letras')
        self.CheckLetras.setStyleSheet('QCheckBox {font-size:20px;color:black}')
        self.CheckLetras.clicked.connect(self.VerificaTipo)

        # CheckBox Senha com Numeros:
        self.CheckNumeros = QCheckBox(self)
        self.CheckNumeros.move(150, 40)
        self.CheckNumeros.setText('Numeros')
        self.CheckNumeros.setStyleSheet('QCheckBox {font-size:20px;color:black}')
        self.CheckNumeros.clicked.connect(self.VerificaTipo)

        # CheckBox Senha com Especiais:
        self.CheckEspecial = QCheckBox(self)
        self.CheckEspecial.move(270, 40)
        self.CheckEspecial.setText('Especiais')
        self.CheckEspecial.setStyleSheet('QCheckBox {font-size:20px;color:black}')
        self.CheckEspecial.clicked.connect(self.VerificaTipo)

        # Label Quantidade de caracteres
        label1 = QLabel(self)
        label1.setText('Quantidade de caracteres:')
        label1.move(20, 60)
        label1.resize(450, 40)
        label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:black}')

        # EditText quantidade de caracteres
        self.EditText_Qtde = QLineEdit(self)
        self.EditText_Qtde.move(40, 95)
        self.EditText_Qtde.resize(85, 40)
        self.EditText_Qtde.setStyleSheet('QLineEdit {font-size:24px;color:black}')
        self.EditText_Qtde.setPlaceholderText("Qtde...")
        self.EditText_Qtde.setEnabled(False)
        self.EditText_Qtde.textChanged.connect(self.onChangedQtde)

        # Botão de gerar senha
        self.botao_gerador = QPushButton('Gerar Senha', self)
        self.botao_gerador.move(140, 95)
        self.botao_gerador.resize(125, 40)
        self.botao_gerador.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:16px}')
        self.botao_gerador.setEnabled(False)
        self.botao_gerador.clicked.connect(self.GeraSenha)

        # Label maximo de caracteres recomendado
        self.label3 = QLabel(self)
        self.label3.setText('recomendamos no maximo 27 \ncaracteres, para melhor\nvisualização na tela!')
        self.label3.move(270, 65)
        self.label3.resize(450, 100)
        self.label3.setStyleSheet('QLabel {font:bold;font-size:12px;color:#BDBCBC}')
        self.label3.setVisible(False)

        # Label Senha
        label2 = QLabel(self)
        label2.setText('Senha:')
        label2.move(20, 150)
        label2.resize(450, 40)
        label2.setStyleSheet('QLabel {font:bold;font-size:20px;color:black}')

        # EditText senha gerada
        # Max 27 caracteres
        self.EditText_Senha = QLineEdit(self)
        self.EditText_Senha.move(100, 150)
        self.EditText_Senha.resize(360, 40)
        self.EditText_Senha.setStyleSheet('QLineEdit {font-size:24px;color:black}')
        self.EditText_Senha.setPlaceholderText("Senha gerada...")
        self.EditText_Senha.setEnabled(False)
        self.EditText_Senha.textChanged.connect(self.SenhaGerada)

        # Botão Limpar tudo
        self.botao_limpar = QPushButton('Limpar tudo', self)
        self.botao_limpar.move(120, 200)
        self.botao_limpar.resize(125, 40)
        self.botao_limpar.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:16px}')
        self.botao_limpar.setEnabled(False)
        self.botao_limpar.clicked.connect(self.LimparTudo)

        # Botão Copiar senha
        self.botao_copiar = QPushButton('Copiar Senha', self)
        self.botao_copiar.move(300, 200)
        self.botao_copiar.resize(125, 40)
        self.botao_copiar.setStyleSheet('QPushButton {background-color:#B0C4DE;font:bold;font-size:16px}')
        self.botao_copiar.setEnabled(False)
        self.botao_copiar.clicked.connect(self.CopiarSenha)

        # Label Confirma Copia
        self.label4 = QLabel(self)
        self.label4.setText('Copiado com Sucesso!')
        self.label4.move(270, 65)
        self.label4.resize(450, 100)
        self.label4.setStyleSheet('QLabel {font:bold;font-size:16px;color:#2FFF2E}')
        self.label4.setVisible(False)

        # Abre a janela
        self.LoadJanela()

    # Função que Carrega a Janela:
    def LoadJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    # Verifica se há pelo menos um tipo de caracter selecionado
    def VerificaTipo(self):
        if self.CheckLetras.isChecked() or self.CheckNumeros.isChecked() or self.CheckEspecial.isChecked():
            # print('checado pelo menos 1')
            self.EditText_Qtde.setEnabled(True)
            self.EditText_Qtde.setText('')
            self.EditText_Qtde.setFocus()
        else:
            # print('nao há nd checado')
            self.EditText_Qtde.setEnabled(False)
            self.EditText_Qtde.setText('')
        self.EditText_Senha.setText('')
        self.botao_limpar.setEnabled(False)
        self.botao_copiar.setEnabled(False)
        self.label4.setVisible(False)

    # verifica mudanca de caracter na quantidade
    def onChangedQtde(self):
        QuantidadeString = str(self.EditText_Qtde.text())
        # print(QuantidadeString)
        if QuantidadeString != '' and not QuantidadeString.isnumeric():
            QuantidadeString = QuantidadeString[:-1]
        self.EditText_Qtde.setText(QuantidadeString)
        if QuantidadeString == '':
            self.botao_gerador.setEnabled(False)
        else:
            self.botao_gerador.setEnabled(True)
        if QuantidadeString.isnumeric():
            if int(QuantidadeString) > 27:
                self.label3.setVisible(True)
            else:
                self.label3.setVisible(False)
            if int(QuantidadeString) == 0:
                QuantidadeString = QuantidadeString[:-1]
                self.EditText_Qtde.setText(QuantidadeString)
        self.EditText_Senha.setText('')
        self.botao_limpar.setEnabled(False)
        self.botao_copiar.setEnabled(False)
        self.label4.setVisible(False)

    # Verifica se pd gerar senha e chama a funcao que gera
    def GeraSenha(self):
        QuantidadeString = str(self.EditText_Qtde.text())
        if QuantidadeString != '':
            self.EditText_Senha.setText(self.AlgoritimoGeraSenha(QuantidadeString))
            # print('safe')
        else:
            self.EditText_Qtde.setFocus()
            # print('not safe')

    # senha foi gerada
    def SenhaGerada(self):
        self.botao_limpar.setEnabled(True)
        self.botao_copiar.setEnabled(True)

    # manda a senha criada para a area de transferencia
    def CopiarSenha(self):
        SenhaGerada = self.EditText_Senha.text()
        pyperclip.copy(SenhaGerada)
        self.label3.setVisible(False)
        self.label4.setVisible(True)

    # limpa todos os campos
    def LimparTudo(self):
        self.EditText_Qtde.setEnabled(False)
        self.EditText_Qtde.setText('')
        self.EditText_Senha.setText('')
        self.botao_gerador.setEnabled(False)
        self.botao_limpar.setEnabled(False)
        self.botao_copiar.setEnabled(False)
        self.CheckLetras.setChecked(False)
        self.CheckNumeros.setChecked(False)
        self.CheckEspecial.setChecked(False)
        self.label3.setVisible(False)
        self.label4.setVisible(False)

    # Algoritimo que gera a senha
    def AlgoritimoGeraSenha(self, Qtde):
        Qtde = int(Qtde)
        Letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        Numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        Especiais = ['!', '@', '#', '$', '%', '*', '(', ')', '{', '}', '^', '&', '?', '_', '-', '+', '/', '=']
        Lista1 = []
        Lista2 = []
        Lista3 = []
        QtOpCaracteres = 0
        if self.CheckLetras.isChecked():
            # print("Há letras!")
            QtOpCaracteres += 1
            Lista1 = Letras
        if self.CheckNumeros.isChecked():
            # print("Há numeros!")
            QtOpCaracteres += 1
            if QtOpCaracteres == 1:
                Lista1 = Numeros
            else:
                Lista2 = Numeros
        if self.CheckEspecial.isChecked():
            # print("Há especiais!")
            QtOpCaracteres += 1
            if QtOpCaracteres == 1:
                Lista1 = Especiais
            elif QtOpCaracteres == 2:
                Lista2 = Especiais
            else:
                Lista3 = Especiais
        Senha = ""
        while len(Senha) < int(Qtde):
            if QtOpCaracteres == 1:
                QualListaIndice = 1
            elif QtOpCaracteres == 2:
                QualListaIndice = random.randint(1, 2)
            else:
                QualListaIndice = random.randint(1, 3)
            if QualListaIndice == 1:
                Senha += random.choice(Lista1)
            elif QualListaIndice == 2:
                Senha += random.choice(Lista2)
            else:
                Senha += random.choice(Lista3)
        # Retorna a senha gerada
        return Senha


# Inicialização da Tela
application = QApplication(sys.argv)
Window = Janela()
sys.exit(application.exec_())
