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


##### FLEGT #####
possible_sections = [
    [
        'tab_sbd_ch',
        ['pct_w', 'vol_w', 'vol_u1', 'pct_o', 'vol_o', 'vol_u1', 'pct_o', 'vol_o', 'vol_u1', 'weight', 'chk_recycled', 'chk_mixedPlywood'],
        ['pct_wood_1', 'vol_wood_1', 'vol_u_wood_1', 'pct_board_1', 'vol_board_1', 'vol_u_board_1', 'pct_other_1', 'vol_other_1', 'vol_u_other_1', 'pct_weight_1', 'chk_recycled', 'chk_mixedPlywood']
    ],
    [
        'tab_sbd_ch_crt',
        ['lst_crt1', 'prd_crt_code', 'prd_crt_pct', 'cac_oth_certificate', 'certificate_dov', 'nam_certificate', 'cac_oth_invoice', 'invoice_dov', 'nam_invoice'],
        ['lst_crt1_1', 'prd_crt_code_1', 'prd_crt_pct_1', 'cac_oth_certificate_1', 'certificate_dov_1', 'nam_certificate_1', 'cac_oth_invoice_1', 'invoice_dov_1', 'nam_invoice_1']
    ],
    [
        'tab_sbd_ch_det',
        ['lst_s1', 'lst_u1', 'vol_1', 'vol_u1', 'lst_c1', 'lst_s2', 'lst_u2', 'vol_2', 'vol_u2', 'lst_c2', 'lst_s3', 'lst_u3', 'vol_3', 'vol_u3', 'lst_c3']
    ],
    [
        'tab_sbd_oth',
        ['pct_w', 'pct_p', 'pct_m', 'pct_g', 'pct_o', 'pct_t', 'weight'],
        ['pct_wood_2', 'pct_plastic_2', 'pct_metal_2', 'pct_glass_2', 'pct_other_2', 'pct_total_2', 'pct_weight_2']
    ],
    [
        'tab_sbd_oth_crt',
        ['chk_seu', 'radio actor operator trader', 'chk_fli', 'nam_fli', 'chk_cli', 'nam_cli', 'chk_ind', 'nam_ind', 'lst_crt1', 'prd_crt_code', 'prd_crt_pct', 'cac_oth_certificate', 'certificate_dov', 'nam_certificate', 'cac_oth_invoice', 'invoice_dov', 'nam_invoice'],
        ['chk_seu', 'actor', 'chk_fli', 'nam_fli', 'chk_cli', 'nam_cli', 'chk_ind', 'nam_ind', 'lst_crt1_2', 'prd_crt_code_2', 'prd_crt_pct_2', 'cac_oth_certificate_2', 'certificate_dov_2', 'nam_certificate_2', 'cac_oth_invoice_2', 'invoice_dov_2', 'nam_invoice_2']
    ],
    [
        'tab_sbd_oth_sht',
        ['pct_r', 'vol_r', 'vol_r_u', 'pct_n', 'vol_n', 'vol_n_u']
    ]
]


flegt_special_data = {
    "possible_sections": possible_sections
}

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
    "flegt_special_data": flegt_special_data
}


flegt_map_list = [
    flegt_1_map
]
