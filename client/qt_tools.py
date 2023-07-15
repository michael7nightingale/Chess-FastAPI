from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


def show_exit_dialog(parent, label: str):
    """Shows error exit dialog. After showing closes the window."""
    dialog = QDialog(parent)
    v_layout = QVBoxLayout()
    dialog.setLayout(v_layout)
    text = QLabel(dialog)
    text.setText(label)
    v_layout.addWidget(text)
    accept_button = QPushButton(parent)
    accept_button.setText("OK")
    accept_button.clicked.connect(lambda: parent.close())
    v_layout.addWidget(accept_button)
    dialog.show()


def alert(label: QLabel, text: str):
    """Shows given hidden label."""
    if not label.isVisible():
        label.show()
        label.setText(text)


def show_dialog(parent, label: str):
    """Shows a simple dialog. After showing closes the window."""
    dialog = QDialog(parent)
    v_layout = QVBoxLayout()
    dialog.setLayout(v_layout)
    text = QLabel(dialog)
    text.setText(label)
    v_layout.addWidget(text)
    accept_button = QPushButton(parent)
    accept_button.setText("OK")
    accept_button.clicked.connect(dialog.close)
    v_layout.addWidget(accept_button)
    dialog.show()
