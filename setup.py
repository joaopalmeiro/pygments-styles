from setuptools import setup, find_packages

setup( 
    name = 'pygments-styles', 
    version = '1.0', 
    description = "A set of custom Pygments styles", 
    author = "João Palmeiro",
    author_email='jm.palmeiro@campus.fct.unl.pt',
    license = 'MIT',
    install_requires = ['pygments'],
    packages = find_packages(), 
    entry_points = '''
    [pygments.styles]
    cv = styles.cv:CVStyle
    '''
) 
