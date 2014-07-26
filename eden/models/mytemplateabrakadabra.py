tablename = "templte_test_table1"
table = db.define_table(tablename,
                        # A 'name' field
                        Field("incident_type"),
                        # The start time
                        Field("template"),
                        # The facilitator
                        Field("start"),
                        Field("facilitator"),
                        # This adds all the metadata to store
                        # information on who created/updated
                        # the record & when
                        *s3_meta_fields()
                        )
