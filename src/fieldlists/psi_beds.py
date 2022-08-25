##### MAIN TABLE #####
psi_beds_1 = [
    # Sourcing
    'date', 'sourcing_office', 'qe_group', 'qe_name', 'email_qe',
    # Supplier Identification
    'supplier_boss_code', 'supplier_sislvendor_code', 'supplier_name', 'factory', 'factory_address', 'email_sup',
    # Product Destination
    'subsidiary', 'chk_brd_France', 'chk_brd_Italy', 'chk_brd_Croatia', 'chk_brd_Switzerland', 'chk_brd_Austria', 'chk_brd_Spain', 'chk_brd_Portugal', 'chk_brd_Turkey', 'chk_brd_Australia', 'chk_brd_CzechRepublic', 'chk_brd_NewZealand', 'chk_brd_UK', 'chk_brd_Germany', 'chk_brd_SouthAfrica', 'chk_brd_Romania', 'chk_brd_Hungary', 'chk_brd_Poland', 'chk_brd_Bulgaria', 'chk_brd_Slovakia', 'chk_brd_Serbia',
    # Identification Comment
    'Champ_de_texte',
    # Volumetry
    'TOTAL_SIZE', 'SAMPLE1_SIZE', 'SAMPLE2_SIZE',
    # Comments and Corrective Actions
    'c', 'qe_sig', 'supplier_sig', 'ihtm_sig',
    # Sum Up of Defect Quantity
    'TND1', 'DA1', 'DR1', 'TND2', 'DA2', 'DR2'
]
psi_beds_2 = []
psi_beds_3 = []


