# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import SkullStrip
def test_SkullStrip_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(name_source='in_file',
    name_template='%s_skullstrip',
    argstr='-prefix %s',
    ),
    args=dict(argstr='%s',
    ),
    outputtype=dict(),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(position=1,
    mandatory=True,
    argstr='-input %s',
    ),
    )
    inputs = SkullStrip.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_SkullStrip_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = SkullStrip.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
