##### MAIN TABLE #####
psi_g3_except = [
    'date', 'sourcing_office', 'qe_group', 'qe_name', 'email_qe', 
    'Champ_de_texte', 
    'supplier_boss_code', 'supplier_name', 'factory', 'factory_address', 'email_sup',
    'subsidiary', 'chk_brd_France', 'chk_brd_Italy', 'chk_brd_Croatia', 'chk_brd_Switzerland', 'chk_brd_Austria', 'chk_brd_Spain', 'chk_brd_Portugal', 'chk_brd_Turkey', 'chk_brd_Australia', 'chk_brd_CzechRepublic', 'chk_brd_NewZealand', 'chk_brd_UK', 'chk_brd_Germany', 'chk_brd_SouthAfrica', 'chk_brd_Romania', 'chk_brd_Hungary', 'chk_brd_Poland', 'chk_brd_Bulgaria', 'chk_brd_Slovakia', 'chk_brd_Serbia', 
    'TOTAL_SIZE', 'SAMPLE1_SIZE', 
    'c', 'qe_sig', 'supplier_sig', 'ihtm_sig',
    'CR_found', 'CR_max', 'CR_result', 'MJ_found', 'MJ_max', 'MJ_result', 'MI_found', 'MI_max', 'MI_result'
]

##### SUB TABLES #####
psi_g3_except_prod_info = [
    'NR', 'REF', 'CODE', 'COLOR', 'DESCRIPTION', 'FP', 'SIZE'
]
psi_g3_except_packages_mapping = {
    'outer_field': 'OPD',
    'fnl_a': ['code', 'a_l', 'a_w', 'a_h', 'a_gwnw', 'a_ply', 'a_perforation', 'a_closing'],
    'fnl_b': ['code', 'b_l', 'b_w', 'b_h', 'b_gwnw', 'b_ply', 'b_perforation', 'b_closing'],
    'target': ['code', 'L', 'W', 'H', 'gw_nw', 'ply', 'perforation', 'closing']
}

