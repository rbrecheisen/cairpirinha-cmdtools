import os
import pydicom


class Dcm2Numpy(object):

    def __init__(self):
        self._input_dicom_file_path = None
        self._output_numpy_array = None
        self._shape = None

    def set_input_dicom_file_path(self, input_dicom_file_path):
        self._input_dicom_file_path = input_dicom_file_path

    def get_output_numpy_array(self):
        return self._output_numpy_array

    def get_shape(self):
        return self._shape

    def execute(self):
        if self._input_dicom_file_path is None:
            raise RuntimeError('Input DICOM file path not set')
        p = pydicom.read_file(self._input_dicom_file_path)
        self._shape = (p.Rows, p.Columns)
        self._output_numpy_array = p.pixel_array.reshape(self._shape)


if __name__ == '__main__':
    component = Dcm2Numpy()
    component.set_input_dicom_file_path('/Users/Ralph/data/Jorne/P0001.dcm')
    component.execute()
    print(component.get_output_numpy_array().shape)