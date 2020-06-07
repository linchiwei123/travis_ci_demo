from hypothesis import given, example
from hypothesis.strategies import text

from .run_length_encoding import encode, decode


@given(text())
@example("")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