##### NESTED DATA #####
psi_beds_1_nested = {
    "REPORT": (
        # Inner field names
        ['report_n1_MI', 'report_n2_MI', 'report_n1_MJ', 'report_n2_MJ', 'report_n1_CR', 'report_n2_CR'],
        # Suffix
        ['n1Mi', 'n2Mi', 'n1Mj', 'n2Mj', 'n1Cr', 'n2Cr'],
        # Field Name (Category)
        ['mechanical_tests', 'labelling', 'packaging', 'materials', 'workmanship', 'measurements', 'finishing', 'assembling', 'functioning', 'bed_test']
    ),
    "REPORT_TOTAL": (
        # Inner field names
        ['report_n1_MI', 'report_n2_MI', 'report_n1_MJ', 'report_n2_MJ', 'report_n1_CR', 'report_n2_CR'],
        # Suffix
        ['n1Mi', 'n2Mi', 'n1Mj', 'n2Mj', 'n1Cr', 'n2Cr'],
        # Field Name (Category)
        ['total_defects']
    ),
    "TOTAL_S": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
        ['S00_total', 'S01_total', 'S02_total', 'S03_total', 'S04_total', 'S05_total', 'S06_total', 'S07_total', 'S08_total', 'S09_total']
    ),
    "DATA_S00": (
        # Inner field names
        ['n1_MJ', 'n1_CR', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mj', 'n1Cr', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
        ['vibe_test', 'bend_stress', 'compress_test', 'shift_test', 'free_drop', 'corner_drop', 'tilt_drop']
    ),
    "remark_S00": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S00'],
        # Field Name (Category)
        ['remark']
    ),
    "DATA_S01": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
            # Labelling on Secondary Packaging
        ['lsp_missing_label', 'lsp_product_reference', 'lsp_label_quality', 'lsp_multiple_labels', 'lsp_sticked_labels', 'lsp_distributor_logo', 'lsp_product_id', 'lsp_ean_code', 'lsp_id_label', 'lsp_product_description_language', 'lsp_distributed_name_address', 'lsp_imported_name_address', 'lsp_purchase_number', 'lsp_batch_colour', 'lsp_product_description', 'lsp_sketch', 'lsp_made_in', 'lsp_product_name', 'lsp_colour', 'lsp_quantity',
            # Labelling on Primary Packaging
        'lpp_missing_label', 'lpp_product_reference', 'lpp_label_quality', 'lpp_label_position', 'lpp_size_labelling', 'lpp_sticked_labels', 'lpp_product_id', 'lpp_ean_code', 'lpp_id_label', 'lpp_xy_rank', 'lpp_localisation_hardware', 'lpp_localisation_instructions', 'lpp_batch_colour', 'lpp_product_name', 'lpp_colour', 'lpp_product_description', 'lpp_description_language', 'lpp_specific_label', 'lpp_fragile_warning', 'lpp_gross_weight', 'lpp_made_in', 'lpp_order_number', 'lpp_sketch', 'lpp_distributed_name_address', 'lpp_imported_name_address', 'lpp_logo', 'lpp_spare_parts', 'lpp_carton_info', 'lpp_triman_logo',
            # Marking
        'mk_logo', 'mk_safety_markings', 'mk_suffocation_risk', 'mk_package_marking', 'mk_id_label', 'mk_recycle_logo', 'mk_components_id', 'mk_raw_material_picture',
            # Assembly Instructions
        'ai_missing', 'ai_stages_clarity', 'ai_conformity_specification', 'ai_min_age_warning', 'ai_translation', 'ai_format', 'ai_advice', 'ai_instructions_error', 'ai_triman_logo', 'ai_conforama_subsidiary', 'ai_info_tri_logo']
    ),
    "remark_S01": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S01'],
        # Field Name (Category)
        ['remark']
    ),
    "DATA_S02": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
            # Packaging on Secondary Packaging
        ['psp_injury_risk', 'psp_damaged', 'psp_wet', 'psp_closing', 'psp_material', 'psp_movement', 'psp_slipping', 'psp_inside_protection', 'psp_dimensions', 'psp_metallic_stripes', 'psp_plastic', 'psp_strength', 'psp_method',
            # Primary Packaging
        'ppp_material_conform', 'ppp_inside_protection', 'ppp_fragile_protection', 'ppp_cleaness', 'ppp_injury_risk', 'ppp_damaged', 'ppp_wet', 'ppp_closing', 'ppp_material', 'ppp_movement', 'slipping', 'ppp_pre_assembled_protection', 'ppp_move_package', 'ppp_metallic_stripes', 'ppp_plastic', 'ppp_strength']
    ),
    "remark_S02": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S02'],
        # Field Name (Category)
        ['remark']
    )
}
psi_beds_2_nested = {
    "DATA_S03": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
            # Material (Components) on General
        ['mg_nature', 'mg_broken', 'mg_scratch', 'mg_rust', 'mg_dirt', 'mg_deform',
            # Material (Components) on Quality: Solid Wood
        'msw_species_respect', 'msw_dead_knots', 'msw_knot_size', 'msw_knot_filler', 'msw_knot_display', 'msw_resin', 'msw_mold', 'msw_weather', 'msw_sapwood', 'msw_flash', 'msw_larva', 'msw_moist', 'msw_grain', 'msw_add_pieces', 'msw_stains', 'msw_other_defects',
            # Material (Components) on Quality: Panel
        'mpl_grain_imitation', 'mpl_moist', 'mpl_quality', 'mpl_veneer_species', 'mpl_type', 'mpl_dimensions', 'mpl_bubbling', 'mpl_other_defects', 'mpl_gloss',
            # Material (Components) on Quality: Metal
        'mm_tube_section', 'mm_regular_section', 'mm_strength', 'mm_kind', 'mm_surface', 'mm_dents', 'mm_tube_ends', 'mm_solders',
            # Material (Components) on Quality: Plastic
        'mpc_hardness', 'mpc_surface_state',
            # Material (Components) on Quality, Glass, Mirror
        'mgm_resistance', 'mgm_dents', 'mgm_safety_glass', 'mgm_finishing', 'mgm_temperes_test', 'mgm_back_protection', 'mgm_decoration', 'mgm_thickness',
            # Material (Components) on Quality: Upholstering Materials
        'mum_sag', 'mum_type', 'mum_thickness',
            # Material (Components) on Quality: Covering / Textiles
        'mct_damage', 'mct_stitch', 'mct_slippage', 'mct_pluckering', 'mct_reference', 'mct_shrinkage', 'mct_care_labels', 'mct_composition_label', 'mct_yarn', 'mct_broken_seam', 'mct_damaged_seam', 'mct_tint', 'mct_nuance', 'mct_decoloration', 'mct_insect_hole', 'mct_fabric_flaws', 'mct_leather',
            # Material (Components) on Quality: Suspension
        'ms_type', 'ms_number', 'ms_resistance', 'ms_cover',
            # Material (Components) on Electric Parts
        'mep_energy_sticker', 'mep_erp_logo', 'mep_two_phrases']
    ),
    "remark_S03": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S03'],
        # Field Name (Category)
        ['remark']
    ),
    "DATA_S04": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
        ['m_minima_quality', 'm_decor', 'm_veneer_edges', 'm_mould', 'm_drilling', 'm_veneer_peel', 'm_pierced', 'm_bubble', 'm_overlap', 'm_resist_stick', 'm_cleanness', 'm_splinter', 'm_sharp_edges', 'm_regular_profile', 'm_motif_profile', 'm_sanding', 'm_solders']
    ),
    "remark_S04": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S04'],
        # Field Name (Category)
        ['remark']
    ),
    "DATA_S05": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
        ['mm_thickness', 'mm_diameter', 'mm_component_dimensions', 'mm_overall_dimensions']
    ),
    "remark_S05": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S05'],
        # Field Name (Category)
        ['remark']
    ),
    "DATA_S06": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
        ['fac_nature', 'fac_surface', 'fac_back_varnish', 'fac_colour_error', 'fac_uniform_colour', 'fac_decoloration', 'fac_glue_mark', 'fac_spread_varnish', 'fac_bubble', 'fac_drying', 'fac_varnish_bump']
    ),
    "remark_S06": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S06'],
        # Field Name (Category)
        ['remark']
    ),
    "DATA_S07": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
        ['a_easy', 'a_missing', 'a_oxodized', 'a_number', 'a_tolerance', 'a_conformity', 'a_colour', 'a_assemble']
    ),
    "remark_S07": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S07'],
        # Field Name (Category)
        ['remark']
    ),
    "DATA_S08": (
        # Inner field names
        ['n1_MI', 'n1_MJ', 'n1_CR', 'n2_MI', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mi', 'n1Mj', 'n1Cr', 'n2Mi', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
        ['fs_rigid', 'fs_safe_mark', 'fs_functioning', 'fs_strength', 'fs_corner_safety', 'fs_fall_risk', 'fs_suffocation_risk', 'fs_pinching', 'fs_jamming', 'fs_rolling', 'fs_fire_label', 'fs_technical_sheet', 'fs_90cm_beds', 'fs_stability', 'fs_vertical_load', 'fs_vertical_edge_load', 'fs_batten_width', 'fs_cross_pieces', 'fs_holes', 'fs_finger_jointing', 'fs_folding_blocking', 'fs_folding_vent']
    ),
    "remark_S08": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S08'],
        # Field Name (Category)
        ['remark']
    )
}
psi_beds_3_nested = {
    "DATA_S09": (
        # Inner field names
        ['n1_MJ', 'n1_CR', 'n2_MJ', 'n2_CR'],
        # Suffix
        ['n1Mj', 'n1Cr', 'n2Mj', 'n2Cr'],
        # Field Name (Category)
            # LABELLING OF PACKAGE
        ['bhc_safety_mention',
            # ASSEMBLING INSTRUCTIONS : LANGUAGE OF THE COUNTRY OF DESTINATION
        'bhc_sentences_warn', 'bhc_height_warn',
            # MARKING ON BED
        'bhc_child_bunk', 'bhc_security_mention', 'bhc_matress_height', 'bhc_model_name', 'bhc_batch_number', 'bhc_label_erasable', 'bhc_supplier_name_address',
            # MEASUREMENTS
        'bhc_surface_barrier_distance', 'bhc_opening_scale', 'bhc_step_faces_distance', 'bhc_step_distance', 'bhc_footstep_width', 'bhc_batten_width', 'bhc_barrier_opening', 'bhc_gaps_opening', 'bhc_barriers_distance', 'bhc_barrier_height', 'bhc_bedbase_head_space', 'bhc_dimensions_accuracy', 'bhc_cone_25mm', 'bhc_cone_60mm', 'bhc_cone_75mm', 'bhc_safe_barrier_height']
    ),
    "remark_S09": (
        # Inner field names
        ['remark'],
        # Suffix
        ['S09'],
        # Field Name (Category)
        ['remark']
    )
}


