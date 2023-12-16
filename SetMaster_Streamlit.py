import streamlit as st

def format_list(items, delimiter, separator):
    opening, closing = delimiter[0], delimiter[-1]
    # Asegurarse de que el separador incluya un espacio solo si es necesario
    if separator in [',', ';']:
        separator += ' '
    # Unir los elementos con el separador adecuado, omitiendo elementos vacíos
    formatted_list = f"{opening}{separator.join(item for item in items if item)}{closing}"
    return formatted_list

def extract_elements(set_code):
    # Eliminar delimitadores comunes y usar coma como separador por defecto
    set_code = set_code.strip('[]{}()')
    separator = ','  # Separador por defecto
    if ';' in set_code:
        separator = ';'
    elif '-' in set_code:
        separator = '-'
    elif '_' in set_code:
        separator = '_'

    elements = [element.strip() for element in set_code.split(separator)]
    return '\n'.join(elements)

st.title('Editor de estructuras de datos')

# Opción para elegir entre A>B y B>A
option = st.radio("Elige una opción", ('Generar estructura a partir de una lista', 'Extraer elementos de una estructura'))

if option == 'Generar estructura a partir de una lista':
    # Interfaz para A>B
    items = st.text_area("Ingresa los elementos de la lista:", height=100)
    delimiter = st.selectbox("Elige un delimitador", ["( )", "[ ]", "{ }"])
    separator = st.selectbox("Elige un separador", [",", ";", "-", "_"])
    if st.button('Format List'):
        formatted_list = format_list(items.split('\n'), delimiter, separator)
        st.text_area("Lista Formateada:", formatted_list, height=100)

elif option == 'Extraer elementos de una estructura':
    # Interfaz para B>A
    set_code = st.text_area("Ingresa el código de conjunto:", height=100)
    if st.button('Extraer Elementos'):
        extracted_elements = extract_elements(set_code)
        st.text_area("Elementos Extraídos:", extracted_elements, height=100)