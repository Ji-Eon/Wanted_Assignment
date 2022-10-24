def concept_drug(concept_id):
    query= """
            SELECT * from de.drug_exposure where drug_concept_id = ${concept_id};
            """
            
    return query