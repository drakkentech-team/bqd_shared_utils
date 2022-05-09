##### MAIN TABLE #####
reach = [
    # Main PDF Info
    'fuid', 'mode', 'chk_approved', 'product_sid', 'supplier_sid',
    # Sourcing
    'date', 'sourcing_office', 'qe_china_group', 'qe_name', 'email_qe',
    # Supplier Identification
    'supplier_name', 'supplier_boss_code', 'email_sup',
    # Product Identification
    'product_name_supp', 'product_family', 'product_name', 'subsidiary',
    # Product specifications
    'pack_weight', 'prd_weight', # Other product info is nested
    # Comment
    'notes',
    # Reserved for the QE/NPD/QCC
    'Case_à_cocher', 'comment',
    # 2 - Validation
    'chk_gc'
]


##### NESTED DATA #####
reach_nested = {
    "r": (
        # Inner field names
        ['f1'],
        # Suffix
        ['product'],
        # Field Name (Category)
        ['typology', 'description', 'size', 'color']
    )
}


##### SUB TABLES #####


##### PACKAGES #####


reach_1_map = {
    # MAIN TABLE
    "main_table": 'reach',
    "main_map": reach,
    # NESTED DATA
    "nested_data_map": reach_nested,
    # SUB TABLES
    "sub_tables": [],
    "sub_table_maps": []
}


reach_map_list = [
    reach_1_map
]
