from test import create, view

def test_create():
    assert create() == "ajouté"
    assert len(view()) == 1

def test_view():
    todos = view()
    assert len(todos) == 1
    assert todos[0] == "text"
