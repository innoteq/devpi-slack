# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

from devpi_common.request import new_requests_session

from devpi_slack import __version__


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

    session = new_requests_session(agent=("devpi-slack", __version__))
    try:
        r = session.post(
            slack_hook,
            data={
                'payload': json.dumps({
                    "text": "Uploaded {}=={} to {}".format(
                        project,
                        version,
                        application_url
                    ),
                    "icon_url": slack_icon,
                    "username": slack_user,
                })
            })
    except session.Errors:
        raise RuntimeError("%s: failed to send Slack notification %s",
                           project, slack_hook)

    if 200 <= r.status_code < 300:
        log.info("successfully sent Slack notification: %s", slack_hook)
    else:
        log.error("%s: failed to send Slack notification: %s", r.status_code,
                  slack_hook)
        log.debug(r.content)
        raise RuntimeError("%s: failed to send Slack notification: %s",
                           project, slack_hook)
