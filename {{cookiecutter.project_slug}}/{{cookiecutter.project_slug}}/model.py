from pathlib import Path
from {{cookiecutter.project_slug}}.general_utils import check_suffix, ROOT


class Model:
    """docstring for Model."""

    def __init__(self, model_path:str=None, device:str='cpu', **kwargs):
        """Init Model.
        Inputs:
            model_path (str) - path to model weights
            device (str) - name of the device: cpu|cuda:IDX
            **kwargs (map) - map with aditional arguments, specific for the models
        """
        super(Model, self).__init__()
        self.model_path = model_path
        # TODO: model_path handler
        if self.model_path is None:
            self.model_path = ROOT / '{{cookiecutter.project_slug}}/assets/model.onnx'

        self.device = device
        # TODO: check requirements
        # check_requirements(('numpy', 'onnx', 'onnxruntime'))

    def _preprocess(self, sample, **kwargs):
        """Model depended prepare batch for inferencing."""
        # TODO: sample preprocessing, i.e. image resizing, normalizing
        raise NotImplemented
        # return sample

    def _postprocess(self, result, **kwargs):
        """Model depended process results for batch."""
        # Result postprocessing, i.e. data interpreting: NMS,...
        raise NotImplemented
        # return result

    def to(self, device='cpu'):
        """Move model to device: cpu|cuda:IDX"""
        raise NotImplemented

    def process_sample(self, sample, **kwargs):
        """Process signle sample."""
        # TODO: implement process single sample method
        batch = [sample]
        return self.process_batch(batch, **kwargs)[0]

    def process_batch(self, batch, **kwargs):
        # TODO: implement process batch method
        raise NotImplemented
