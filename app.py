import streamlit as st

import streamlit as st



if "ten_x" not in st.session_state:
    st.session_state.ten_x = False

if "hundred_x" not in st.session_state:
    st.session_state.hundred_x = False

if "count" not in st.session_state:
    st.session_state.count = 0



def get_step():
    if st.session_state.hundred_x:
        return 100
    elif st.session_state.ten_x:
        return 10
    return 1


def increment():
    st.session_state.count += get_step()


def decrement():
    st.session_state.count -= get_step()
    if st.session_state.count < 0:
        st.session_state.count = 0


# -----------------------
# UI
# -----------------------
with st.expander("Options"):
    st.checkbox("10x mode", key="ten_x")
    st.checkbox("100x mode", key="hundred_x")

st.write(f"Total count is {st.session_state.count}")

step = get_step()

st.button(
    f"plus {step}",
    key="increment",
    on_click=increment,
)

st.button(
    f"minus {step}",
    key="decrement",
    on_click=decrement,
)