import pytest
import graphics.lightprobe_tetra_leak as mod

CASES = [
    ("tetra_weights", (1,)),
    ("versioned_readback", (1,)),
    ("clamp_outside", (1,)),
    ("rebuild_tetra", (1,)),
    ("thread_local_buffer", (1,)),
    ("ordered_accum", (1,)),
    ("bake", (1,)),
    ("sample", (1,)),
    ("update_probe", (1,)),
    ("remove_probe", (1,)),
    ("validate_leak", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
