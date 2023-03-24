from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("msg encriptada", 0) == "adatpircne gsm"
    assert encrypt_message("hello msg", 3) == "leh_gsm ol"
    assert encrypt_message("hello msg", 4) == "gsm o_lleh"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("hello msg", "text")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(6486, 1)
