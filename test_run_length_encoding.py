from hypothesis import example, given
from hypothesis.strategies import text

from .run_length_encoding import decode, encode


@given(text())
@example("")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
