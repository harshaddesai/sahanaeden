# coding: utf8
"""
tablename = "incident_template"
table = db.define_table(tablename,
                        # A 'name' field
                        Field("incident_type",unique=True),
                        # The start time
                        Field("template",unique=True),
                        # This adds all the metadata to store
                        # information on who created/updated
                        # the record & when
                        #*s3_meta_fields()
                        )


tablename = "incident_template_def"
table = db.define_table(tablename,
                        # A 'name' field
                        Field("template_type"),
                        # The start time
                        Field("name"),
                        #*s3_meta_fields()
                        )
"""
