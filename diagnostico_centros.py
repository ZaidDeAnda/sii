import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import os
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

#http://registro.sii.nl.gob.mx:8010/


st.write('<style>label.css-qrbaxs.effi0qh0 > label{font-weight: bold}</style>', unsafe_allow_html=True)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#image = Image.open('C:\\NL\\auxiliar\\sii.png')

col1, col2 = st.columns(2)
col1.header("Gobierno del Estado de Nuevo León")
#col2.image(image,width=300)
st.subheader('Valoración de Centros comunitarios 2022')

centros = pd.read_csv(r'centros_comunitarios.csv', encoding="latin-1")

st.write('###### Solicitamos su apoyo para contestar la siguiente encuesta de valoración')
st.write("###### Selección de centro")
col1,col2 = st.columns(2)
cc = col1.selectbox("Selecciona el centro comunitario", centros['centro'].unique())

direccion = centros.query("""centro==@cc""")
gb = GridOptionsBuilder.from_dataframe(direccion)
gb.configure_columns(["municipio", "calle", "entre_calles", "colonia", "CP"], editable=True)
gridOptions = gb.build()

st.write(centros)
with col2:
    st.write("Dirección del centro comunitario")
    AgGrid(direccion, gridOptions=gridOptions, theme="streamlit")


#image upload and save to file
@st.cache
def load_image(imagen):
    img = Image.open(imagen)
    return img

col1.write("Adjunta fotografía del centro comunitario")
imagen = col1.file_uploader('Cargar imagen', type = ['png','jpeg','jpg'])
if imagen is not None:
    details = {"File name": imagen.name, "FileType":imagen.type }
    img = load_image(imagen)
    col1.image(img,width=100)



#Input data

st.markdown("___")
data = {}
data['centro'] = cc

st.write("###### Recursos de computación")
data['equipo de cómputo'] = st.radio('¿Cuenta con equipos de cómputo?', ('Si','No'))
if data['equipo de cómputo'] == 'Si':
     x = st.slider('¿Cuántos equipos de computo tiene?', 0, 80, 0)
     data['cantidad_equipos'] = x
     test_keys = [*range(1, x + 1, 1)]
     test_values = [*range(1, x + 1, 1)]

     n_equipos = {test_keys[i]: test_values[i] for i in range(len(test_keys))}

     for key, value in list(n_equipos.items()):
         data[key] = st.selectbox(f'¿El equipo {value} cuenta con internet de mas de 4 MB?', ('Si', 'No', 'No aplica'),
                                  index=2)
         data[key] = st.selectbox(f'¿El equipo {value}  cuenta con tarjetería?            ', ('Si', 'No', 'No aplica'),
                                  index=2)
         data[key] = st.selectbox(f'¿El equipo {value} cuenta con software de diseño grafico?', ('Si', 'No'))
         data[key] = st.selectbox(f'¿El equipo {value} cuenta con software de microsoft office?', ('Si', 'No'))
         data[key] = st.selectbox(f'¿El equipo {value} cuenta con mantenimietno ?', ('Si', 'No'))

else:
    data['cantidad_equipos'] = 'NA'



st.markdown("___")
st.write("###### Recursos Humanos")

recursos = {'administrador': 'Administradores',
            'instructor_computación': 'Instructores de computo',
            'psicólogo_comunitario': 'Psicólogos comunitarios',
            'promotor_social':'Promotores sociales',
            'promotor_dep':'Promotores deportivos',
            'tutor_aula':'turores de aula',
            'talleristas': 'talleristas',
            'promotores_mic':'Promotores Mic',
            'bibliotecarios':'bibliotecarios',
            'mantenimiento':'personal de mantenimiento',
            'vigilante':'personal de vigilancia',
            'intendentes': 'personal de intendencia'}

col3, col4 = st.columns(2)
for key, value in list(recursos.items())[:6]:
    data[key] = col3.selectbox(f'Cuánto(s) {value} tienen',[*range(1,11)])

for key, value in list(recursos.items())[6:]:
    data[key] = col4.selectbox(f'Cuánto(s) {value} tienen',[*range(1,11)])

st.markdown("___")
st.write("###### Aulas")

aulas = {'aulas_belleza': 'belleza', 'aulas_ludoteca': 'Ludoteca', 'aulas_serigrafia':'Serigrafia','aulas_edu':'Aula Educación'}

for key, value in list(aulas.items()):
    data[key] = st.radio(f'Cuantas aulas especificas para talleres de {value} tienen', [*range(1,11)])


@st.cache
def load_image2(imagen2):
    img2 = Image.open(imagen2)
    return img2


