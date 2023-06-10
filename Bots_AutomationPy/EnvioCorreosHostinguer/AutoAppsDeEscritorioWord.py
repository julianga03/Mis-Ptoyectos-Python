from pywinauto import Desktop, Application

pathAplicacion = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'

# Abre la aplicación de Word
app = Application(backend="uia").start(pathAplicacion)

# Espera a que la aplicación se cargue completamente
window = Desktop(backend="uia").window(title_re=".*Word")

# Encuentra y hace clic en el control 'Documento en blanco' con el identificador especificado
list_item = window.child_window(title="Documento en blanco", control_type="ListItem")
list_item.click_input()

inicio = window.child_window(title="Inicio", auto_id="TabHome", control_type="TabItem")
inicio.click_input()

insetar = window.child_window(title="Insertar", auto_id="TabInsert", control_type="TabItem")
insetar.click_input()

dibujar = window.child_window(title="Dibujar", auto_id="TabDrawInk", control_type="TabItem")
dibujar.click_input()

diseño = window.child_window(title="Diseño", auto_id="TabWordDesign", control_type="TabItem")
diseño.click_input()

disposicion = window.child_window(title="Disposición", auto_id="TabPageLayoutWord", control_type="TabItem")
disposicion.click_input()

referencias = window.child_window(title="Referencias", auto_id="TabReferences", control_type="TabItem")
referencias.click_input()

correspondencia = window.child_window(title="Correspondencia", auto_id="TabMailings", control_type="TabItem")
correspondencia.click_input()

revisar = window.child_window(title="Revisar", auto_id="TabReviewWord", control_type="TabItem")
revisar.click_input()

vista = window.child_window(title="Vista", auto_id="TabView", control_type="TabItem")
vista.click_input()

ayuda = window.child_window(title="Ayuda", auto_id="HelpTab", control_type="TabItem")
ayuda.click_input()

#imprimir los identificadores de la pagina_____________
"""
output_file = 'C:\AutomationPy\identificadores.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    sys.stdout = file
    window.print_control_identifiers()

sys.stdout = sys.__stdout__
"""
#______________________________________________________

# Cierra la aplicación de Word
window.close()

