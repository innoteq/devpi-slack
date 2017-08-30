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

    devpi index /testuser/dev slack_icon=http://doc.devpi.net/latest/_static/devpicat.jpg slack_hook=https://hooks.slack.com/services/XXX/YYY/ZZZ slack_user=devpi

Environment Variables:

Optionally, you can pass environment variables to configure the plugin.

- ``SLACK_HOOK`` to adjust the Slack hook URL used. Defaults to the devpi slack_hook value above. (Note: slack_hook provided by devpi takes precedence. Setting both will default to the value specified in devpi)
- ``SLACK_ICON`` to adjust the Slack icon used. Defaults to: <http://doc.devpi.net/latest/_static/devpicat.jpg>
- ``SLACK_USER`` to adjust the Slack username used. Defaults to: devpi
