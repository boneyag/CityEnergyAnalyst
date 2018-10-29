from __future__ import division
from __future__ import print_function

import functools
import cea.plots
import pandas as pd
import os

"""
Implements py:class:`cea.plots.SupplySystemPlotBase` as a base class for all plots in the category "supply-system" and also
set's the label for that category.
"""

__author__ = "Daren Thomas"
__copyright__ = "Copyright 2018, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Daren Thomas"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daren Thomas"
__email__ = "cea@arch.ethz.ch"
__status__ = "Production"

# identifies this package as a plots category and sets the label name for the category
label = 'Supply System'


class SupplySystemPlotBase(cea.plots.PlotBase):
    """Implements properties / methods used by all plots in this category"""
    category_name = "supply-system"
    category_path = os.path.join('new_basic', category_name)

    # cache hourly_loads results to avoid recalculating it every time
    _cache = {}

    def __init__(self, config, locator, **parameters):
        super(SupplySystemPlotBase, self).__init__(config, locator, **parameters)
        self.category_path = os.path.join('new_basic', 'supply-system')

    @property
    def output_path(self):
        """Overriding output_path to include the individual and generation parameters"""
        return self.locator.get_timeseries_plots_file('gen' + str(self.generation) + '_' + self.individual + '_energy_system_map', category)