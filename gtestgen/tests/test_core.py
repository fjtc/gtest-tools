import gtestgen.core
import unittest
import os.path
from gtestgen.core import FileExistsException

class TemplateFileTest(unittest.TestCase):

    def test_constructor(self):
        t = gtestgen.core.TemplateFile('TemplateFileTest.tpl')
        self.assertIsNotNone(t.template)
        self.assertIsNotNone(t.file_name)
        
    def test_constructor_failed(self):
        try:
            t = gtestgen.core.TemplateFile('this_file_does_not_exist')
            self.fail()
        except gtestgen.core.TemplateNotFoundException:
            pass
        
    def test_template(self):
        t = gtestgen.core.TemplateFile('TemplateFileTest.tpl')
        self.assertEquals('This is a simple ${VALUE} test.\n', t.template)
        
    def test_file_name(self):
        t = gtestgen.core.TemplateFile('TemplateFileTest.tpl')
        self.assertEquals('TemplateFileTest.tpl', t.file_name)

    def test_process(self):
        t = gtestgen.core.TemplateFile('TemplateFileTest.tpl')
        v = t.process({'VALUE': 'TemplateFileTest'})
        self.assertEquals('This is a simple TemplateFileTest test.\n', v)
        
    def test_processMissingParameter(self):
        t = gtestgen.core.TemplateFile('TemplateFileTest.tpl')
        v = t.process({'VALUES': 'TemplateFileTest'})
        self.assertEquals('This is a simple ${VALUE} test.\n', v)

class TestTitleTest(unittest.TestCase):
    
    def test_constructor(self):
        t = gtestgen.core.TestTitle('title')
        self.assertIsNotNone(t)
        
    def test_name(self):
        t = gtestgen.core.TestTitle('title')
        self.assertEqual('title', t.name)
        
    def test_is_valid_identifier(self):
        t = gtestgen.core.TestTitle('title')
        self.assertTrue(t.is_valid_identifier)
        
        t = gtestgen.core.TestTitle('tItle')
        self.assertTrue(t.is_valid_identifier)
        
        t = gtestgen.core.TestTitle('t0tle')
        self.assertTrue(t.is_valid_identifier)

        t = gtestgen.core.TestTitle('Title')
        self.assertTrue(t.is_valid_identifier)
        
        t = gtestgen.core.TestTitle('_title')
        self.assertTrue(t.is_valid_identifier)
        
        t = gtestgen.core.TestTitle('t_itle')
        self.assertTrue(t.is_valid_identifier)
        
        t = gtestgen.core.TestTitle('9title')
        self.assertFalse(t.is_valid_identifier)
                 
        t = gtestgen.core.TestTitle(' title')
        self.assertFalse(t.is_valid_identifier)

        t = gtestgen.core.TestTitle('t.itle')
        self.assertFalse(t.is_valid_identifier)
        
    def test_header_name(self):
        t = gtestgen.core.TestTitle('title')
        self.assertEqual('title.h', t.header_name)
        
    def test_source_name(self):
        t = gtestgen.core.TestTitle('title')
        self.assertEqual('title.cpp', t.source_name)

    def test_macro_name(self):
        t = gtestgen.core.TestTitle('title')
        self.assertEqual('__TITLE_H__', t.macro_name)
        
      
class EngineTest(unittest.TestCase):
        
    def get_output_dir(self):     
        outdir = os.path.join('.', 'tmp')
        if not os.path.isdir(outdir):
            os.mkdir(outdir)
        return outdir
    
    def clear_output_dir(self):
        outdir = self.get_output_dir()
        
        for f in os.listdir(outdir):
            path = os.path.join(outdir, f)
            os.remove(path)
    
    def test_constructor(self):
        engine = gtestgen.core.Engine(None, None)
        self.assertIsNotNone(engine.output_dir)
        self.assertIsNotNone(engine.template_dir)
        
    def test_output_dir(self):
        engine = gtestgen.core.Engine(None, None)
        self.assertEqual(os.path.abspath('.'), engine.output_dir)
        
        engine.output_dir = '.'
        self.assertEqual(os.path.abspath('.'), engine.output_dir)
                
        engine.output_dir = '/opt'
        self.assertEqual('/opt', engine.output_dir)

        engine.output_dir = __file__
        self.assertEqual(os.path.dirname(os.path.abspath(__file__)), engine.output_dir)
        
    def test_template_dir(self):
        engine = gtestgen.core.Engine(None, None)
        
        self.assertEqual(os.path.dirname(gtestgen.core.__file__), engine.template_dir)
        
        engine.template_dir = None
        self.assertEqual(os.path.dirname(gtestgen.core.__file__), engine.template_dir)
        
        engine.template_dir = '.'
        self.assertEqual(os.path.abspath('.'), engine.template_dir)
        
        try:
            engine.template_dir = __file__
            self.fail()
        except gtestgen.core.TemplateNotFoundException:
            pass
        
    def test_generate_main(self):
        
        outdir = self.get_output_dir()
        self.clear_output_dir()
        
        engine = gtestgen.core.Engine(outdir, os.path.dirname(__file__))        
        engine.generate_main()

        # Test duplicated file        
        try:
            engine.generate_main()
            self.fail()
        except gtestgen.core.FileExistsException:
            pass
        
    def test_generate_test(self):
        
        outdir = self.get_output_dir()
        self.clear_output_dir()
        
        engine = gtestgen.core.Engine(outdir, os.path.dirname(__file__))
        engine.generate_test('test_name')

        # Test duplicated file        
        try:
            engine.generate_test('test_name')
            self.fail()
        except gtestgen.core.FileExistsException:
            pass
        
    def test_generate_test_invalid_name(self):
        
        outdir = self.get_output_dir()
        self.clear_output_dir()
        
        engine = gtestgen.core.Engine(outdir, os.path.dirname(__file__))
        try:
            engine.generate_test('00000')
            self.fail()
        except ValueError:
            pass
            
if __name__ == '__main__':
    unittest.main()
