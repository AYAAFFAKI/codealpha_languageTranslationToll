# Import necessary modules from PyQt5 and system
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys

# Import Google Translate API and language dictionary
from googletrans import Translator
from googletrans import LANGUAGES as langue

# Initialize the translator
translator = Translator()

# Create the application instance
app = QApplication(sys.argv)

# Load the UI file created with Qt Designer
window = uic.loadUi("E:\\CodeAlpha\\tache1\\translator.ui")

# Set window title and icon
window.setWindowTitle("translator")
window.setWindowIcon(QIcon("E:\\CodeAlpha\\tache1\\translator.jpg"))

# Populate the language selection dropdowns with language names
list_langue = list(langue.values())
window.comboBox_Choose_language1.addItems(list_langue)
window.comboBox_Choose_language2.addItems(list_langue)

# Define the translation function
def translate():
    # Get selected source and destination languages
    src = window.comboBox_Choose_language1.currentText()
    dist = window.comboBox_Choose_language2.currentText()

    # Get the input text from the text box
    input_text = window.text.toPlainText()

    # Default language codes
    src_code = 'auto'  # auto-detect source language
    dist_code = 'en'   # default to English if not found

    # Find the language code for the selected source language
    for code, name in langue.items():
        if name.lower() == src:
            src_code = code
            break

    # Find the language code for the selected destination language
    for code, name in langue.items():
        if name.lower() == dist:
            dist_code = code
            break

    # Translate the text using Google Translate API
    translation = translator.translate(input_text, src=src_code, dest=dist_code)

    # Display the translated text in the label
    window.label.setText(translation.text)

# Connect the translate button to the translation function
window.translate.clicked.connect(translate)

# Run the application
if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())
