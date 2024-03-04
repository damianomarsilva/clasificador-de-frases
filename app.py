import streamlit as st
import joblib as jb

st.title('Clasificador de sentimientos')

text_input=st.text_input(label="Put your fucking phrase")
button = st.button(label="Predict")

modelo = jb.load('best_model_v1.joblib')

if button:
    y_pred = modelo.predict([text_input])
    if y_pred == 1:
        st.write("Tu comentario es positivo: ", y_pred)
    else:
        st.write("Tu comentario es NEGATIVO: ", y_pred)