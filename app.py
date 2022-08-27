import streamlit as st

st.title("Badminton Calculator")
st.write(
    """Badminton Calculator is a webapp that can calculate bill splitting 
from court and shuttlecocks price.
"""
)

st.header("Players Information")
st.subheader("Number of players")
col1, _ = st.columns(2)
with col1:
    n_players = st.number_input("Insert number of players", step=1)

st.subheader("Player Names")
player_names = []
col1, _ = st.columns(2)
with col1:
    for i in range(n_players):
        name = st.text_input("Player", key=f"player_{i+1}")
        player_names.append(name)

st.subheader("List of players")
st.write(player_names)

st.header("Court Price")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        court_payer = st.selectbox("Select court payer", options=player_names)
    with col2:
        court_price = st.number_input("Insert court price", step=1)

st.header("Shuttlecock Information")
col1, _ = st.columns(2)
with col1:
    n_shuttlecock_owner = st.number_input(
        "Insert number of different shuttlecock used", step=1
    )

st.subheader("Shuttlecock prices")
st.write("Remark: price per tube will be divided by 12 to get price per shuttle")
shuttlecock_owners = dict()
for i in range(n_shuttlecock_owner):
    # TODO prompath: add functionalities for players to be able to own multiple
    # types of shuttlecock
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            owner = st.selectbox("Owner", options=player_names, key=f"owner_{i+1}")
        with col2:
            shuttlecock_price = st.number_input(
                "Price per tube", step=1, key=f"price_{i+1}"
            )
    shuttlecock_owners[owner] = shuttlecock_price

st.subheader("List of shuttlecock owners")
st.write(shuttlecock_owners)
