##### MAIN TABLE #####
psi_tableware = [
    # Sourcing
    'date', 'sourcing_office', 'qe_group', 'qe_name', 'email_qe',
    # Supplier Identification
    'supplier_boss_code', 'supplier_sislvendor_code', 'supplier_name', 'factory', 'factory_address', 'email_sup',
    # Product destination
    'subsidiary', 'chk_brd_France', 'chk_brd_Italy', 'chk_brd_Croatia', 'chk_brd_Switzerland', 'chk_brd_Austria', 'chk_brd_Spain', 'chk_brd_Portugal', 'chk_brd_Turkey', 'chk_brd_Australia', 'chk_brd_CzechRepublic', 'chk_brd_NewZealand', 'chk_brd_UK', 'chk_brd_Germany', 'chk_brd_SouthAfrica', 'chk_brd_Romania', 'chk_brd_Hungary', 'chk_brd_Poland', 'chk_brd_Bulgaria', 'chk_brd_Slovakia', 'chk_brd_Serbia', 
    # Identification Comment
    'Champ_de_texte',
    # Volumetry
    'TOTAL_SIZE', 'SAMPLE1_SIZE',
    # COMMENTS AND CORRECTIVE ACTIONS
    'c', 'qe_sig', 'supplier_sig', 'ihtm_sig',
    # Sum up of defect quantity
    'CR_found', 'CR_max', 'CR_result', 'MJ_found', 'MJ_max', 'MJ_result', 'MI_found', 'MI_max', 'MI_result'
]

##### NESTED DATA #####
psi_tableware_nested = {
    "REPORT": (
        # Inner field names
        ['report_CR', 'report_MJ', 'report_MI'],
        # Suffix
        ['CR', 'MJ', 'MI'],
        # Field Name (Category)
        ['drop_test', 'secondary_packaging', 'primary_packaging', 'product_inspection', 'measurements', 'safety', 'instructions_booklet']
    ),
    "REPORT_TOTAL": (
        # Inner field names
        ['report_CR', 'report_MJ', 'report_MI'],
        # Suffix
        ['CR', 'MJ', 'MI'],
        # Field Name (Category)
        ['total_defects']
    ),
    "remark_S0": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['drop_test']
    ),
    "remark_S01": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['secondary_packaging']
    ),
    "remark_S02": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['primary_packaging']
    ),
    "remark_S03": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['product_inspection']
    ),
    "remark_S04": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['measurements']
    ),
    "remark_S05": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['safety']
    ),
    "remark_S06": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['instructions_booklet']
    ),
    "DATA_S0": (
        # Inner field names
        ['NA', 'CR', 'CO'],
        # Suffix
        ['na0', 'cr0', 'co0'],
        # Field Name (Category)
        ['free_drop_test', 'drop_test_corner', 'drop_test_tilting']
    ),
    "DATA_S01": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na0', 'cr0', 'mj01', 'mi01', 'co0'],
        # Field Name (Category)
        ['wet', 'dirty', 'damaged', 'injury_risk', 'closing', 'small_label', 'imported', 'distributed', 'brand_logo', 'designation', 'quantity', 'brand_code', 'EAN_13_code', 'id_number', 'po_number', 'scheme', 'color_indication', 'logo', 'wrong_label', 'made', 'name', 'up_down']
    ),
    "DATA_S02": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na02', 'cr02', 'mj02', 'mi02', 'co02'],
        # Field Name (Category)
        ['wet', 'brand_respect', 'dirty', 'damaged', 'closing', 'injury_risk', 'brand', 'import_info', 'distributed_info', 'brand_logo', 'product_designation', 'eco_label', 'brand_code', 'pe_logo', 'poor_printing', 'id', 'num_products', 'country', 'ean_barcode', 'logo_fragile', 'warning_suffocation', 'labelling', 'dimensions', 'description', 'photos_prod', 'wrong_label', 'triman_logo']
    ),
    "DATA_S03": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na03', 'cr03', 'mj03', 'mi03', 'co03'],
        # Field Name (Category)
        ['external_elements', 'colour_differences', 'deformed', 'nf_cutting_edge', 'cutting', 'incomplete', 'nf_holes', 'interrupted', 'decor_positioning', 'marks', 'flash', 'broken', 'surfaces', 'air_bubbles', 'cutlery', 'blunt', 'cracks', 'pattern_status', 'glaze_situation', 'decal_situation', 'pin_holes', 'oblique']
    ),
    "DATA_S04": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na04', 'cr04', 'mj04', 'mi04', 'co04'],
        # Field Name (Category)
        ['width', 'length', 'diameter', 'different_shape', 'wobbling', 'disjointed', 'measurement', 'weight']
    ),
    "DATA_S05": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na05', 'cr05', 'mj05', 'mi05', 'co05'],
        # Field Name (Category)
        ['no_danger', 'no_rupture']
    ),
    "DATA_S06": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na06', 'cr06', 'mj06', 'mi06', 'co06'],
        # Field Name (Category)
        ['available', 'poor_printing', 'available_translation', 'warnings', 'info_logo', 'triman_logo']
    )
}

##### SUB TABLES #####
psi_tableware_prod_info = [
    # Product Information
    'NR', 'REF', 'CODE', 'COLOR', 'DESCRIPTION', 'FP', 'SIZE'
]

##### PACKAGES #####
psi_tableware_packages_mapping = {
    'outer_field': 'OPD',
    # Inner field names
    'fnl_a': ['code', 'a_l', 'a_w', 'a_h', 'a_gwnw', 'a_ply', 'a_perforation', 'a_closing'],
    'fnl_b': ['code', 'b_l', 'b_w', 'b_h', 'b_gwnw', 'b_ply', 'b_perforation', 'b_closing'],
    # Field Name (Category)
    'target': ['code', 'L', 'W', 'H', 'gw_nw', 'ply', 'perforation', 'closing']
}

psi_tableware_map = {
    "main_table": 'psi_tableware',
    "main_map": psi_tableware,
    "sub_tables": ['psi_tableware_prod_info'],
    "sub_table_maps": [psi_tableware_prod_info],
    "nested_data_map": psi_tableware_nested,
    "packaging_map": psi_tableware_packages_mapping,
    "packaging_table": 'psi_tableware_packages',
}

psi_tableware_map_list = [
    psi_tableware_map
]