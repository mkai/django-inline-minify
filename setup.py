from setuptools import setup

setup(name='django-inline-minify',
      version='0.01',
      description="Django template filter for minifying inline scripts",
      long_description="",
      author='Markus Kaiserswerth',
      author_email='mkai@sensun.org',
      license='GPL',
      packages=['inlineminify'],
      zip_safe=True,
      install_requires=['django', 'webassets'],
)
