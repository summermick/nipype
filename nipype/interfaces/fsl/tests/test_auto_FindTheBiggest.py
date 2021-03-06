# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.dti import FindTheBiggest
def test_FindTheBiggest_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(hash_files=False,
    genfile=True,
    position=2,
    argstr='%s',
    ),
    args=dict(argstr='%s',
    ),
    in_files=dict(argstr='%s',
    mandatory=True,
    position=0,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    output_type=dict(),
    )
    inputs = FindTheBiggest.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_FindTheBiggest_outputs():
    output_map = dict(out_file=dict(argstr='%s',
    ),
    )
    outputs = FindTheBiggest.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
