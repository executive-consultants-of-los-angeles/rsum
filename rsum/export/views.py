#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Views for the export app."""
import os
from io import BytesIO

from django.http import HttpResponse

from export.models import ExportDocument


def index(request, graphics):
    """Export cv to word document.

    :param request: HttpRequest object for export_docx page.
    :type request: object
    :return: Word document generated by export module.
    :rtype: object
    """
    document = ExportDocument().export_word(request, graphics)

    # Special thanks to: https://stackoverflow.com/a/24122313

    target_stream = BytesIO()
    document.save(target_stream)
    length = target_stream.tell()
    response = HttpResponse(
        target_stream.getvalue(),
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "wordprocessingml.document"
        )
    )
    response['Content-Length'] = length
    response['Content-Disposition'] = (
        'attachment; filename={0}-cv.docx'.format(os.environ.get('RSUM_ENV'))
    )
    target_stream.close()
    return response
