psi_bulk_fl = ['date', 'sourcing_office', 'qe_group', 'qe_name', 'email_qe', 'supplier_boss_code', 'supplier_name', 'factory', 'factory_address', 'email_sup', 'subsidiary', 'chk_brd_France', 'chk_brd_Italy', 'chk_brd_Croatia', 'chk_brd_Switzerland', 'chk_brd_Austria', 'chk_brd_Spain', 'chk_brd_Portugal', 'chk_brd_Turkey', 'chk_brd_Australia', 'chk_brd_CzechRepublic', 'chk_brd_NewZealand', 'chk_brd_UK', 'chk_brd_Germany', 'chk_brd_SouthAfrica', 'chk_brd_Romania', 'chk_brd_Hungary', 'chk_brd_Poland', 'chk_brd_Bulgaria', 'chk_brd_Slovakia', 'chk_brd_Serbia', 'TOTAL_SIZE', 'SAMPLE1_SIZE', 'Champ_de_texte', 'c', 'qe_sig', 'supplier_sig', 'ihtm_sig', 'CR_found', 'CR_max', 'CR_result', 'MJ_found', 'MJ_max', 'MJ_result', 'MI_found', 'MI_max', 'MI_result']
psi_bulk_prod_info_fl = ['NR', 'REF', 'CODE', 'COLOR', 'DESCRIPTION', 'FP', 'SIZE']
psi_bulk_nested_1 = {}
psi_bulk_nested_1["REPORT"] = (['report_CR', 'report_MJ', 'report_MI'], ['Cr', 'Mj', 'Mi'], ['drop_test_report', 'secondary_packaging', 'primary_packaging', 'prod_inspection', 'manufacturing', 'measurements', 'assembly', 'functionality', 'instructions_booklet', 'prod_with_suspension'])
psi_bulk_nested_1["REPORT_TOTAL"] = (['report_CR', 'report_MJ', 'report_MI'], ['Cr', 'Mj', 'Mi'], ['total_defects'])
psi_bulk_nested_1["DATA_S0"] = (['NA', 'CR', 'CO'], ['Na', 'Cr', 'Co'], ['drop_test', 'drop_test_corner', 'drop_test_tilting'])
psi_bulk_nested_1["DATA_S01"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['wet_package_sec', 'dirty_packaging_sec', 'packaging_damaged_sec', 'injury_risk_sec', 'closing_sec', 'presence_sec', 'distributor_sec', 'importer_sec', 'logo_sec', 'prod_designation_sec', 'quantity_sec', 'brand_code_sec', 'ean_code_sec', 'id_number_sec', 'po_number_sec', 'prod_scheme_sec', 'color_indication_sec', 'made_in_sec', 'fragile_sec', 'missing_sec', 'wrong_incomplete_sec', 'location_sec', 'prod_name_sec', 'up_down_sec'])
psi_bulk_nested_1["DATA_S02"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['wet_package_prim', 'dirty_packaging_prim', 'injury_risk_prim', 'recycling_prim', 'warning_prim', 'presence_prim', 'distributor_prim', 'importer_prim', 'logo_prim', 'brand_code_prim', 'id_number_prim', 'specific_label_prim', 'made_in_prim', 'ean_code_prim', 'triman_logo_prim'])
psi_bulk_packages_mapping = {'outer_field': 'OPD', 'fnl_a': ['code', 'a_l', 'a_w', 'a_h', 'a_gwnw', 'a_ply', 'a_perforation', 'a_closing'], 'fnl_b': ['code', 'b_l', 'b_w', 'b_h', 'b_gwnw', 'b_ply', 'b_perforation', 'b_closing'], 'target': ['code', 'L', 'W', 'H', 'gw_nw', 'ply', 'perforation', 'closing']}

psi_bulk_nested_2 = {}
psi_bulk_nested_2["DATA_S03"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['label_language', 'label_position', 'label_marking', 'label_removal', 'label_char', 'warning_sym', 'prod_ref', 'foreign_mat', 'strongly_dirty_prod', 'color_error', 'glue_mark', 'sharp_point', 'varnish_unstick', 'varnish_bubble', 'moisture', 'textile_quality', 'textile_shrink', 'prototype_conform', 'rust_presence', 'visual_foreign_mat', 'broken_component', 'deformed_component', 'dirty_prod', 'visual_color_error', 'color_var', 'decolor', 'knock', 'strong_scratches', 'small_scratches', 'paint_adhesion', 'coating_hardness', 'rusted_component', 'visual_surface_condition', 'back_varnish', 'varnish_spreading', 'varnish_bump_smears', 'visual_glue_mark', 'drying', 'species_respect', 'dead_open_knot', 'knot_size', 'wood_filler', 'knot_display', 'resin_marks', 'rot', 'crack_check', 'sap_wood', 'flash', 'larva', 'wood_moisture_content', 'regularity_color', 'wood_repair', 'stains', 'grain_imitation_error', 'panel_moisture_content', 'veneer_species_error', 'type_kind', 'dimensions', 'tube_section', 'section_regularity', 'strength', 'composition_kind', 'surface_state', 'hardness', 'plastic_surface_condition', 'resistance_type', 'finishing', 'manufacturing_shape', 'mirror_protection', 'decor', 'glass_thickness', 'foam_wadding', 'upholstery_material', 'material_thickness', 'tear_cut', 'defective_stitch', 'slippage', 'gathers', 'wrong_reference', 'shrinkage', 'care_labels', 'wrong_label', 'count_construction', 'broken_seam_thread', 'torn_seam_covering', 'nuance_variation', 'unmatching_nuance_color', 'decoloration_fastness', 'insect_hole', 'suspension_type', 'suspension_number', 'suspension_resistance', 'suspension_cover'])