##### NESTED DATA #####
psi_g3_except_nested_1 = {
    "REPORT": (
        # Inner field names
        ['report_CR', 'report_MJ', 'report_MI'],
        # Suffix
        ['CR', 'MJ', 'MI'],
        # Field Name (Category)
        ['drop_test', 'secondary_packaging', 'primary_packaging', 'product_inspection', 'manufacturing', 'measurements', 'assembly', 'functionality', 'instructions_booklet', 'product_with_suspension', 'candles', 'christmas_trees']
    ),
    "REPORT_TOTAL": (
        # Inner field names
        ['report_CR', 'report_MJ', 'report_MI'],
        # Suffix
        ['CR', 'MJ', 'MI'],
        # Field Name (Category)
        ['total_defects']
    ),
    "DATA_S0": (
        # Inner field names
        ['NA', 'CR', 'CO'],
        # Suffix
        ['na0', 'cr0', 'co0'],
        # Field Name (Category)
        ['free_drop_test', 'drop_test_corner', 'drop_test_tilting']
    ),
    "remark_S0": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['drop_test']
    ),
    "DATA_S01": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na01', 'cr01', 'mj01', 'mi01', 'co01'],
        # Field Name (Category)
        ['wet', 'dirty', 'damaged', 'injury_risk', 'closing', 'small_label', 'imported', 'distributed', 'brand_logo', 'designation', 'number_of_pieces', 'brand_code', 'EAN_13_code', 'id_number', 'po_number', 'scheme', 'color_indication', 'made_in', 'fragile_warning', 'missing_labels', 'wrong_labels', 'location_of_labels', 'name_of_product', 'up_down']
    ),
    "remark_S01": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['secondary_packaging']
    ),
    "DATA_S02": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na02', 'cr02', 'mj02', 'mi02', 'co02'],
        # Field Name (Category)
        ['wet', 'brand_respect', 'dirty', 'damaged', 'closing', 'injury_risk', 'handles', 'movement', 'slipping', 'accessories_isolation', 'glass_protection', 'prominant_protection', 'missing_accessories', 'metallic_sheet', 'recycling_logo', 'warnings', 'graphical_charter', 'imported', 'distributed', 'brand_logo', 'designation', 'product_name', 'ecoemballage_logo', 'brand_code', 'poor_printing', 'id_number', 'po_number', 'schemes', 'set_description', 'colour', 'specific_labelling', 'made_in', 'EAN_barcode', 'EAN_code_number', 'missing_label', 'wrong_labels', 'triman_logo']
    ),
    "remark_S02": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['primary_packaging']
    ),
}
psi_g3_except_nested_2 = {
    "DATA_S03": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na03', 'cr03', 'mj03', 'mi03', 'co03'],
        # Field Name (Category)
        ['language', 'label_position', 'label_erased', 'label_removable', 'character_size', 'warning_symbols_present', 'product_reference', 'flammable_warning', 'foreign_material', 'strongly_dirty', 'colour_error_1', 'glue_mark_1', 'no_sharp_edges', 'varnish_unsticking', 'varnish_bubbles', 'moisture_contains', 'textile_quality', 'textile_shrinkage', 'tested_prototype', 'rust', 'foreign_material_inside', 'broken_components', 'deformed_components', 'dirty_product', 'colour_error_2', 'colour_variation', 'decoloration', 'knock', 'strong_scratches', 'small_scratches', 'painting_adhesion', 'coating_hardness', 'rusted_components', 'surface_condition', 'back_varnish', 'varnish_spreading', 'varnish_bump', 'glue_mark_2', 'drying', 'species_respect', 'dead_knot', 'knot_size', 'wood_filler', 'knots_display', 'resin', 'mold', 'weathered', 'sap_wood', 'flash', 'larva', 'moisture', 'grain_regularity', 'added_pieces', 'stains', 'grain_imitation_error', 'moisture_contain', 'veneer_species_error', 'panel_type', 'panel_dimensions', 'tube_section', 'section_regularity', 'strength', 'composition', 'surface_condition_metal', 'hardness', 'surface_condition_plastic', 'resistance', 'finishing', 'manufacturing_shape', 'mirror_protection_back', 'decoration', 'thickness_glass', 'foam', 'upholstery_material', 'thickness_upholstering', 'tear', 'defective_stitch', 'slipage', 'undulation', 'wrong_reference', 'covering_shrinkage', 'care_labels', 'wrong_composition_label', 'yarn_cound', 'broken_seam', 'teared_seam', 'nuance_variation', 'unmatching_nuance', 'covering_decoloration', 'insect_hole', 'suspension_type', 'suspension_number', 'suspension_resistance', 'suspension_cover']
    ),
    "remark_S03": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['product_inspection']
    ),
    "DATA_S04": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na04', 'cr04', 'mj04', 'mi04', 'co04'],
        # Field Name (Category)
        ['decor_positioning', 'moulding_edges', 'mould_absense', 'drilling', 'veneer_unsticking', 'pierced_veneer', 'veneer_bubble', 'veneer_overlap', 'sticking_resistance', 'cleanness', 'splinter', 'regular_profile', 'motif_profile_conformity', 'sanding', 'welding']
    ),
    "remark_S04": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['manufacturing']
    ),
    "DATA_S05": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na05', 'cr05', 'mj05', 'mi05', 'co05'],
        # Field Name (Category)
        ['thickness', 'diameter', 'component_dimensions', 'overall_dimensions']
    ),
    "remark_S05": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['measurements']
    ),
    "DATA_S06": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na06', 'cr06', 'mj06', 'mi06', 'co06'],
        # Field Name (Category)
        ['easy_to_assemble', 'number_of_hardwares', 'oxidized_hardwares', 'number_or_components', 'tolerance_assembling', 'assembling_conformity', 'homogeneity_colour', 'net_weight']
    ),
    "remark_S06": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['assembly']
    ),
    "DATA_S07": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na07', 'cr07', 'mj07', 'mi07', 'co07'],
        # Field Name (Category)
        ['stability', 'rigidity', 'functioning', 'strength', 'product_security']
    ),
    "remark_S07": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['functionality_safety']
    ),
    "DATA_S08": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na08', 'cr08', 'mj08', 'mi08', 'co08'],
        # Field Name (Category)
        ['availability', 'poor_printing', 'assembly_explanation', 'connecting_explanation', 'translation', 'damaged_cable_warning', 'all_warnings', 'warning_sentences_height', 'errors', 'triman_logo', 'info_tri_logo']
    ),
    "remark_S08": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['instructions_booklet']
    ),
    "DATA_S09": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na09', 'cr09', 'mj09', 'mi09', 'co09'],
        # Field Name (Category)
        ['articulation_test', 'suspension_number', 'cover', 'loading_test']
    ),
    "remark_S09": (
        # Inner field names
        ['remark'],
        # Suffix
        ['remark'],
        # Field Name (Category)
        ['product_with_suspension']
    ),
    "DATA_S10": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na10', 'cr10', 'mj10', 'mi10', 'co10'],
        # Field Name (Category)
        ['young_child_warning', 'specific_candles_warning']
    ),
    "DATA_S11": (
        # Inner field names
        ['NA', 'CR', 'MJ', 'MI', 'CO'],
        # Suffix
        ['na11', 'cr11', 'mj11', 'mi11', 'co11'],
        # Field Name (Category)
        ['injuries_risk', 'flame_burning_warning', 'no_small_elements_ingested', 'stability']
    )
}

psi_g3_except_map_1 = {
    "main_table": "psi_g3_except_1",
    "main_map": psi_g3_except,
    "sub_tables": ["psi_g3_except_prod_info"],
    "sub_table_maps": [psi_g3_except_prod_info],
    "nested_data_map": psi_g3_except_nested_1,
    "packaging_map": psi_g3_except_packages_mapping,
    "packaging_table": "psi_g3_except_packages"
}

psi_g3_except_map_2 = {
    "main_table": "psi_g3_except_2",
    "main_map": [],
    "sub_tables": [],
    "sub_table_maps": [],
    "nested_data_map": psi_g3_except_nested_2
}

psi_g3_except_map_list = [psi_g3_except_map_1, psi_g3_except_map_2]