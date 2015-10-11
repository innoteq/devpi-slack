# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from devpi_common.request import new_requests_session
from devpi_slack import __version__

import json


def devpiserver_indexconfig_defaults():
    return {"slack_hook": None}


def devpiserver_on_upload_sync(log, application_url, stage, projectname, version):
    slack_hook = stage.ixconfig.get("slack_hook")
    if not slack_hook:
        return

    session = new_requests_session(agent=("devpi-slack", __version__))
    try:
        r = session.post(
            slack_hook,
            data={
                'payload': json.dumps({
                    "text": "Uploaded {}=={} to {}".format(
                        projectname,
                        version,
                        application_url
                    ),
                    "icon_url": "http://doc.devpi.net/latest/_static/devpicat.jpg",
                    "username": "devpi",
                })
            })
    except session.Errors:
        raise RuntimeError("%s: failed to send Slack notification %s",
                           projectname, slack_hook)

    if 200 <= r.status_code < 300:
        log.info("successfully sent Slack notification: %s", slack_hook)
    else:
        log.error("%s: failed to send Slack notification: %s", r.status_code,
                  slack_hook)
        log.debug(r.content)
        raise RuntimeError("%s: failed to send Slack notification: %s",
                           projectname, slack_hook)
