PACKAGE_URL = 'PACKAGE_URL = 'git+https://www.github.com/Luaithrenn/asdemo.git@''

import numpy as np
import pandas as pd
from iotfunctions.preprocessor import BaseTransformer

class MyCustomFunction(BaseTransformer):
  '''
  Multiple input item by 3.41
  '''
  url = PACKAGE_URL

  def _init(self,
    input_item,
    output_item - 'output_item'
    ):
    self.input_item = input_item
    self.output_item = output_item
    super()._init_()

  def execute(self, df):
    df = df.copy()
    df[self.output_item] = df[self.input_item]*3.41

    return df
