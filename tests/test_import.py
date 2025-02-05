#
# SPDX-License-Identifier: Apache-2.0
#

def test_import():
    import spdx_python_model

    p = spdx_python_model.v3_0_1.Person()


def test_import_rename():
    from spdx_python_model import v3_0_1 as spdx_3_0_1

    p = spdx_3_0_1.Person()


def test_version():
    from spdx_python_model import VERSION

    print(VERSION)