##### SUB TABLES #####
psi_beds_prod_info = [
    # Product Information
    'NR', 'REF', 'CODE', 'COLOR', 'DESCRIPTION', 'FP', 'SIZE'
]


##### PACKAGES #####
psi_beds_packages_mapping = {
    'outer_field': 'OPD',
    # Inner field names
    'fnl_a': ['code', 'a_l', 'a_w', 'a_h', 'a_gwnw', 'a_ply', 'a_perforation', 'a_closing'],
    'fnl_b': ['code', 'b_l', 'b_w', 'b_h', 'b_gwnw', 'b_ply', 'b_perforation', 'b_closing'],
    # Field Name (Category)
    'target': ['code', 'L', 'W', 'H', 'gw_nw', 'ply', 'perforation', 'closing']
}


psi_beds_1_map = {
    # MAIN TABLE
    "main_table": "psi_beds_1",
    "main_map": psi_beds_1,
    # NESTED DATA
    "nested_data_map": psi_beds_1_nested,
    # SUB TABLES
    "sub_tables": ["psi_beds_prod_info", ],
    "sub_table_maps": [psi_beds_prod_info],
    # PACKAGES
    "packaging_table": "psi_beds_packages",
    "packaging_map": psi_beds_packages_mapping
}

psi_beds_2_map = {
    # MAIN TABLE
    "main_table": "psi_beds_2",
    "main_map": psi_beds_2,
    # NESTED DATA
    "nested_data_map": psi_beds_2_nested,
    # SUB TABLES
    "sub_tables": [],
    "sub_table_maps": [],
    # PACKAGES
    "packaging_map": None,
    "packaging_table": None
}

psi_beds_3_map = {
    # MAIN TABLE
    "main_table": "psi_beds_3",
    "main_map": psi_beds_3,
    # NESTED DATA
    "nested_data_map": psi_beds_3_nested,
    # SUB TABLES
    "sub_tables": [],
    "sub_table_maps": []
}

psi_beds_map_list = [
    psi_beds_1_map,
    psi_beds_2_map,
    psi_beds_3_map
]
