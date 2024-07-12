import streamlit as st
import functions

todos = functions.get_todos('todos.txt')

if 'new_todo' not in st.session_state:
    st.session_state['new_todo'] = ''

def add_todo():
    newtodo = st.session_state["new_todo"] + "\n"
    todos.append(newtodo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title('My to do List Web App')
st.subheader('this is the subheader')
st.write('Testing')
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

st.text_input(label='Enter your new todo', placeholder='Enter your new todo', on_change=add_todo, key='new_todo')