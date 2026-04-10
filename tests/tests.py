"""
Tests for ../app.py

Run from the project directory (not the tests directory) with the invocation `pytest tests/tests.py`
"""
import streamlit as st
from streamlit.testing.v1 import AppTest


def test_button_increments_counter():
    """Test that the counter increments when the button is clicked."""
    at = AppTest.from_file("app.py").run()

    at.session_state.count = 1

    at.button(key="increment").click().run()

    assert at.session_state.count == 2


def test_button_decrements_counter():
    """Test that the decrement button works."""
    at = AppTest.from_file("app.py").run()

    at.session_state.count = 5

    at.button(key="decrement").click().run()

    assert at.session_state.count == 4


def test_button_increments_counter_ten_x():
    """Test that the increment button works in ten_x mode."""
    at = AppTest.from_file("app.py").run()

    at.session_state.count = 0
    at.session_state.ten_x = True

    at.button(key="increment").click().run()

    assert at.session_state.count == 10


def test_button_decrements_counter_ten_x():
    """Test that the decrement button works in ten_x mode."""
    at = AppTest.from_file("app.py").run()

    at.session_state.count = 20
    at.session_state.ten_x = True

    at.button(key="decrement").click().run()

    assert at.session_state.count == 10


def test_output_text_correct():
    """Test that the text shows the correct value."""
    at = AppTest.from_file("app.py").run()

    at.session_state.count = 0
    at.session_state.ten_x = False

    at.button(key="increment").click().run()
    at.checkbox(key="ten_x").check().run()
    at.button(key="increment").click().run()

    assert at.markdown[0].value == "Total count is 11"