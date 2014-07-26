tablename = "templte_test_table1_abrakadabra"
table = db.define_table(tablename,
                        # A 'name' field
                        Field("name"),
                        # The start time
                        Field("start"),
                        # The facilitator
                        Field("facilitator"),
                        # This adds all the metadata to store
                        # information on who created/updated
                        # the record & when
                        *s3_meta_fields()
                        )
