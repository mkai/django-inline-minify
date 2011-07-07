from setuptools import setup

setup(name='django-inline-minify',
      version='0.02',
      description="Django template tag for minifying inline scripts",
      long_description="",
      author='Markus Kaiserswerth',
      author_email='mkai@sensun.org',
      license='GPL',
      packages=['inlineminify'],
      zip_safe=True,
      install_requires=['django', 'webassets'],
)
