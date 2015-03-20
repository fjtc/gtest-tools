from string import Template
import re

class TemplateFile:
    
    def __init__(self, file_name):
        self._file_name = file_name
        self._load_file(file_name)
        
    def _load_file(self, file_name):
        with open(file_name, 'r') as inp:
            self._template = Template(inp.read())

    @property
    def template(self):
        return self._template.template
        
    @property
    def file_name(self):
        return self._file_name
    
    def process(self, params):
        return self._template.safe_substitute(params)

class TestTitle:
    
    IDENTIFIER_PATTERN = re.compile('^[_a-zA-Z][_a-zA-Z0-9]*$')
    
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @property
    def is_valid_identifier(self):
        return TestTitle.IDENTIFIER_PATTERN.match(self.name) != None
    
    @property
    def header_name(self):
        return self.name + '.h' 

    @property
    def source_name(self):
        return self.name + '.cpp' 
    
    @property
    def macro_name(self):
        return '__' + self.header_name.upper().replace('.', '_') + '__' 
    