# Login Form

from PyQt6.QtWidgets import (QLineEdit, QRadioButton, QLabel, QFormLayout)

def LoginForm(UN, PW):
    login_layout = QFormLayout()

    Jama_label = QLabel("Jama Connect API Login Information")
    login_layout.addRow(Jama_label)

    URL_label = QLabel("Jama Connect URL: ")
    URL_input = QLineEdit()
    URL_input.setPlaceholderText("Enter your Jama Connect instance's URL")
    login_layout.addRow(URL_label,URL_input)

    username_label = QLabel(UN + ": ")
    username_input = QLineEdit()
    username_input.setPlaceholderText("Enter your " + UN)
    login_layout.addRow(username_label, username_input)

    password_label = QLabel(PW + ": ")
    password_input = QLineEdit()
    password_input.setPlaceholderText("Enter your " + PW)
    password_input.setEchoMode(QLineEdit.EchoMode.Password)
    login_layout.addRow(password_label, password_input)

    project_api_id_label = QLabel("Project API ID: ")
    project_api_id_input = QLineEdit()
    project_api_id_input.setPlaceholderText("Enter the API ID of the specific project for updates")
    login_layout.addRow(project_api_id_label,project_api_id_input)

    return login_layout