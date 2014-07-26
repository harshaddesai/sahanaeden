# -*- coding: utf-8 -*-

__all__ = ["S3myModel"
           ]

from gluon import *
from gluon.storage import Storage
from ..s3 import *

# =============================================================================
class S3WaterModel(S3Model):
    """
        Water Sources
    """

    names = ["table_one",
             "table_two",
             ]

    def model(self):

        T = current.T

        # Shortcuts
        crud_strings = current.response.s3.crud_strings
        define_table = self.define_table

        # -----------------------------------------------------------------------------
        # Gauges
        #
        # @ToDo: Link together ones on same river with upstream/downstream relationships
        #
        
        tablename = "table_one"
        table = define_table(tablename,
                             Field("name",
                                   label=T("Name")),
                             Field("code",
                                   label=T("Code")),
                             *s3_meta_fields())
"""
        ADD_GAUGE = T("Add Gauge")
        crud_strings[tablename] = Storage(
            title_create = ADD_GAUGE,
            title_display = T("Gauge Details"),
            title_list = T("Gauges"),
            title_update = T("Edit Gauge"),
            title_search = T("Search Gauges"),
            title_map = T("Map of Gauges"),
            subtitle_create = T("Add New Gauge"),
            label_list_button = T("List Gauges"),
            label_create_button = ADD_GAUGE,
            msg_record_created = T("Gauge added"),
            msg_record_modified = T("Gauge updated"),
            msg_record_deleted = T("Gauge deleted"),
            msg_list_empty = T("No Gauges currently registered"),
            name_nice = T("Gauge"),
            name_nice_plural = T("Gauges"))
"""
        # -----------------------------------------------------------------------------
        # Rivers
       tablename = "table_two"
        table = define_table(tablename,
                             Field("name",
                                   label=T("Name"),
                                   requires = IS_NOT_EMPTY()),
                             s3_comments(),
                             *s3_meta_fields())
"""
        # CRUD strings
        ADD_RIVER = T("Add River")
        crud_strings[tablename] = Storage(
            title_create = ADD_RIVER,
            title_display = T("River Details"),
            title_list = T("Rivers"),
            title_update = T("Edit River"),
            title_search = T("Search Rivers"),
            subtitle_create = T("Add New River"),
            label_list_button = T("List Rivers"),
            label_create_button = ADD_RIVER,
            msg_record_created = T("River added"),
            msg_record_modified = T("River updated"),
            msg_record_deleted = T("River deleted"),
            msg_list_empty = T("No Rivers currently registered"))
"""
        #represent = S3Represent(lookup = tablename)
        #river_id = S3ReusableField("river_id", table,
        #                           requires = IS_NULL_OR(IS_ONE_OF(db, "water_river.id", represent)),
        #                           represent = represent,
        #                           label = T("River"),
        #                           comment = S3AddResourceLink(c="water",
        #                                                       f="river",
        #                                                       title=ADD_RIVER),
        #                           ondelete = "RESTRICT")

        # ---------------------------------------------------------------------
        # Pass names back to global scope (s3.*)
        #
        return dict()

# END =========================================================================
