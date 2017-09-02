import os
import unittest

if __name__ == '__main__':
    print("Current directory        : {}".format(os.getcwd()))
    print("os.path.dirname(__file__): {}".format(os.path.dirname(__file__)))
    # To run a specific module
    # unittest.main(module='test1')

    # Discover all the tests
    #
    # ATTENTION: A __init__.py is necessary in each directory and sub-directory in the search tree for all
    # test files to be discovered.
    suite = unittest.TestLoader().discover('.', pattern='test*.py')
    unittest.TextTestRunner().run(suite)
