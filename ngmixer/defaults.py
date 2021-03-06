# flagging
################################
# bits for the 'flags' column
# this is here for testing, it will be removed one day
USE_OLD_FLAGS = False

if USE_OLD_FLAGS:
    IMAGE_FLAGS=2**8
    NO_CUTOUTS=2**0
    BOX_SIZE_TOO_BIG=2**4
    UTTER_FAILURE=2**7
    NO_ATTEMPT=2**30

    PSF_FIT_FAILURE=2**1
    GAL_FIT_FAILURE=2**3
    PSF_FLUX_FIT_FAILURE=2**9
    LOW_PSF_FLUX=2**6
else:
    # flags used by NGMixer
    BAD_OBJ              = 2**25
    IMAGE_FLAGS          = 2**26
    NO_CUTOUTS           = 2**27
    BOX_SIZE_TOO_BIG     = 2**28
    UTTER_FAILURE        = 2**29
    NO_ATTEMPT           = 2**30

    # flags for fitting codes
    PSF_FIT_FAILURE      = 2**0
    GAL_FIT_FAILURE      = 2**1
    PSF_FLUX_FIT_FAILURE = 2**2
    LOW_PSF_FLUX         = 2**3

################################
# flags used by MOF 
MOF_NBR_NOT_CONVERGED            = 2**0
MOF_NBR_BAD_FIT                  = 2**1
MOF_NBR_NOT_FIT                  = 2**2
MOF_NBR_SKIPPED_IN_CONV_CHECK    = 2**3
MOF_FOFMEM_NOT_CONVERGED         = 2**4
MOF_FOFMEM_BAD_FIT               = 2**5
MOF_FOFMEM_NOT_FIT               = 2**6
MOF_FOFMEM_SKIPPED_IN_CONV_CHECK = 2**7
MOF_NOT_CONVERGED                = 2**8
MOF_SKIPPED_IN_CONV_CHECK        = 2**9

################################
# defaults
DEFVAL = -9999
PDEFVAL = 9999
BIG_DEFVAL = -9.999e9
BIG_PDEFVAL = 9.999e9

################################
# running code
_CHECKPOINTS_DEFAULT_MINUTES = [0,30,60,110]

################################
# setup logging/verbosity
class _VERBOSITY(object):
    def __init__(self,level=0):
        self.level = level

    def __call__(self):
        return self.level

VERBOSITY = _VERBOSITY(0)
