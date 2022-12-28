import torch

import penn


###############################################################################
# Voiced/unvoiced
###############################################################################


def interpolate(pitch, periodicity, value=penn.DEFAULT_VOICING_THRESHOLD):
    """Fill unvoiced regions via linear interpolation"""
    # Threshold periodicity
    voiced = threshold(periodicity, value)

    # Pitch is linear in base-2 log-space
    pitch = torch.log2(pitch)

    # Interpolate
    pitch[~voiced] = penn.interpolate(
        torch.where(~voiced[0])[0][None],
        torch.where(voiced[0])[0][None],
        pitch[voiced][None])

    return 2 ** pitch


def threshold(periodicity, value):
    """Threshold periodicity to produce voiced/unvoiced classifications"""
    return periodicity > value
