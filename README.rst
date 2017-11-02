Mobius Python API Client
========================

|Version| |Python Versions|

The Mobius Python Client provides simple access to the Mobius API for
applications written on Python

Installation
------------

Install the package with ``pip``:

::

    $ pip install pymobius

Usage
-----

For importing library use:

.. code:: python

    from pymobius import Mobius

The library need to be configured with your API secret key which you can
create in `Mobius DApp Store <https://mobius.network/store/developer>`__

.. code:: python

    mobius = Mobius(api_key='your_api_key')

Examples
~~~~~~~~

.. code:: python

    data = mobius.app_store.balance(app_uid='f9e5e943', email='mail@example.com')

    if data['num_credits'] > 0:
        mobius.app_store.use(app_uid='f9e5e943', email='mail@example.com', num_credits=1)

Methods
-------

-  .. rubric:: ``mobius.app_store.balance(app_uid, email)``
      :name: mobius.app_store.balanceapp_uid-email

   Get balance of credits for email.

-  .. rubric:: ``mobius.app_store.use(app_uid, email, num_credits)``
      :name: mobius.app_store.useapp_uid-email-num_credits

   Use numCredits from user with email.

-  .. rubric:: ``mobius.tokens.register(token_type, name, symbol, address)``
      :name: mobius.tokens.registertoken_type-name-symbol-address

   Register a token.

-  .. rubric:: ``mobius.tokens.balance(token_uid, address)``
      :name: mobius.tokens.balancetoken_uid-address

   Query the number of tokens specified by the token.

-  .. rubric:: ``mobius.tokens.create_address(token_uid, managed)``
      :name: mobius.tokens.create_addresstoken_uid-managed

   Create an address for the token.

-  .. rubric:: ``mobius.tokens.register_address(token_uid, address)``
      :name: mobius.tokens.register_addresstoken_uid-address

   Register an address for the token.

-  .. rubric:: ``mobius.tokens.transfer_managed(token_address_uid, address_to, num_tokens)``
      :name: mobius.tokens.transfer_managedtoken_address_uid-address_to-num_tokens

   Transfer tokens from a Mobius managed address to a specified address.

-  .. rubric:: ``mobius.tokens.transfer_info(token_address_transfer_uid)``
      :name: mobius.tokens.transfer_infotoken_address_transfer_uid

   Get the status and transaction hash of a Mobius managed token
   transfer.

More information
----------------

See the `REST API docs <https://mobius.network/docs/>`__

.. |Version| image:: https://img.shields.io/pypi/v/pymobius.svg
   :target: https://pypi.org/project/pymobius/
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/pymobius.svg
   :target: https://pypi.org/project/pymobius/
