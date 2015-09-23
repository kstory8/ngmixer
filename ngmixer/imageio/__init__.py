import imageio
import medsio
import simpsimmedsio
import desmedsio

from .imageio import ImageIO
from .medsio import MEDSImageIO
from .desmedsio import SVMEDSImageIO, SVMOFMEDSImageIO, Y1MEDSImageIO
from .simpsimmedsio import SimpSimMEDSImageIO

#######################################################
# setup image i/o dict
# each time you create a new image i/o class, add it to this dict
IMAGEIO = {}

# MEDS formats
IMAGEIO['meds'] = MEDSImageIO
IMAGEIO['meds-sv'] = SVMEDSImageIO
IMAGEIO['meds-sv-mof'] = SVMOFMEDSImageIO
IMAGEIO['meds-y1'] = Y1MEDSImageIO

# MEDS sim formats
IMAGEIO['meds-simp-sim'] = SimpSimMEDSImageIO

def get_imageio_class(imageio_name):
    """
    returns the imageio class for a given imageio_name
    """
    cftype = imageio_name.lower()
    assert cftype in IMAGEIO,'could not find image i/o class %s' % cftype    
    return IMAGEIO[cftype]