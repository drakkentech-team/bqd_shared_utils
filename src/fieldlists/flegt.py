##### MAIN TABLE #####
flegt = [
    'chk_read_cnf', 'chk_SEP',
    # Main PDF Info
    'fuid', 'mode', 'chk_approved', 'product_sid', 'supplier_sid',
    # Sourcing
    'date', 'sourcing_office', 'qe_china_group', 'qe_name', 'email_qe',
    # Supplier Identification
    'supplier_name', 'supplier_boss_code', 'email_sup',
    # Product Identification
    'chk_chonly', 'product_name_supp', 'product_family', 'product_name', 'subsidiary',
    # Comment
    'notes'
]

flegt_all_fields = [
    'chk_read_cnf', 'chk_SEP',
    # Main PDF Info
    'fuid', 'mode', 'fvers', 'chk_approved',
    # Sourcing
    'date', 'sourcing_office', 'qe_china_group', 'qe_name', 'email_qe',
    # Supplier Identification
    'supplier_name', 'supplier_boss_code', 'supplier_ct_code', 'supplier_sispro_code', 'email_sup',
    # Product Identification
    'chk_chonly', 'product_name_supp', 'product_family', 'product_name', 'subsidiary',
    # Comment
    'notes'
]


##### NESTED DATA #####
flegt_nested = {
}


##### SUB TABLES #####
flegt_massive_wood = [
    'mw_lst_s', 'mw_lst_u', 'mw_vol', 'mw_vol_u', 'mw_lst_c', 'mw_region'
]
flegt_particle_board = [
    'pw_lst_s', 'pw_lst_u', 'pw_vol', 'pw_vol_u', 'pw_lst_c', 'pw_region'
]
flegt_plywood = [
    'pl_lst_s', 'pl_lst_u', 'pl_vol', 'pl_vol_u', 'pl_lst_c', 'pl_region'
]


##### PACKAGES #####


flegt_1_map = {
    # MAIN TABLE
    "main_table": 'flegt',
    "main_map": flegt,
    # NESTED DATA
    "nested_data_map": flegt_nested,
    # SUB TABLES
    "sub_tables": ['flegt_massive_wood', 'flegt_particle_board', 'flegt_plywood'],
    "sub_table_maps": [flegt_massive_wood, flegt_particle_board, flegt_plywood],
    "non_mandatory_sub_tables": True,
}


flegt_map_list = [
    flegt_1_map
]
