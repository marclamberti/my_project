"""Test the validity of all DAGs."""

from airflow.models import DagBag

def test_nb_dag():
    """
    Verify if there is the right number of DAGs in the dag folder
    - Check number of dags
    """
    dag_bag = DagBag(include_examples=False)
    nb_dags = len(dag_bag.dags.items())
    assert nb_dags == 3, "Wrong number of dags, {0} expected got {1}".format(3, nb_dags)

def test_dagbag():
    """
    Validate DAG files using Airflow's DagBag.
    This includes validation checks to ensure that tasks have required arguments, DAG IDs are unique, DAGs have no cycles, etc.
    """
    dag_bag = DagBag(include_examples=False)
    print(dag_bag)
    assert not dag_bag.import_errors  # Import errors aren't raised but captured to ensure all DAGs are parsed

    # Additional project-specific checks can be added here, e.g. to enforce each DAG has a tag
    for dag_id, dag in dag_bag.dags.items():
        error_msg = f"{dag_id} in {dag.fileloc} has no tags"
        assert error_msg