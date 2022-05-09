psi_lighting_fl = ['date', 'sourcing_office', 'qe_group', 'qe_name', 'email_qe', 'supplier_boss_code', 'supplier_name', 'factory', 'factory_address', 'email_sup', 'subsidiary', 'chk_brd_France', 'chk_brd_Italy', 'chk_brd_Croatia', 'chk_brd_Switzerland', 'chk_brd_Austria', 'chk_brd_Spain', 'chk_brd_Portugal', 'chk_brd_Turkey', 'chk_brd_Australia', 'chk_brd_CzechRepublic', 'chk_brd_NewZealand', 'chk_brd_UK', 'chk_brd_Germany', 'chk_brd_SouthAfrica', 'chk_brd_Romania', 'chk_brd_Hungary', 'chk_brd_Poland', 'chk_brd_Bulgaria', 'chk_brd_Slovakia', 'chk_brd_Serbia', 'TOTAL_SIZE', 'SAMPLE1_SIZE', 'Champ_de_texte', 'c', 'qe_sig', 'supplier_sig', 'ihtm_sig', 'CR_found', 'CR_max', 'CR_result', 'MJ_found', 'MJ_max', 'MJ_result', 'MI_found', 'MI_max', 'MI_result']
psi_lighting_prod_info_fl = ['NR', 'REF', 'CODE', 'COLOR', 'DESCRIPTION', 'FP', 'SIZE']
psi_lighting_nested_1 = {}
psi_lighting_nested_1["REPORT"] = (['report_CR', 'report_MJ', 'report_MI'], ['Cr', 'Mj', 'Mi'], ['drop_test_report', 'secondary_packaging', 'primary_packaging', 'prod_inspection'])
psi_lighting_nested_1["REPORT_TOTAL"] = (['report_CR', 'report_MJ', 'report_MI'], ['Cr', 'Mj', 'Mi'], ['total_defects'])
psi_lighting_nested_1["DATA_S0"] = (['NA', 'CR', 'CO'], ['Na', 'Cr', 'Co'], ['drop_test', 'drop_test_corner', 'drop_test_tilting'])
psi_lighting_nested_1["DATA_S01"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['wet_package_sec', 'dirty_packaging_sec', 'packaging_damaged_sec', 'injury_risk_sec', 'presence_sec', 'marking_language', 'importer_sec', 'logo_sec', 'prod_designation_sec', 'prod_quantity_sec', 'brand_code_sec', 'ean_code_sec', 'id_number_sec', 'order_number_presence', 'prod_scheme_sec', 'color_indication_sec', 'prod_name_sec', 'made_in_sec', 'fragile_sec', 'recycling_logo_sec', 'supplier_sec'])
psi_lighting_nested_1["DATA_S02"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['wet_packaging', 'dirty_packaging', 'damaged_packaging', 'broken_lighting', 'package_closing', 'injury_risk', 'handles_presence', 'movement', 'accessories_isolation', 'packaging_material_plastic', 'recycling_logo_prim', 'warning_sentences_prim', 'distributor_prim', 'importer_prim', 'logo_prim', 'prod_designation_prim', 'prod_scheme_prim', 'set_description', 'color_finishing', 'eco_emballage', 'brand_code_prim', 'poor_printing_prim', 'id_number_prim', 'po_number_prim', 'prod_number_prim', 'ratting_voltage', 'frequency_prim', 'ratting_wattage', 'supply_nature_prim', 'bulb_wattage_number', 'bulb_type_prim', 'bulb_drawing', 'class_prim', 'ip_marking_prim', 'flammable_logo_prim', 'distance_symbol_prim', 'ce_logo_prim', 'ean_barcode_number_prim', 'bulb_included_logo', 'fragile_logo', 'bin_logo', 'energy_labelling', 'erp_data', 'decoration_purposes', 'triman_logo_prim'])
psi_lighting_packages_mapping = {'outer_field': 'OPD', 'fnl_a': ['code', 'a_l', 'a_w', 'a_h', 'a_gwnw', 'a_ply', 'a_perforation', 'a_closing'], 'fnl_b': ['code', 'b_l', 'b_w', 'b_h', 'b_gwnw', 'b_ply', 'b_perforation', 'b_closing'], 'target': ['code', 'L', 'W', 'H', 'gw_nw', 'ply', 'perforation', 'closing']}

