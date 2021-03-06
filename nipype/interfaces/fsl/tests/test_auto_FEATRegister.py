# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.model import FEATRegister
def test_FEATRegister_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    reg_dof=dict(usedefault=True,
    ),
    reg_image=dict(mandatory=True,
    ),
    feat_dirs=dict(mandatory=True,
    ),
    )
    inputs = FEATRegister.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_FEATRegister_outputs():
    output_map = dict(fsf_file=dict(),
    )
    outputs = FEATRegister.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
