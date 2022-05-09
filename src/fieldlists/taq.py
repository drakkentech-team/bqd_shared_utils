##### MAIN TABLE #####
taq = [
    'sourcing',
    'supplier_sislvendor_code',
    'supp_name', 'supp_address', 'supp_product', 'supp_zzcode', 'supp_participant',
    'grade_percent',
    'chk_first_audit', 'chk_re_audit',
    'min_avg', 'max_avg'
]

##### SUB TABLES #####
taq_raw_material_list = [
    'spc', 'coo', 'sup'
]
taq_sup_factory_loc = [
    'prd', 'pcp', 'smf', 'qps'
]

##### NESTED DATA #####
taq_nested = {
    "r_nc": (
        # Inner field names
        ['nc'],
        # Suffix
        ['comment'],
        # Field Name (Category)
        ['strong_points', 'improved_points', 'general_conclusion']
    )
}

taq_map_1 = {
    "main_table": "taq_1",
    "main_map": taq,
    "sub_tables": ["taq_raw_material_list", "taq_sup_factory_loc"],
    "sub_table_maps": [taq_raw_material_list, taq_sup_factory_loc],
    "nested_data_map": taq_nested,
    "packaging_map": None,
    "packaging_table": None,
    "non_mandatory_sub_tables": True
}

taq_map_2 = {
    "main_table": "taq_2",
    "main_map": [],
    "sub_tables": [],
    "sub_table_maps": [],
    "nested_data_map": {}
}

taq_map_3 = {
    "main_table": "taq_3",
    "main_map": [],
    "sub_tables": [],
    "sub_table_maps": [],
    "nested_data_map": {}
}

taq_map_4 = {
    "main_table": "taq_4",
    "main_map": [],
    "sub_tables": [],
    "sub_table_maps": [],
    "nested_data_map": {}
}

taq_map_list = [taq_map_1, taq_map_2, taq_map_3, taq_map_4]