psi_lighting_nested_2 = {}
psi_lighting_nested_2["DATA_S03"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['labels_language', 'rating_label', 'additional_label', 'marking_label', 'label_easily_removed', 'character_size', 'distributor_brand_name', 'model_name', 'id_number', 'po_number', 'brand_code', 'power_rating', 'frequency', 'max_power', 'supply_nature', 'power_bulb', 'bulb_type', 'class', 'ip_marking', 'warning_presence', 'flammable_logo', 'distance_symbol', 'ce_logo', 'crossed_bin', 'lighting_studied_sphere', 'lamp_symbol', 'lighting_studied_lamp', 'input_output_voltage', 'transformer_supplier_name', 'adaptor_model_number', 'transformer_frequency_label', 'transformer_ce_logo', 'cut_off_temperature', 'transformer_supply_current', 'transformer_crossed_bin', 'double_isolation_logo', 'transformer_class', 'transformer_specific_marking', 'transformer_power_label', 'short_circuit_logo', 'conforama', 'foreign_mat', 'strongly_dirty', 'color_error', 'lighting_damaged', 'lamp_scratches', 'lamp_scratches_small', 'glue_mark', 'sharp_edges', 'paint_holding_lighting', 'varnish_unsticking', 'varnish_bubble', 'pvc_plastic', 'bulb_presence', 'moisture_content', 'textile_quality', 'textile_shrinkage', 'prototype_conformity', 'rust_presence', 'cracked_shield_symbol', 'warning_symbol_presence', 'overall_dimensions', 'head_dimensions', 'tube_dimensions', 'base_dimensions', 'protection_presence', 'assembly_rust_presence', 'ac_switch', 'basic_insulation', 'assembly_bushing_presence', 'assembly_resistance', 'assembly_sharp_edge'])

psi_lighting_nested_3 = {}
psi_lighting_nested_3["DATA_S03"] = (['NA', 'CR', 'MJ', 'MI', 'CO'], ['Na', 'Cr', 'Mj', 'Mi', 'Co'], ['ceramic_lamps', 'halogen_lamps', 'stability', 'lighting_test', 'bulb_mounting', 'abnormal_vibration', 'switch_malfunction', 'cable_rotation', 'live_parts', 'wires_fixed', 'wireways', 'terminal_block', 'switch_fixed', 'wood_contact', 'glass_shield', 'bushing_fixed', 'earthing', 'mechanical_stress', 'cable_movement', 'y_z_type', 'socket_conformity', 'lvd_report', 'terminal_block_presence', 'terminal_block_mounted', 'hi_pot_test', 'dimmer_function', 'noiseless_dimmer', 'creepage_distance', 'replaceable', 'hi_pot_test_all_classes', 'hi_pot_test_sleeves', 'grounding_test', 'adequate_grounding_test', 'thermal_test_normal', 'thermal_test_abnormal', 'torque_test_holder', 'torque_test_screws', 'pull_test_wire', 'pull_test_luminaires', 'adjusting_device_test', 'impact_test', 'free_wire_test', 'cable_warning_symbol', 'power_cord_damage', 'flexible_chord_damage', 'chord_anchorage_presence', 'chord_anchorage_position', 'plastic_part_ceramic_lamps', 'chord_anchorage_damage', 'cable_diameter', 'bushing_presence', 'earth_wire', 'cable_length_conformity', 'ib_available', 'ib_poor_printing', 'assembly_explanation', 'connecting_explanation', 'bulb_ref', 'lang_translation', 'warning_cable_damage', 'warning_lighting', 'shield_ref', 'all_warnings', 'warning_bulb_contact', 'warning_strangulation', 'warning_sentences_3mm', 'ib_errors', 'triman_logo', 'info_tri_logo', 'earth_marking', 'continuity_test', 'earth_wire_longer', 'double_isolation'])

psi_lighting_nested_4 = {}
psi_lighting_nested_4["remark_S0"] = (['remark'], ['S0'], ['remark'])
psi_lighting_nested_4["remark_S01"] = (['remark'], ['S01'], ['remark'])
psi_lighting_nested_4["remark_S02"] = (['remark'], ['S02'], ['remark'])
psi_lighting_nested_4["remark_S03"] = (['remark'], ['S03'], ['remark'])

psi_lighting_map_1 = {
    "main_table": 'psi_lighting_1',
    "main_map": psi_lighting_fl,
    "nested_data_map": psi_lighting_nested_1,
    "sub_tables": ['psi_lighting_prod_info'],
    "sub_table_maps": [psi_lighting_prod_info_fl],
    "packaging_table": 'psi_lighting_packages',
    "packaging_map": psi_lighting_packages_mapping,
}

psi_lighting_map_2 = {
    "main_table": 'psi_lighting_2',
    "main_map": [],
    "nested_data_map": psi_lighting_nested_2,
    "sub_tables": [],
    "sub_table_maps": []
}

psi_lighting_map_3 = {
    "main_table": 'psi_lighting_3',
    "main_map": [],
    "nested_data_map": psi_lighting_nested_3,
    "sub_tables": [],
    "sub_table_maps": []
}

psi_lighting_map_4 = {
    "main_table": 'psi_lighting_4',
    "main_map": [],
    "nested_data_map": psi_lighting_nested_4,
    "sub_tables": [],
    "sub_table_maps": []
}

psi_lighting_map_list = [psi_lighting_map_1, psi_lighting_map_2, psi_lighting_map_3, psi_lighting_map_4]
