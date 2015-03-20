import gtestgen.core
import unittest

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
    
    def test_constructor(self):
        engine = gtestgen.core.Engine(None, None)

            
if __name__ == '__main__':
    unittest.main()
