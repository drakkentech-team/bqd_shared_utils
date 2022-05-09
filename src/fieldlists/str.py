

str_fn = ['date', 'sourcing_office', 'qe_group', 'qe_name', 'email_qe', 'supplier_sislvendor_code', 'supplier_name', 'factory', 'factory_address', 'email_sup', 'product_family', 'subsidiary', 'chk_brd_France', 'chk_brd_Italy', 'chk_brd_Croatia', 'chk_brd_Switzerland', 'chk_brd_Austria', 'chk_brd_Spain', 'chk_brd_Portugal', 'chk_brd_Turkey', 'chk_brd_Australia', 'chk_brd_CzechRepublic', 'chk_brd_NewZealand', 'chk_brd_UK', 'chk_brd_Germany', 'chk_brd_SouthAfrica', 'chk_brd_Romania', 'chk_brd_Hungary', 'chk_brd_Poland', 'chk_brd_Bulgaria', 'chk_brd_Slovakia', 'chk_brd_Serbia', 'Champ_de_texte', 'overall_comment', 'chk_pass', 'chk_modif', 'chk_fail']
str_prod_info_fn = ['supplier_pdt_name', 'supplier_pdt_code', 'brand_pdt_name', 'brand_pdt_code', 'f_desc', 'color', 'o_desc', 'chk_brd_fr']
str_nested = {}

str_nested["r"] = (['comment'], ['Co'], ['certificates', 'weight', 'packaging', 'labelling', 'assembly_instruction', 'quality', 'machining', 'color', 'aesthetic', 'assembly_quality', 'stability', 'safety', 'functionality', 'tech_sheet_conformity', 'steinhoff_label'])

str_map = {
    "main_table": 'str',
    "main_map": str_fn,
    "nested_data_map": str_nested,
    "sub_tables": ['str_prod_info'],
    "sub_table_maps": [str_prod_info_fn],
    # "packaging_table": 'psi_bulk_packages',
    # "packaging_map": psi_bulk_packages_mapping,
}

str_map_list = [str_map, ]
