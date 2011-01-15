=============
Dynamic_forms
=============

Dynamic_forms is a small Django exercice to answer the following question :

    | Give a working code example for dynamic form in django:
    | 
    | Base form should have fields: name, email(Number, "-" and " " allowed), phone and sex(as boolean).
    | and Dynamic form A should inherit the Base form with adding field: Birthday 
    | and Dynamic form B should inherit the Base form with adding field: Upload image
    | 
    | We want to see Your working forms with Ajax and without any js.


Installation
------------

If you have virtualenvwrapper, start with::

    $ mkvirtualenv Dynamic_forms

Then download the project::

    $ git clone git@github.com:Fandekasp/dynamic_forms.git

Go to the project, install the required libraries::

    $ cd dynamic_forms
    $ pip install -r requirements.txt

Finally, create the database (you should have sqlite3 installed)::

    $ ./manage.py syncdb


Start
-----

::

    $ ./manage.py runserver

You can also run the tests::

    $ ./manage.py test contact

And get some statistiques on these tests::    

    $ mkdir coverage
    $ ./manage.py test_coverage contact
