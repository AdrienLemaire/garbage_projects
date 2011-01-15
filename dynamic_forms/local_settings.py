'''
Exceptionnally, I have put my local_settings file in the git project.
I have added coverage and django-coverage to the requirements.txt as well.
'''


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'contact',
    'django_coverage',
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = "/Users/Fandekasp/Documents/django/dynamic_forms/coverage"
COVERAGE_MODULE_EXCLUDES = ['tests$', 'settings$', 'urls$',
                            'common.views.test', '__init__', 'django',
                            'migrations', 'fixtures$', 'templates$']