st.write("Adjunta fotografía del aula")
imagen2 = st.file_uploader('Cargar evidencia', type=['png', 'jpeg', 'jpg'])
if imagen2 is not None:
    details = {"File name": imagen.name, "FileType": imagen.type}
    img = load_image(imagen)
    st.image(img, width=100)

st.markdown("___")
st.write("###### Servicios")

servicios = {'Agua': 'agua', 'Luz': 'luz', 'Gas': 'Gas', 'teléfono':'telefonos'}
col5, col6 = st.columns(2)

for key, value in list(servicios.items()):
    data[key] = col5.radio(f'¿Cuenta con servicio de {value}?',('Si', 'No', 'No aplica'), index = 2 )
    if data[key] == 'Si':
        data[key] = col5.selectbox(f'¿Cuántos servicios de {value} tienen?',[*range(1,11)])


data['internet'] = col6.radio(f'¿Cuenta con servicio de internet?',('Si', 'No', 'No aplica'), index = 2)
if data['internet'] == 'Si':
    data[key] = col6.selectbox(f'¿Cuántos GB de internet tiene?',('100', '200','300','400','500','600','700','1000','más de 1000'))

st.markdown("___")
st.write("###### Materiales para talleres")

talleres = {'material_oficios': 'oficios', 'material_culturales': 'culturales', 'material_deportivos': 'deportivos', 'material_formativos': 'formativos'}
col7, col8 = st.columns(2)

for key, value in list(talleres.items())[:2]:
    data[key] = col7.selectbox(f'¿Cuenta con materiales para talleres de {value}?',('Si', 'No', 'No aplica'), index = 2)
    if data[key] == 'Si':
        data[key] = col7.radio(f'¿Cuál es la calidad de los materiales para talleres {value}?',('Buena', 'Regular','Mala'))

for key, value in list(talleres.items())[2:]:
    data[key] = col8.selectbox(f'¿Cuenta con materiales para talleres de {value}?', ('Si', 'No', 'NA'), index=2)
    if data[key] == 'Si':
        data[key] = col8.radio(f'¿Cuál es la calidad de los materiales para talleres {value}?',('Buena', 'Regular', 'Mala'))


st.markdown("___")
st.write("###### Mantenimiento")

mantenimiento = {'plomería': 'Plomería',
            'electricidad': 'Electricidad',
            'climas': 'Climas',
            'albañilería':'Albañilería',
            'mobiliario':'Mobiliario',
            'pintura':'Pintura',
            'ventanas': 'Ventanas',
            'persianas':'Persianas',
            'ventiladores':'Ventiladores',
            'baños':'Baños',
            'mallas':'Mallas',
            'jardineras': 'Jardineras'}

col9, col10 = st.columns(2)
for key, value in list(mantenimiento.items())[:6]:
    data[key] = col9.selectbox(f'Se cuenta con mantenimiento preventivo / correctivo para {value}',('Si', 'No','No aplica'), index = 2)
    if data[key] == 'Si':
        data[key] = col9.radio(f'¿Cuál es la calidad de los mantenimientos {value}?',('Buena', 'Regular','Mala'))

for key, value in list(mantenimiento.items())[6:]:
    data[key] = col10.selectbox(f'Se cuenta con mantenimiento preventivo / correctivo para {value}',('Si', 'No','No aplica'), index = 2)
    if data[key] == 'Si':
        data[key] = col10.radio(f'¿Cuál es la calidad de los mantenimientos de {value}?',('Buena', 'Regular','Mala'))

sub = st.empty()


if sub.button('Enviar'):
    data_diagnostico=pd.DataFrame([data])
    emp = data_diagnostico.empty
    if (emp == True or imagen is None):
        st.warning('**Por favor verifique que se ingresaron todos los campos y se adjunto imagen del centro comunitario**')

    else:
        #data_diagnostico = data_diagnostico.replace('',np.nan)
        #nan = data_diagnostico.isna().values.any()

        with open(os.path.join("C:\\NL\\centros_comunitarios\\diagnostico", imagen.name), "wb") as f:
            f.write((imagen).getbuffer())
            st.success("**imagen adjuntada con exito**")

        #if nan == True:
        #    st.warning('**Por favor ingresa los campos faltantes**')
        #else:
        df = pd.read_csv(r'C:\NL\centros_comunitarios\diagnostico\centros_diagnostico_db.csv', encoding='latin-1')
        df = pd.concat([df,data_diagnostico])
        df.to_csv('C:\\NL\\centros_comunitarios\\diagnostico\\centros_diagnostico_db.csv', index=False)
        sub.info('**Muchas gracias por completar la encuesta.**')


