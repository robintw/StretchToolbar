# -*- coding: utf-8 -*-
"""
/***************************************************************************
 StretchToolbar
                                 A QGIS plugin
 Provides easy access to raster stretch configuration on the toolbar
                             -------------------
        begin                : 2018-03-10
        copyright            : (C) 2018 by Robin Wilson
        email                : robin@rtwilson.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load StretchToolbar class from file StretchToolbar.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .stretch_toolbar import StretchToolbar
    return StretchToolbar(iface)