psi_bulk_nested_3 = {}
psi_bulk_nested_3["DATA_S04"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['decor_position', 'moulding_edges', 'mould_absence', 'drilling', 'veneer_unsticking', 'veneer_pierced', 'veneer_bubble', 'veneer_overlap', 'sticking_resistance', 'cleanness', 'splinter', 'regular_profile', 'profile_conformity', 'sanding', 'welding'])
psi_bulk_nested_3["DATA_S05"] = (['NA', 'MJ', 'MI', 'CO'], ['Na', 'Mj', 'Mi', 'Co'], ['measurement_thickness', 'measurement_diameter', 'measurement_comp_dimensions', 'measurement_overall_dimensions'])
psi_bulk_nested_3["DATA_S06"] = (['NA', 'MJ', 'MI', 'CO'], ['Na', 'Mj', 'Mi', 'Co'], ['easy_assemble', 'hardwares_number', 'manufacturing_problem', 'component_number', 'tolerance_assembling', 'method_conformity', 'color_homogeneity', 'net_weight'])
psi_bulk_nested_3["DATA_S07"] = (['NA', 'MJ', 'MI', 'CO'], ['Na', 'Mj', 'Mi', 'Co'], ['stability', 'product_rigidity', 'functioning', 'strength_durability', 'product_security'])
psi_bulk_nested_3["DATA_S08"] = (['NA', 'MJ', 'CO'], ['Na', 'Mj', 'Co'], ['available', 'poor_printing', 'assembly_explanation', 'connecting_explanation', 'translation_available', 'warning_sentence', 'warnings_present', 'triman_logo', 'info_tri_logo'])
psi_bulk_nested_3["DATA_S09"] = (['NA', 'MJ', 'CO'], ['Na', 'Mj', 'Co'], ['articulation_suspension_test', 'product_suspension_number', 'cover', 'loading_test'])
psi_bulk_nested_3["remark_S0"] = (['remark'], ['S0'], ['remark'])
psi_bulk_nested_3["remark_S01"] = (['remark'], ['S01'], ['remark'])
psi_bulk_nested_3["remark_S02"] = (['remark'], ['S02'], ['remark'])
psi_bulk_nested_3["remark_S03"] = (['remark'], ['S03'], ['remark'])
psi_bulk_nested_3["remark_S04"] = (['remark'], ['S04'], ['remark'])
psi_bulk_nested_3["remark_S05"] = (['remark'], ['S05'], ['remark'])
psi_bulk_nested_3["remark_S06"] = (['remark'], ['S06'], ['remark'])
psi_bulk_nested_3["remark_S07"] = (['remark'], ['S07'], ['remark'])
psi_bulk_nested_3["remark_S08"] = (['remark'], ['S08'], ['remark'])
psi_bulk_nested_3["remark_S09"] = (['remark'], ['S09'], ['remark'])
psi_bulk_nested_3["remark_S10"] = (['remark'], ['S10'], ['remark'])
psi_bulk_nested_3["remark_S11"] = (['remark'], ['S11'], ['remark'])

psi_bulk_map_1 = {
    "main_table": 'psi_bulk_1',
    "main_map": psi_bulk_fl,
    "nested_data_map": psi_bulk_nested_1,
    "sub_tables": ['psi_bulk_prod_info'],
    "sub_table_maps": [psi_bulk_prod_info_fl],
    "packaging_table": 'psi_bulk_packages',
    "packaging_map": psi_bulk_packages_mapping,
}

psi_bulk_map_2 = {
    "main_table": 'psi_bulk_2',
    "main_map": [],
    "nested_data_map": psi_bulk_nested_2,
    "sub_tables": [],
    "sub_table_maps": []
}

psi_bulk_map_3 = {
    "main_table": 'psi_bulk_3',
    "main_map": [],
    "nested_data_map": psi_bulk_nested_3,
    "sub_tables": [],
    "sub_table_maps": []
}

psi_bulk_map_list = [psi_bulk_map_1, psi_bulk_map_2, psi_bulk_map_3]