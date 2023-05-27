import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue(), "")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            instance_id = f.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(instance_id))
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_do_destroy(self):
        """Tests destroy for all classes."""
        for classname in ["BaseModel"]:
            uid = self.create_class(classname)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('{}.destroy("{}")'.format(classname, uid))
            s = f.getvalue()
            self.assertNotEqual(len(s), 0)
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
            s = f.getvalue()
            self.assertNotEqual(len(s), 0)

    def create_class(self, classname):
        """Creates a class with the given name and returns its id."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create {}'.format(classname))
        s = f.getvalue()
        self.assertNotEqual(len(s), 0)
        return s[:-1]

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_update(self):
        """Tests update 1"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            instance_id = f.getvalue().strip()
            self.console.onecmd("update BaseModel {} name 'Betty'".format(
                instance_id))
            self.console.onecmd("show BaseModel {}".format(instance_id))
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_quit()
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_EOF()
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_create()
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_show()
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_destroy()
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_all()
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_update()
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.help_count()
            output = f.getvalue().strip()
            self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()
