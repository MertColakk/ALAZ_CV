import json
from ..helper import reg_table
import importlib

class Pipeline:
    def __init__(self, data_path):
        """
            MODUL LOADING AREA
        """
        # Load all modules auto
        for module in [
            "core.operations.io",
            "core.operations.color",
            "core.operations.transform",
        ]:
            importlib.import_module(module)
        """
            VARIABLE AREA
        """
        self.config = None
        self.operations = []
        self.paramaters = []
        
        """
            OPERATION AREA
        """
        # Read pipeline
        with open(data_path) as f:
            self.config = json.load(f)
            
        # Process pipeline file
        for step in self.config["pipeline"]:
            self.operations.append(step["operation"].lower())
            self.paramaters.append(step.get("params", {}))
            
        # Execute the pipeline
        self._process()
            
    def _process(self):
        image = None
        for op, param in zip(self.operations, self.paramaters):
            op_class = reg_table[op]()
            image = op_class.apply(image, param)
            
        