import os.path
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import *
from PyQt5 import QtPrintSupport
from PyQt5 import QtGui, QtCore
import sys

class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("NotePad")
        self.setWindowIcon(QIcon('note.png'))
        self.resize(400, 200)
        self.Text = QTextEdit()
        self.Text.setAlignment(Qt.AlignVCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.Text)
        self._createActions()
        self._createMenuBar()
        self._createContextMenu()

        self.saveAction.triggered.connect(self.FileSave)
        self.helpAction.triggered.connect(self.Help)
        self.printAction.triggered.connect(self.print_file)
        self.openAction.triggered.connect(self.file_open)
        self.saveToPDFAction.triggered.connect(self.SavetoPDF)
        self.previewAction.triggered.connect(self.preview)
        self.aboutAction.triggered.connect(self.About)
        self.fontAction.triggered.connect(self.Font)
        self.colorAction.triggered.connect(self.Color)
        self.themeDarkAction.triggered.connect(self.Dark)
        self.themeLightAction.triggered.connect(self.Light)
        self.copyAction.triggered.connect(self.copy)
        self.pasteAction.triggered.connect(self.paste)
        self.cutAction.triggered.connect(self.cut)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        fileMenu.setIcon(QIcon('file.png'))
        menuBar.addMenu(fileMenu)

        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.printAction)
        fileMenu.addAction(self.saveToPDFAction)


        helpMenu = menuBar.addMenu("&Help")
        helpMenu.setIcon(QIcon('help.png'))
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)

        viewMenu = menuBar.addMenu("View")
        viewMenu.setIcon(QIcon('preview.png'))
        viewMenu.addAction(self.previewAction)

        themeMenu = viewMenu.addMenu('Theme')
        themeMenu.setIcon(QIcon('mode.png'))
        themeMenu.addAction(self.themeLightAction)
        themeMenu.addAction(self.themeDarkAction)

        editMenu = menuBar.addMenu("Edit")
        editMenu.setIcon(QIcon('edit.png'))
        editMenu.addAction(self.fontAction)
        editMenu.addAction(self.colorAction)
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)


    def _createActions(self):
        self.newAction = QAction(self)
        self.saveAction = QAction('Save', self)
        self.printAction = QAction('Print', self)
        self.helpAction = QAction('Help', self)
        self.openAction = QAction('Open File', self)
        self.saveToPDFAction = QAction('SaveToPDF', self)
        self.previewAction = QAction('Preview', self)
        self.aboutAction = QAction('About', self)
        self.fontAction = QAction('Font', self)
        self.colorAction = QAction('Color', self)
        self.themeLightAction = QAction('Light', self)
        self.themeDarkAction = QAction('Dark', self)
        self.copyAction = QAction('Copy', self)
        self.pasteAction = QAction('Paste', self)
        self.cutAction = QAction('Cut', self)

        self.openAction.setIcon(QIcon('openfile.png'))
        self.saveAction.setIcon(QIcon('save.png'))
        self.printAction.setIcon(QIcon('print.png'))
        self.helpAction.setIcon(QIcon('help1.png'))
        self.saveToPDFAction.setIcon(QIcon('savePDF.png'))
        self.previewAction.setIcon(QIcon('preview1.png'))
        self.aboutAction.setIcon(QIcon('about.png'))
        self.fontAction.setIcon(QIcon('font.png'))
        self.colorAction.setIcon(QIcon('palette.png'))
        self.themeLightAction.setIcon(QIcon('sun.png'))
        self.themeDarkAction.setIcon(QIcon('moon.png'))
        self.copyAction.setIcon(QIcon('copy.png'))
        self.pasteAction.setIcon(QIcon('paste.png'))
        self.cutAction.setIcon(QIcon('cut.png'))


    def _createContextMenu(self):
        self.Text.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.Text.addAction(self.saveAction)
        self.Text.addAction(self.saveToPDFAction)
        self.Text.addAction(self.openAction)
        self.Text.addAction(self.printAction)
        self.Text.addAction(self.previewAction)
        self.Text.addAction(self.copyAction)
        self.Text.addAction(self.pasteAction)
        self.Text.addAction(self.cutAction)

    def About(self):
        msg = QMessageBox(self)
        msg.setWindowIcon(QIcon("about.png"))
        msg.setWindowTitle("About")
        msg.setIcon(QMessageBox.Information)
        msg.setText("App Version-1.3.1 \n"
                    "Creator: Vildanov Almas")
        msg.exec_()

    def Help(self):
        msg = QMessageBox(self)
        msg.setWindowIcon(QIcon("help.png"))
        msg.setWindowTitle("Help")
        msg.setText("When you click on 'Save', the text is saved to a TXT file \n"
                    "When you click on 'SaveToPDF', the text is saved in PDF format\n"
                    "When you click on 'Print', the contents of the text field are printed\n"
                    "When you click on 'Open File', a file explorer opens with which you can open a file (format-TXT)\n"
                    "Clicking on 'Preview' opens a window for previewing the text\n"
                    "Clicking on 'Copy' copies the selected text\n"
                    "When you click on 'Paste', the copied text is inserted \n"
                    "When you click on 'Cut', the selected text is cut \n"
                    "When you hover over 'Theme', two more actions appear: 'Light' and 'Dark' \n"
                    "When you click on 'Light', the transition to light mode\n"
                    "Clicking on 'Dark' switches to dark mode\n"
                    "'Font' is responsible for selecting the font and text size\n"
                    "'Color' is responsible for selecting the text color")
        msg.exec_()

    def FileSave(self):
        text = self.Text.toPlainText()
        filename, _ = QFileDialog.getSaveFileName(None, "Save File (TXT)", ".", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'w') as file:
                file.write(text)
                file.write('\n')

    def file_open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "",
                                            "TXT File (*.txt)")[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.Text.setText(data)

    def print_file(self):
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.Text.print_(printer)

    def preview(self):
        pp = QtPrintSupport.QPrintPreviewDialog()
        pp.paintRequested.connect(self.Text.print_)
        pp.exec_()

    def SavetoPDF(self):
        printer = QPrinter()
        filename, ok= QFileDialog.getSaveFileName(None, "Save File (PDF)", ".", "Text Files (*.pdf);;All Files (*)")
        if ok:
            printer.setOutputFileName(filename)
            self.Text.document().print_(printer)

    def Font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.Text.setFont(font)

    def Color(self):
        color = QColorDialog.getColor()
        self.Text.setTextColor(color)

    def Dark(self):
        self.Text.setStyleSheet('background-color: rgb(60, 60, 60); color: rgb(255, 255, 255);')
        self.setStyleSheet('background-color: rgb(175, 175, 175);')

    def Light(self):
        self.Text.setStyleSheet('')
        self.setStyleSheet('')

    def copy(self):
        self.Text.copy()

    def paste(self):
        self.Text.paste()

    def cut(self):
        self.Text.cut()

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())