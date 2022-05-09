psi_textile_fl = ['date', 'sourcing_office', 'qe_group', 'qe_name', 'email_qe', 'supplier_boss_code', 'supplier_name', 'factory', 'factory_address', 'email_sup', 'subsidiary', 'chk_brd_France', 'chk_brd_Italy', 'chk_brd_Croatia', 'chk_brd_Switzerland', 'chk_brd_Austria', 'chk_brd_Spain', 'chk_brd_Portugal', 'chk_brd_Turkey', 'chk_brd_Australia', 'chk_brd_CzechRepublic', 'chk_brd_NewZealand', 'chk_brd_UK', 'chk_brd_Germany', 'chk_brd_SouthAfrica', 'chk_brd_Romania', 'chk_brd_Hungary', 'chk_brd_Poland', 'chk_brd_Bulgaria', 'chk_brd_Slovakia', 'chk_brd_Serbia', 'TOTAL_SIZE', 'SAMPLE1_SIZE', 'Champ_de_texte', 'c', 'qe_sig', 'supplier_sig', 'ihtm_sig', 'CR_found', 'CR_max', 'CR_result', 'MJ_found', 'MJ_max', 'MJ_result', 'MI_found', 'MI_max', 'MI_result']
psi_textile_prod_info_fl = ['NR', 'REF', 'CODE', 'COLOR', 'DESCRIPTION', 'FP', 'SIZE']
psi_textile_nested_1 = {}
psi_textile_nested_1["REPORT"] = (['report_CR', 'report_MJ', 'report_MI'], ['Cr', 'Mj', 'Mi'], ['drop_test_report', 'secondary_packaging', 'prod_packing', 'prod_inspection', 'measurements', 'safety', 'instructions_booklet'])
psi_textile_nested_1["REPORT_TOTAL"] = (['report_CR', 'report_MJ', 'report_MI'], ['Cr', 'Mj', 'Mi'], ['total_defects'])
psi_textile_nested_1["DATA_S0"] = (['NA', 'CR', 'CO'], ['Na', 'Cr', 'Co'], ['drop_test', 'drop_test_corner', 'drop_test_tilting'])
psi_textile_nested_1["DATA_S01"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['wet_package_sec', 'dirty_packaging_sec', 'packaging_damaged_sec', 'injury_risk_sec', 'closing_sec', 'presence_sec', 'wrong_incomplete_sec', 'location_sec', 'distributor_sec',  'importer_sec', 'logo_sec', 'prod_designation_sec', 'quantity_sec', 'brand_code_sec', 'ean_code_sec', 'id_number_sec', 'po_number_sec', 'prod_scheme_sec', 'color_indication_sec', 'prod_name_sec', 'up_down_sec'])
psi_textile_nested_1["DATA_S02"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['wet_packing', 'graphical_charter', 'dirty_packaging', 'damaged_packaging', 'package_closing', 'injury_risk', 'poly_bag', 'brand_charter', 'leaflet_presence', 'importer', 'distributor', 'logo', 'prod_designation', 'recycling_mark', 'brand_code', 'plastic_logo', 'id_number', 'prod_number', 'manufacturing_country', 'ean_barcode', 'ean_code', 'suffocation_warning', 'composition_presence', 'specific_weight', 'care_symbols', 'size_presence', 'set_description', 'specific_labelling', 'prod_photo', 'wrong_incomplete', 'triman_france', 'blinds_warning', 'biocides', 'logo_conforama', 'prod_code', 'ean_13_barcode', 'po_id', 'composition', 'care_symbols_label', 'france_only', 'blinds_warning_label'])
psi_textile_packages_mapping = {'outer_field': 'OPD', 'fnl_a': ['code', 'a_l', 'a_w', 'a_h', 'a_gwnw', 'a_ply', 'a_perforation', 'a_closing'], 'fnl_b': ['code', 'b_l', 'b_w', 'b_h', 'b_gwnw', 'b_ply', 'b_perforation', 'b_closing'], 'target': ['code', 'L', 'W', 'H', 'gw_nw', 'ply', 'perforation', 'closing']}

psi_textile_nested_2 = {}
psi_textile_nested_2["DATA_S03"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['contamination_05_1', 'contamination_2_up', 'fabric_damages', 'slub_05_1', 'slub_1_up', 'hole', 'open_seam', 'broken_stitch_05_1', 'broken_stitch_15_up', 'uneven_hem', 'loose_stitch', 'shell_material_flaws', 'unsecured_label', 'stains', 'broken_missing_button', 'barcode_fault', 'broken_embroidery', 'bad_smell', 'moisture', 'wet_item', 'print_overlapping', 'print_register', 'missing_label', 'misprint_05', 'misprint_1_up', 'smudgy_print', 'streaks', 'shade_variation', 'wrong_assortment', 'untrimmed_thread', 'darn', 'design_upside_down', 'wavy_stitch', 'needle_mark', 'style', 'shell_material_qualities', 'shell_material_not_straight', 'hemlines', 'shell_material_color', 'color_difference', 'seams', 'seam_allowance', 'faulty_buttonholes', 'faulty_zippers', 'badly_pressed', 'glazing', 'shrinkage', 'laundering_color_fastness', 'rubbing_color_fastness'])
psi_textile_nested_2["DATA_S04"] = (['NA', 'MJ', 'CO'], ['Na', 'Mj', 'Co'], ['width', 'length', 'neck_height', 'neck_opening', 'drop'])
psi_textile_nested_2["DATA_S05"] = (['NA', 'MJ', 'CO'], ['Na', 'Mj', 'Co'], ['broken_needle', 'sharp_points'])
psi_textile_nested_2["DATA_S06"] = (['NA', 'MJ', 'CO'], ['Na', 'Mj', 'Co'], ['available', 'poor_printing', 'translation_available', 'warnings_present', 'sentence_height', 'ib_errors', 'info_tri_logo', 'triman_logo'])
psi_textile_nested_2["remark_S0"] = (['remark'], ['S0'], ['remark'])
psi_textile_nested_2["remark_S01"] = (['remark'], ['S01'], ['remark'])
psi_textile_nested_2["remark_S02"] = (['remark'], ['S02'], ['remark'])
psi_textile_nested_2["remark_S03"] = (['remark'], ['S03'], ['remark'])
psi_textile_nested_2["remark_S04"] = (['remark'], ['S04'], ['remark'])
psi_textile_nested_2["remark_S05"] = (['remark'], ['S05'], ['remark'])
psi_textile_nested_2["remark_S06"] = (['remark'], ['S06'], ['remark'])

psi_textile_map_1 = {
    "main_table": 'psi_textile_1',
    "main_map": psi_textile_fl,
    "nested_data_map": psi_textile_nested_1,
    "sub_tables": ['psi_textile_prod_info'],
    "sub_table_maps": [psi_textile_prod_info_fl],
    "packaging_table": 'psi_textile_packages',
    "packaging_map": psi_textile_packages_mapping,
}

psi_textile_map_2 = {
    "main_table": 'psi_textile_2',
    "main_map": [],
    "nested_data_map": psi_textile_nested_2,
    "sub_tables": [],
    "sub_table_maps": []
}

psi_textile_map_list = [psi_textile_map_1, psi_textile_map_2]