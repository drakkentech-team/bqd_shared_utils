
def reduce_items(item_list, to_subtract):
    """
    Subtracts items from a list.
    """

    filtered_items = []
    for item in item_list:
        if item not in to_subtract:
            filtered_items.append(item)
    return filtered_items


def remove_items_if_present(total_item_sids, related_item_sids):
    """
    Removes the related items from the total items and returns the list,
    along with a boolean of whether items were removed.
    """

    items_were_removed = False
    for item_sid in related_item_sids:
        if item_sid in total_item_sids:
            total_item_sids.remove(item_sid)
            items_were_removed = True

    return total_item_sids, items_were_removed


def filter_docs_to_delete(sql_get_basic_data_func, product_sid, existing_docs, adding_items_already_provided=[]):
    """
    Filters a list of existing documents to to remove only the most recent
    documents with at least one item from the product that is the latest.

    Parameters:
        product_sid (int): to get all the total related items.
        existing_docs (list) -> (tuples): each document's basic information
                            (sid, doc_specific_sid, path, filename)

    Returns:
        filtered_list (list) -> (tuples): documents' information linked to
                            documents to be deleted.
    """

    product_items = sql_get_basic_data_func("items", "sid", f"WHERE product_sid = {product_sid}")
    total_item_sids = [item[0] for item in product_items]

    if adding_items_already_provided:
        total_item_sids = reduce_items(total_item_sids, adding_items_already_provided)

    filtered_list = []
    # rearrange the list by when the email was received, with newest first
    # reverse_chrono_existing_docs = sorted(existing_docs, key=lambda r: r[4])[::-1]

    for doc in existing_docs[::-1]:
        doc_sid = doc[0]
        related_items = sql_get_basic_data_func("item_doc", "item_sid", f"WHERE doc_sid = {doc_sid}")
        related_item_sids = [tup[0] for tup in related_items]

        total_item_sids, items_were_removed = remove_items_if_present(total_item_sids, related_item_sids)
        if not items_were_removed:
            filtered_list.insert(0, doc)

    return filtered_list
