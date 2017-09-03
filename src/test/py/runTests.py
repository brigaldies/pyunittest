import os
import unittest

import xmlrunner

if __name__ == '__main__':
    print("Current directory        : {}".format(os.getcwd()))
    print("os.path.dirname(__file__): {}".format(os.path.dirname(__file__)))

    # To run a specific module
    # unittest.main(module='test1')

    # Discover all the tests
    #
    # ATTENTION: A __init__.py is necessary in each directory and sub-directory in the search tree for all
    # test files to be discovered.
    suite = unittest.TestLoader().discover(start_dir=os.getcwd(), pattern='test*.py')
    # unittest.TextTestRunner(verbosity=2).run(suite)

    # Run the tests, and generate the JUnit-compatible XML tests report that Jenkins can consume.
    with open('unittest-results.xml', 'wb') as output:
        # unittest.main(
        #     testRunner=xmlrunner.XMLTestRunner(output=output),
        #     failfast=False, buffer=False, catchbreak=False)

        xmlrunner.XMLTestRunner(output=output, verbosity=2, failfast=False, buffer=False).run(suite)
