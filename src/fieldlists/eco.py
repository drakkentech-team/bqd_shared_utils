##### MAIN TABLE #####
eco = [
    # Main PDF Info
    # 'fuid', 'mode', 'fvers', 'chk_approved',
    'supplier_sid', 'product_sid', 'mode', 'chk_approved', 'fuid',
    # Sourcing
    'date', 'sourcing_office', 'qe_china_group', 'qe_name', 'email_qe',
    # Supplier Identification
    'supplier_name', 'supplier_boss_code', 'email_sup',
    # Product Identification
    'product_name_supp', 'product_family', 'product_name', 'subsidiary',
    # Ecomballage
    'chk_no_pck', 'PwAi_weight', 'PwAi_nop', 'lst', 'chk_dsp', 'chk_tri', 'chk_imp', 'chk_ink',
    # Comment
    'notes',
    # Third Party Checked Box
    'chk_third_party',
]


##### NESTED DATA #####


##### SUB TABLES #####
eco_data = [
    'lst', 'pct_mat_typ', 'pck_qt', 'pck_wt', 'chkYg'
]


##### PACKAGES #####


eco_1_map = {
    # MAIN TABLE
    "main_table": 'eco',
    "main_map": eco,
    # NESTED DATA
    "nested_data_map": {},
    # SUB TABLES
    "sub_tables": ['eco_data'],
    "sub_table_maps": [eco_data]
}


eco_map_list = [
    eco_1_map
]
