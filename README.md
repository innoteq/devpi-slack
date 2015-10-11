devpi-slack: Slack notification plugin for devpi-server
=======================================================

Installation
------------

``devpi-slack`` needs to be installed alongside ``devpi-server``.

You can install it with::

    pip install devpi-slack

For ``devpi-server`` there is no configuration needed, as it will automatically discover the plugin through calling hooks using the setuptools entry points mechanism.

Details about configuration below.

Configuration
-------------

devpi-slack can trigger Slack notifications upon package upload.

    devpi index /testuser/dev slack_hook=https://hooks.slack.com/services/XXX/YYY/ZZZ
