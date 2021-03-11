# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

from devpi_common.request import new_requests_session

from devpi_slack import __version__


# simple duplicate message suppression for multiple formats of the same package
# the hook is triggered once per format upload
last_message = None


def devpiserver_indexconfig_defaults():
    return {"slack_icon": None, "slack_hook": None, "slack_user": None}


def devpiserver_on_upload_sync(log, application_url, stage, project, version):
    slack_hook = stage.ixconfig.get("slack_hook") or os.getenv("SLACK_HOOK")
    slack_icon = stage.ixconfig.get("slack_icon") or os.getenv(
        "SLACK_ICON", "http://doc.devpi.net/latest/_static/devpicat.jpg")
    slack_user = stage.ixconfig.get(
        "slack_user") or os.getenv("SLACK_USER", "devpi")
    if not slack_hook:
        return

    message = "Uploaded {}=={} to {}".format(
        project,
        version,
        application_url
    )
    global last_message
    if message == last_message:
        log.debug("skipping duplicate Slack notification: %s", message)
        return

    session = new_requests_session(agent=("devpi-slack", __version__))
    try:
        r = session.post(
            slack_hook,
            data={
                'payload': json.dumps({
                    "text": message,
                    "icon_url": slack_icon,
                    "username": slack_user,
                })
            })
    except session.Errors:
        raise RuntimeError("%s: failed to send Slack notification %s",
                           project, slack_hook)

    if 200 <= r.status_code < 300:
        log.info("successfully sent Slack notification: %s", slack_hook)
        last_message = message
    else:
        log.error("%s: failed to send Slack notification: %s", r.status_code,
                  slack_hook)
        log.debug(r.content.decode('utf-8'))
        raise RuntimeError("%s: failed to send Slack notification: %s",
                           project, slack_hook)
