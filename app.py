import streamlit as st
from earthquakes import Earthquakes

st.set_page_config(page_title="Earthquake Streaming", layout="wide", page_icon=":tada:")
st.title("Earthquake Streaming")
st.write("This dashboard visualizes global earthquakes in near-real time. To get the new earthquakes, please refresh the page.")

def generate_map():
    eq = Earthquakes()

    ######## TO BE ALTERED FOR PRODUCTION
    eq.pulled_data = [{'id': 'e73979a9-f7aa-4b90-9a68-493146537687', 
                       'data': {'date': '2023-07-22', 'depth': 69, 'latitude': -29.61, 'magnitude': 2.9, 
                                'time': '08:21:00', 'uuid': 'e73979a9-f7aa-4b90-9a68-493146537687', 'longitude': -71.29}}]
    ######## END - TO BE ALTERED FOR PRODUCTION

    return eq.generate_map()

st.plotly_chart(generate_map())

    