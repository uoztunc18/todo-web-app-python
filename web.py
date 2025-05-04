import streamlit as st
import scripts

todos = scripts.getItems()

def addItem():
    todo = st.session_state["addInputText"]
    todos.append(todo + "\n")
    scripts.writeItems(todos)
    st.session_state["addInputText"] = ""

st.title("To-Do Application")

for index, item in enumerate(todos):
    key = f"{index + 1}.{item}"
    checkbox = st.checkbox(item, key=key)

    if checkbox:
        todos.remove(item)
        scripts.writeItems(todos)
        del st.session_state[key]
        st.rerun()

st.text_input(label=" ",key="addInputText", placeholder="Enter an item to do...", on_change=addItem)