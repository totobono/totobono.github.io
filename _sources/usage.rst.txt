Usage
=====

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``LogAnalytics.build_signature(customer_id, shared_key, date, content_length, method, content_type, resource)`` function:

.. autofunction:: LogAnalytics.build_signature

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`LogAnalytics.build_signature`
will raise an exception.

.. autoexception:: LogAnalytics.InvalidKindError

.. _installation:

Installation
------------

To use Lumache, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache